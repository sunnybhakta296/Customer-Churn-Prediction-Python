## Command to Run Index File and Save Model

To run your index file and save the trained model, use the following command in your project directory:

```bash
python index.py
```

This will execute the code in `index.py`, which should include the logic to train and save your model.

---

## Saving the Model

Add the following code snippet to your training script to save the trained model:

```python
import joblib

# Assuming 'model' is your trained model object
joblib.dump(model, 'model.pkl')
```

This creates a file named `model.pkl` in your project directory. You can later load this model in your API for predictions.

---

## How to Run the API

To start the prediction API locally, run:

```bash
python app.py
```

---

## Example `curl` Commands to Test the Prediction API

Below are sample `curl` commands to test the `/predict` endpoint. Each command sends a JSON payload with a `features` array.

```bash
# Example 1
curl -X POST http://127.0.0.1:5000/predict \
    -H "Content-Type: application/json" \
    -d "{\"features\": [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]}"

# Example 2
curl -X POST http://127.0.0.1:5000/predict \
    -H "Content-Type: application/json" \
    -d "{\"features\": [0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,29.85,29.85]}"

# Example 3
curl -X POST http://127.0.0.1:5000/predict \
    -H "Content-Type: application/json" \
    -d "{\"features\": [1,0,0,0,34,1,0,0,1,0,1,0,0,0,1,0,1,56.95,1889.5]}"

# Example 4
curl -X POST http://127.0.0.1:5000/predict \
    -H "Content-Type: application/json" \
    -d "{\"features\": [1,0,0,0,2,1,0,0,1,1,0,0,0,0,0,1,1,53.85,108.15]}"

# Example 5
curl -X POST http://127.0.0.1:5000/predict \
    -H "Content-Type: application/json" \
    -d "{\"features\": [1,0,0,0,45,0,0,0,1,0,1,1,0,0,1,0,2,42.3,1840.75]}"

# Example 6
curl -X POST http://127.0.0.1:5000/predict \
    -H "Content-Type: application/json" \
    -d "{\"features\": [0,0,0,0,2,1,0,1,0,0,0,0,0,0,0,1,0,70.7,151.65]}"

# Example 7
curl -X POST http://127.0.0.1:5000/predict \
    -H "Content-Type: application/json" \
    -d "{\"features\": [0,0,0,0,8,1,1,1,0,0,1,0,1,1,0,1,0,99.65,820.5]}"

# Example 8
curl -X POST http://127.0.0.1:5000/predict \
    -H "Content-Type: application/json" \
    -d "{\"features\": [1,0,0,1,22,1,1,1,0,1,0,0,1,0,0,1,3,89.1,1949.4]}"

# Example 9
curl -X POST http://127.0.0.1:5000/predict \
    -H "Content-Type: application/json" \
    -d "{\"features\": [0,0,0,0,10,0,0,0,1,0,0,0,0,0,0,0,1,29.75,301.9]}"

# Example 10
curl -X POST http://127.0.0.1:5000/predict \
    -H "Content-Type: application/json" \
    -d "{\"features\": [0,0,1,0,28,1,1,1,0,0,1,1,1,1,0,1,0,104.8,3046.05]}"

# Example 11
curl -X POST http://127.0.0.1:5000/predict \
    -H "Content-Type: application/json" \
    -d "{\"features\": [1,0,0,1,62,1,0,0,1,1,0,0,0,0,1,0,2,56.15,3487.95]}"
```

---

This dataset is used to predict whether a telecom customer will churn (leave the company) based on their demographic information, account details, and service usage. This helps businesses identify at-risk customers and take actions to improve retention.

---

### Telco Customer Churn CSV Field Descriptions

- **customerID**: Unique identifier for each customer.
- **gender**: Customer’s gender (Male/Female).
- **SeniorCitizen**: Whether the customer is a senior citizen (1 = Yes, 0 = No).
- **Partner**: Whether the customer has a partner (Yes/No).
- **Dependents**: Whether the customer has dependents (Yes/No).
- **tenure**: Number of months the customer has stayed with the company.
- **PhoneService**: Whether the customer has phone service (Yes/No).
- **MultipleLines**: Whether the customer has multiple phone lines (Yes/No/No phone service).
- **InternetService**: Type of internet service (DSL/Fiber optic/No).
- **OnlineSecurity**: Whether the customer has online security add-on (Yes/No/No internet service).
- **OnlineBackup**: Whether the customer has online backup add-on (Yes/No/No internet service).
- **DeviceProtection**: Whether the customer has device protection add-on (Yes/No/No internet service).
- **TechSupport**: Whether the customer has tech support add-on (Yes/No/No internet service).
- **StreamingTV**: Whether the customer has streaming TV service (Yes/No/No internet service).
- **StreamingMovies**: Whether the customer has streaming movies service (Yes/No/No internet service).
- **Contract**: Type of contract (Month-to-month/One year/Two year).
- **PaperlessBilling**: Whether the customer uses paperless billing (Yes/No).
- **PaymentMethod**: Payment method (Electronic check/Mailed check/Bank transfer (automatic)/Credit card (automatic)).
- **MonthlyCharges**: The amount charged to the customer monthly.
- **TotalCharges**: The total amount charged to the customer.
- **Churn**: Whether the customer has left the company (Yes/No).