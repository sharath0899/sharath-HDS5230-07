# Fast Food Health Checker

Check out live app at [Nutrition App](https://health-nultrition-app.onrender.com/)

## Project Summary
This project is a web-based health analysis tool designed to evaluate the nutritional quality of fast food items. It allows users to input data such as calories, saturated fat, sugar, and sodium and classifies the food item as either a healthier choice or unhealthy. A radar chart visually represents the nutritional profile of the item.

## Objectives
- Provide health classification for fast food items using rule-based logic.
- Visually display the food's nutritional composition using radar charts.
- Help users make better dietary decisions through easy-to-understand feedback.

## Technology Stack
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Data Visualization**: Matplotlib (Radar Chart)
- **Deployment**: Render (Cloud Hosting)

## Data Science Concepts Used
- **Rule-Based Modeling**: Used to classify food as healthy or unhealthy based on predefined thresholds.
- **Data Normalization**: Nutrient values are normalized for visual comparison on radar charts.
- **Data Visualization**: Radar chart generated using Matplotlib to communicate multi-dimensional health data.
- **Web Deployment**: Flask backend hosted on Render, integrating both UI and logic.
- **(Optional Extension)**: Prepares a base for using classification models or recommending alternatives based on past inputs.

## Team Members 
-- **Saikiran Boddu**
-- **Sherath Kasula**

## How to Run Locally

1. Clone the repository:
```bash
git clone
cd fastfood-health-checker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Visit [http://localhost:5000](http://localhost:5000) in your browser.

## How to Deploy on Render

1. Push code to GitHub.
2. Go to [https://render.com](https://render.com) and connect your GitHub repo.
3. Set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Deploy.

---

This project is part of a course assignment and is intended for academic demonstration purposes.