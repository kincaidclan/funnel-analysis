# Funnel Analysis with Downstream Probabilities

This project visualizes a user funnel through multiple web stages — from homepage to purchase — using a dual-funnel chart built with Plotly. It not only tracks where users drop off, but also shows **conversion rates** and **probabilities of advancing** to later stages.

---

## 📊 What It Does

- Displays a dual funnel: **Users** vs **Conversions**
- Calculates conversion rates per stage
- Computes **downstream probabilities** — likelihood of reaching future stages based on current stage
- Adds intelligent hover tooltips with:
  - % of previous step
  - % of initial users
  - % of total users
  - Future stage probabilities

---

## 🔍 Why It Matters

This kind of analysis is crucial for product managers and growth teams. It helps:

- Identify where users drop off most
- Quantify how far users are likely to go from each stage
- Inform A/B testing or UX changes for maximum impact

---

## 📁 Files

- `user_data.csv` — sample dataset simulating user journey data
- `funnel_analysis.py` — full code to process, analyze, and visualize the funnel
- `README.md` — project overview

---

## 🛠️ Tools Used

- Python
- Pandas
- Plotly

---

## ✅ Example Use Cases

- Product funnel diagnostics
- Marketing campaign analysis
- A/B test visualization
- Stakeholder-ready reporting

---

## 🚀 Getting Started

To run the code:

```bash
pip install pandas plotly
python funnel_analysis.py
