# 🧠 AI-Based Tagline Generator

This is a full-stack NLP project that automatically generates brand taglines using AI. It was developed as a **capstone project** for the B.Sc. in Data Science at Mulund College of Commerce (University of Mumbai), under the guidance of Dr. Hiren Dand.

It blends natural language processing (NLP), marketing psychology, and web development into a powerful creative tool for modern brands.

---

## 🎯 Project Overview

The goal was to build a web app that enables brands to generate tone-aligned, industry-specific taglines automatically. It uses scraped real-world taglines, keyword frequency analysis, and transformer-based text generation.

The project includes a research report, a web interface, Power BI visualizations, and an AI backend.

---

## 🔧 Tools & Technologies

- **Python** (Core logic, scraping, NLP)
- **NLTK** (Text preprocessing, tone detection)
- **Flask** (Web framework)
- **Bootstrap** (Frontend styling)
- **Power BI** (Keyword & tone visualization)
- **Transformer Model** (Text generation like GPT)

---

## 📌 Key Features

- 🔍 **Web Scraper**: Collected 1,000+ brand taglines across categories
- 🧬 **Keyword Frequency Analyzer**: Identified dominant keywords and industry tones
- 🧠 **Transformer-based Generator**: Created taglines using language models
- 🧰 **Custom Inputs**: Accepts brand name, keyword, tone, and archetype
- 📊 **Power BI Dashboard**: Visualizes tag structure, emotional tone, and archetype usage
- 📖 **Research Paper**: Included BLEU & ROUGE metrics and ethical discussion

---

## 🗂️ Files 
- `app.py` – Python Flask backend
- `templates/` – HTML frontend
- `static/` – CSS styling
- `taglines_dataset.csv` – Scraped tagline data
- `dashboard.pbix` – Power BI visualization
- `tagline-generator-report.pdf` – Full documentation

---

## 🚀 How to Run 

```bash
# 1. Install required libraries
pip install flask nltk openai transformers

# 2. Run the app
python app.py

# 3. Open in browser
http://localhost:5000
