import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Load the trained model
filename = 'pages/loan_amount_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

@st.cache
def predict_expenditure(features):
    return loaded_model.predict(features)

st.title("Loan Amount Predictor 😊")
st.subheader("Enter details to predict the loan amount:")

# Input fields for features
no_of_dependents = st.number_input("Number of Dependents:", min_value=0)
education = st.selectbox("Education Level:", ['Not Graduate', 'Graduate'])
self_employed = st.selectbox("Self Employed:", ['No', 'Yes'])
income_annum = st.number_input("Annual Income:", min_value=0.0)
loan_term = st.number_input("Loan Term (in days):", min_value=0)
cibil_score = st.number_input("CIBIL Score:", min_value=300, max_value=900)
residential_assets_value = st.number_input("Residential Assets Value:", min_value=0.0)
commercial_assets_value = st.number_input("Commercial Assets Value:", min_value=0.0)
luxury_assets_value = st.number_input("Luxury Assets Value:", min_value=0.0)
bank_asset_value = st.number_input("Bank Asset Value:", min_value=0.0)

# Convert categorical features to numerical
education_num = 1 if education == 'Graduate' else 0
self_employed_num = 1 if self_employed == 'Yes' else 0

if st.button('Predict'):
    # Prepare the features for prediction
    features = np.array([[no_of_dependents, education_num, self_employed_num, income_annum, loan_term,
                          cibil_score, residential_assets_value, commercial_assets_value,
                          luxury_assets_value, bank_asset_value]])

    # Make prediction
    loan_amount = predict_expenditure(features)

    # Display the result
    st.write(f"Predicted Loan Amount: {loan_amount[0]:.2f}")
