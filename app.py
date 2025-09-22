from flask import Flask, request, jsonify
import joblib
import numpy as np

model = joblib.load('upi_failure_model.pkl')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])

def predict():
    data = request.get_json(force= True)

    features = [data['mandate_amount'],
                data['account_balance'],
                data['bank_api_latency'],
                data['bank_success_rate'],
                data['retry_attempts'],
                data['mandate_age_days'],
                data['previous_failures']]
    features_array = np.array([features])

    prediction = model.predict(features_array)

    result = 'Failure' if prediction[0] == 1 else 'Success'
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)