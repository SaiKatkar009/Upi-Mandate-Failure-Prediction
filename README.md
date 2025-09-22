# UPI Mandate Failure Prediction — Fintech ML Project
This project is a complete end-to-end machine learning pipeline that predicts whether a UPI mandate (auto-debit transaction) will fail or succeed. I built this to simulate how fintech platforms like Razorpay deal with recurring payments — using realistic (but synthetic) transaction data and actual production-level tools.

It includes:

- ML models (Logistic Regression, XGBoost, Random Forest)
- A working Flask API
- A Streamlit-based user interface
- A Gemini-powered chatbot that answers dataset-specific queries (like “why did transaction 30201 fail?”)
- The idea was to go beyond just a notebook — and create something that feels closer to a real product.
# What’s in it
- Machine Learning: Trained and evaluated three models to predict failures
- Flask API: Used to serve predictions via an endpoint
- Streamlit UI: A simple frontend where anyone can test a transaction
- Gemini Chatbot (RAG): I’ve integrated Google’s Gemini to answer questions based on the dataset itself — it acts like a virtual assistant for the project.
# Why This Project?
While working on projects earlier, I realized most stop at EDA and a .predict(). I wanted to explore:

- What an ML product could look like
- How APIs and chat interfaces are now a major part of modern data apps
- How a recruiter or engineer would evaluate real-world readiness
# Tech Used
- Python (pandas, scikit-learn, xgboost)
- Flask
- Streamlit
- Google Gemini API 
- Faker (to simulate data)
- matplotlib & seaborn (for basic EDA)
# Project Structure
```bash
UPI-Mandate-Failure-Prediction/
│── app.py                # Flask API
│── streamlit_app.py       # Streamlit frontend
│── requirements.txt       # Dependencies
│── data/                  # Synthetic dataset
│── models/                # Trained ML models
│── notebooks/             # EDA & model training notebooks
│── README.md              # Documentation
```

# Running it Locally
```bash
# clone the repo
git clone https://github.com/SaiKatkar009/Upi-Mandate-Failure-Prediction.git
cd Upi-Mandate-Failure-Prediction

# install the required packages
pip install -r requirements.txt

# start the API
python app.py

# run the Streamlit app
streamlit run streamlit_app.py
