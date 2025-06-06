# app.py

from flask import Flask, render_template, request
import random
import tagline_data
from transformers import pipeline

app = Flask(__name__)

# Load the trained model
try:
    generator = pipeline('text-generation', model="./tagline_model")
    model_loaded = True #Bool value to ensure
except Exception as e:
    print(f"Error loading the model: {e}")
    generator = None
    model_loaded = False


def generate_tagline_from_model(prompt, max_length=50):
    if generator:
        try:
            generated_text = generator(prompt,
                                      max_length=max_length,
                                      num_return_sequences=1,
                                      )[0]['generated_text']
            return generated_text
        except Exception as e:
            print(f"Error generating tagline from model: {e}")
            return "Error generating tagline, please try again"
    else:
        return "Model not loaded. Using default tagline generation."

def generate_tagline(industry=None, keywords=None, tone=None, style=None):
    # Choose structure (weighted by industry if available)
    if industry and tagline_data.industries.get(industry):
        industry_data = tagline_data.industries[industry]
        structure = random.choice(industry_data.get("structures", tagline_data.structures))  # get industry structures, otherwise default
    else:
        structure = random.choice(tagline_data.structures)

    # Helper function to choose a word from a category or from a list of words directly
    def choose_word(data_source, category=None):
        if category:
            return random.choice(data_source[category])
        else:
            return random.choice(data_source)

    # Choose adjective (tone-aware)
    adjective_category = random.choice(list(tagline_data.adjectives.keys()))
    adjective = choose_word(tagline_data.adjectives, adjective_category)

    # Choose noun
    noun_category = random.choice(list(tagline_data.nouns.keys()))
    noun = choose_word(tagline_data.nouns, noun_category)

    verb = random.choice(tagline_data.verbs)
    phrase = random.choice(tagline_data.phrases)
    company = random.choice(tagline_data.companies)

    tagline = structure.replace("[Adjective]", adjective).replace("[Noun]", noun).replace("[Verb]", verb).replace("[Phrase]", phrase).replace("[Company]", company)

    # Incorporate keywords (more sophisticated)
    if keywords:
        keyword_list = [k.strip() for k in keywords.split(",")]
        for keyword in keyword_list:
            if random.random() < 0.5:  # 50% chance to include each keyword
                replaceable = [adjective, noun, verb, phrase]
                if replaceable: #Check to make sure the list has value before trying to get a value from it
                    tagline = tagline.replace(random.choice(replaceable), keyword, 1)  # only replace the first occurrence

    # Incorporate industry-specific words (if available)
    if industry and industry_data.get("keywords"):
      industry_keywords = industry_data["keywords"]
    if random.random() < 0.3:  # 30% chance to add an industry keyword if industry exists
      tagline = tagline.replace(random.choice([noun, adjective, verb, phrase]), random.choice(industry_keywords), 1) 
    return tagline

@app.route("/", methods=["GET", "POST"])
def index():
    taglines = []
    if request.method == "POST":
        industry = request.form.get("industry")
        keywords = request.form.get("keywords")
        tone = request.form.get("tone")
        style = request.form.get("style")
        num_taglines = int(request.form.get("num_taglines", 5))  # Default to 5 taglines
        use_model = request.form.get("use_model") #Take check box to see if we want to use or not

        for _ in range(num_taglines):
            if use_model and model_loaded:
                prompt = f"Industry: {industry}, Keywords: {keywords}, Tone: {tone}, Style: {style}. Tagline:"
                taglines.append(generate_tagline_from_model(prompt))
            else:  # Use Default Taglines
                taglines.append(generate_tagline(industry=industry, keywords=keywords, tone=tone, style=style))

    return render_template("index.html", taglines=taglines, industries=tagline_data.industries.keys(),
                           tones=tagline_data.tones, styles=tagline_data.styles)

if __name__ == "__main__":
    app.run(debug=True)