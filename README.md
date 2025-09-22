UPI Mandate Failure Prediction — FinTech ML Project

This project is a complete end-to-end machine learning pipeline that predicts whether a UPI mandate (auto-debit transaction) will fail or succeed.
It is designed to simulate how fintech platforms like Razorpay handle recurring payments — using synthetic but realistic data and production-ready tools.

🔹 Features

ML Models: Logistic Regression, Random Forest, XGBoost

Flask API: Serves ML predictions via REST endpoint

Streamlit UI: Interactive frontend for testing transactions

Gemini-powered Chatbot: Answers dataset-specific queries (e.g., “Why did transaction 30201 fail?”)

Real-world Simulation: Mimics UPI recurring payment workflows

🔹 Why This Project?

Most projects stop at .predict() inside a notebook.
This project goes further by:

Deploying ML models as an API and frontend app

Integrating chatbot support for explainability

Simulating a real-world fintech scenario

Demonstrating end-to-end product readiness for recruiters and engineers

🔹 Tech Stack

Languages: Python

Libraries: pandas, scikit-learn, xgboost, matplotlib, seaborn, Faker

Frameworks: Flask, Streamlit

AI Integration: Google Gemini API (via google-generativeai)

🔹 Project Structure
UPI-Mandate-Failure-Prediction/
│── app.py                # Flask API
│── streamlit_app.py       # Streamlit frontend
│── requirements.txt       # Dependencies
│── data/                  # Synthetic dataset
│── models/                # Trained ML models
│── notebooks/             # EDA and model training notebooks
│── README.md              # Documentation

🔹 Running Locally
1️⃣ Clone the Repository
git clone https://github.com/SaiKatkar009/Upi-Mandate-Failure-Prediction.git
cd Upi-Mandate-Failure-Prediction

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Start the Flask API
python app.py

4️⃣ Launch the Streamlit App
streamlit run streamlit_app.py

🔹 Future Enhancements

Add real-world transaction datasets

Containerize with Docker

Extend to credit card/loan mandate failure prediction

Deploy on cloud (AWS/GCP/Azure)

👤 Author

Sai Katkar

📧 saikatkar009@gmail.com

🔗 LinkedIn

🖥️ GitHub
