# Telco Customer Churn Prediction – Logistic Regression + Streamlit

[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![Streamlit App](https://img.shields.io/badge/Live-App-green)](https://churn-prediction-akwardhan.streamlit.app)

Built an end-to-end churn prediction pipeline on Telco customer data using business-focused EDA, logistic regression modeling, and a Streamlit web application. Designed to help telecom operators reduce customer churn through early prediction and targeted intervention strategies.

---

## 📌 Objective

To analyze customer behavior and deploy a machine learning model that predicts churn risk in real-time — enabling businesses to prioritize retention of high-risk customers.

---

## 📦 Dataset Overview

- **Source:** Kaggle – Telco Customer Churn  
- **Records:** ~7,043 customer profiles  
- **Target Variable:** `Churn` (Yes → 1, No → 0)  
- **Features:** tenure, contract type, monthly charges, services, tech support, and demographics

---

## 📊 Business Insights (From EDA)

| Insight Area | Finding |
|--------------|---------|
| 📆 **Tenure** | Over 50% of churned users had tenure < 6 months |
| 📄 **Contract Type** | 2-year contract churn: ~2%, monthly plan churn: ~55% |
| 💸 **Monthly Charges** | Churn rate increased for charges > ₹75 |
| 🧩 **Tech Support** | Users without tech support churned ~3× more |
| 🧠 **Multi-Service** | Bundled users churned less |
| 👥 **Demographics** | Gender not significant; seniors churn slightly more |

---

## 🛠️ Feature Engineering

Created business-relevant features to enhance model quality:

- `tenure_group`: Buckets like 0–6, 6–12, 12+ months
- `high_value_user`: Customers with charges in top 25%
- `multi_service`: Customers with phone + internet + streaming

Applied one-hot encoding for categorical features and scaling for numeric values.

---

## 🤖 Model Training

| Model | Accuracy | Recall | F1 Score |
|-------|----------|--------|----------|
| **Logistic Regression** | ~80% | ~77% | 0.81 |
| Random Forest | ~78% | ~75% | 0.79 (not selected)

✅ **Final Model:** Logistic Regression  
Chosen due to slightly higher performance and better explainability for business stakeholders.

Evaluated using:
- Accuracy
- Confusion Matrix  
- Classification Report

---

## 🚀 Streamlit App (Real-Time Deployment)

Built a responsive web application using Streamlit:
- Takes customer inputs (contract, tenure, charges, support, services)
- Outputs churn prediction and probability
- Helps business teams forecast churn risk before it happens

📸 _[Optional Screenshot Placeholder: `screenshots/streamlit_app_demo.png`]_

---


---

## 🧠 Tools & Technologies

- Python: Pandas, NumPy, Scikit-learn  
- Streamlit: Real-time web interface  
- Matplotlib & Seaborn: Data visualizations  
- Google Colab: Development  
- Git & GitHub: Version control + collaboration

---

## 📈 Business Impact

This project enables telecom companies to:
- Identify churn-prone customers proactively  
- Understand behavioral and service-related churn drivers  
- Deploy a lightweight tool to assist retention teams in targeting high-risk users  
- Reduce churn-related revenue loss with data-backed decisions

---

## 🔗 Dataset

- [Telco Customer Churn – Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)


---
---

## 📌 Author

**Anmol Kirtiwardhan**  
🌐 Explore all my projects & live apps: [akwardhan.github.io](https://akwardhan.github.io)
