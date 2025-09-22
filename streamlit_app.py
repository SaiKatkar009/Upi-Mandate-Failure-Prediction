import streamlit as st
import joblib
import numpy as np
import pickle
import pandas as pd
from dotenv import load_dotenv
import os
import google.generativeai as genai


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


genai.configure(api_key=GEMINI_API_KEY)


with open('upi_mandate_transactions.pkl', 'rb') as file:
    transactions_df = pickle.load(file)


knowledge_base = transactions_df.set_index('transaction_id').T.to_dict()


model = joblib.load('upi_failure_model.pkl')

st.title('UPI Mandate Failure Prediction - Razorpay Style 🚀')
st.write('Enter transaction details to predict whether the mandate will fail or succeed.')


mandate_amount = st.number_input('Mandate Amount', min_value=1, max_value=5000, value=999)
account_balance = st.number_input('Account Balance', min_value=0.0, max_value=10000.0, value=800.00)
bank_api_latency = st.slider('Bank API Latency (ms)', min_value=100, max_value=800, value=500)
bank_success_rate = st.slider('Bank Success Rate', min_value=0.80, max_value=0.99, value=0.90)
retry_attempts = st.slider('Retry Attempts', min_value=0, max_value=3, value=1)
mandate_age_days = st.number_input('Mandate Age (days)', min_value=0, max_value=365, value=100)
previous_failures = st.slider('Previous Failures', min_value=0, max_value=10, value=2)

if st.button('Predict'):
    features = np.array([[mandate_amount, account_balance, bank_api_latency, 
                          bank_success_rate, retry_attempts, mandate_age_days, previous_failures]])
    prediction = model.predict(features)[0]
    if prediction == 1:
        st.error('❌ Prediction: Mandate Failure')
    else:
        st.success('✅ Prediction: Mandate Success')

# Gemini Chatbot
st.header('💬 Gemini-Powered Chatbot')
chat_input = st.text_input('Ask me anything about UPI mandate failures or the dataset:')

if chat_input:
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')  
    response = model.generate_content(chat_input)
    st.write('Gemini Response:')
    st.write(response.text)