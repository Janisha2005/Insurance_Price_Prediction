# 🏥 Insurance_Price_Prediction

A Streamlit web application that predicts insurance claim costs based on user-provided inputs such as the number of children, past claims, consultations, hospital expenses, and annual salary. The underlying model is trained using machine learning techniques.

## 📂 Project Structure

- ├── insurance_app.py # Streamlit app script
- ├── insurance_data.ipynb # Data analysis and model training notebook
- ├── Insurance_Model.pkl # Trained machine learning model (required)
- └── README.md # Project documentation

## 🚀 Features

- Interactive UI to input parameters like:
  - Number of children
  - Previous claim amount
  - Number of past consultations
  - Hospital expenditure
  - Annual salary
- Real-time prediction of insurance claim costs
- Easy-to-deploy Streamlit interface

## 🧠 Model

The model is trained using a dataset of insurance-related features. It is serialized using `pickle` and loaded in the Streamlit app for inference.
