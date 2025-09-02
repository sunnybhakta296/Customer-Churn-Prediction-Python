import joblib
from flask import Flask, request, jsonify
import numpy as np
app = Flask(__name__)

# Load the trained model
model = joblib.load('customer_churn_rf_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Expecting a dictionary of feature values
    input_features = np.array([data['features']])
    prediction = model.predict(input_features)[0]
    return jsonify({'churn_prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)

    # Example curl command to test the prediction API:
    # Replace the feature values with actual values from your dataset

    # curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d "{\"features\": [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]}"
    # returns
    # {
    #   "churn_prediction": 1
    # }