import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("Insurance_Model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Insurance Claim Cost Prediction")

# Input fields matching model features
children = st.number_input("Number of Children", min_value=0, max_value=20, value=1, key="children_input")
claim_amount = st.number_input("Previous Claim Amount ($)", min_value=0.0, value=1000.0, step=100.0, key="claim_input")
past_consultations = st.number_input("Number of Past Consultations", min_value=0, max_value=100, value=5, key="consult_input")
hospital_expenditure = st.number_input("Hospital Expenditure ($)", min_value=0.0, value=2000.0, step=100.0, key="hospital_input")
annual_salary = st.number_input("Annual Salary (₹)", min_value=0.0, value=50000.0, step=1000.0, key="salary_input")

# Predict on button click
if st.button("Predict Insurance Cost"):
    # Prepare input array
    input_data = np.array([[children, claim_amount, past_consultations, hospital_expenditure, annual_salary]])

    # Make prediction
    prediction = model.predict(input_data)

    st.subheader("Predicted Insurance Cost:")
    st.write(f"₹{prediction[0]:,.2f}")

