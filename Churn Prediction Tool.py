import streamlit as st
import pandas as pd
import joblib


model = joblib.load("model.pkl")
feature_names = joblib.load("feature_names.pkl")
st.title("📉 Telco Customer Churn Prediction")
st.write("Fill in the customer details below to predict if they are likely to churn.")

contract = st.selectbox("Contract Type",["Month-to-month","One Year", "Two Year"])
tenure = st.number_input("Tenure (Months with Company)", min_value =0, max_value=72,value=12)
monthly_charges = st.number_input("Monthly Charges",min_value=0.0, max_value = 2000.0,value = 70.0)
total_charges = st.number_input("Total Charges", min_value = 0.0, max_value =12000.0, value = 12000.0)

internet_service = st.selectbox("Internet Service Type",["DSL","Fiber Optic","No"])
tech_support = st.selectbox("Tech Support",["Yes","No","No internet Service"])
payment_method = st.selectbox("Payment Method",["Electronic check"," Mailed Check"," Bank Transfer(Auto-pay)", "Credit Card(Auto-pay)"])
paperless_billing = st.selectbox("Paperless Billing?",["Yes","No"])

input_data = pd.DataFrame({
    "contract":[contract],
    "tenure":[tenure],
    "monthlyCharges":[monthly_charges],
    "TotalCharges":[total_charges],
    "InternetService":[internet_service],
    'TechSupport':[tech_support],
    "PaymentMethod":[payment_method],
    "PaperlessBilling":[paperless_billing]
})

if st.button ("🔍 Predict Churn"):

    input_encoded = pd.get_dummies(input_data)
    input_encoded = input_encoded.reindex(columns=feature_names, fill_value = 0)
    prediction = model.predict(input_encoded)[0]
    probability = model.predict_proba(input_encoded)[0][1]
    
    if prediction:
        st.error(f"⚠️ High Risk: This customer is likely to churn.(churn Probability:{probability:.2f})")
    else:
        st.success(f"✅ Low Risk: This customer is likely to stay.(churn Probability:{probability:.2f})")
