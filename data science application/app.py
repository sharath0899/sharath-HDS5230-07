#project: fast food checker
# team: sharath kasula & saikiran boddu


from flask import Flask, render_template, request
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend before importing pyplot
import matplotlib.pyplot as plt

import os
import uuid
import numpy as np

app = Flask(__name__)
os.makedirs("static/charts", exist_ok=True)

def classify_health(data):
    reasons = []
    bonuses = []

    if data['calories'] > 600:
        reasons.append("High calories")
    if data['saturated_fat'] > 6:
        reasons.append("High saturated fat")
    if data['sodium'] > 800:
        reasons.append("High sodium")
    if data['sugar'] > 10:
        reasons.append("High sugar")
    if data['trans_fat'] > 0:
        reasons.append("Contains trans fat")
    if data['cholesterol'] > 100:
        reasons.append("High cholesterol")
    if data['total_fat'] > 20:
        reasons.append("High total fat")
    if data['fiber'] > 3:
        bonuses.append("✅ Good fiber content")
    if data['protein'] > 15:
        bonuses.append("✅ High protein")

    all_reasons = reasons + bonuses

    return ("❌ Unhealthy", all_reasons) if reasons else ("✅ Healthier choice", all_reasons)



def generate_chart(data):
    labels = ['Calories', 'Total Fat', 'Saturated Fat', 'Trans Fat', 'Cholesterol', 'Sodium',
              'Carbs', 'Sugar', 'Fiber', 'Protein']
    
    # Normalize values for a better visual scale (divide by a reasonable max)
    max_values = [1000, 50, 20, 2, 200, 2000, 100, 50, 15, 60]
    values = [
        data['calories'], data['total_fat'], data['saturated_fat'], data['trans_fat'],
        data['cholesterol'], data['sodium'], data['total_carbs'], data['sugar'],
        data['fiber'], data['protein']
    ]
    values = [v/m if m else 0 for v, m in zip(values, max_values)]

    values += values[:1]  # repeat first value to close the radar
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, values, color='darkblue', linewidth=2)
    ax.fill(angles, values, color='skyblue', alpha=0.4)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_yticklabels([])
    ax.set_title('Nutrition Radar', size=14, weight='bold')

    filename = f"{uuid.uuid4().hex}.png"
    path = f"static/charts/{filename}"
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    reasons = []
    chart_url = None

    if request.method == 'POST':
        try:
            fields = ['item_name', 'calories', 'total_fat', 'saturated_fat', 'trans_fat', 'cholesterol',
                      'sodium', 'total_carbs', 'fiber', 'sugar', 'protein']
            data = {field: request.form.get(field) for field in fields}
            for k in data:
                if k != 'item_name':
                    data[k] = float(data[k]) if '.' in data[k] else int(data[k])

            result, reasons = classify_health(data)
            chart_url = generate_chart(data)

        except Exception as e:
            result = "⚠️ Error"
            reasons = [str(e)]

    return render_template('index.html', result=result, reasons=reasons, chart_url=chart_url)

if __name__ == '__main__':
    app.run(debug=True)
