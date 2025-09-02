import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import GridSearchCV
import joblib

# Load the dataset
df = pd.read_csv('datasets/WA_Fn-UseC_-Telco-Customer-Churn.csv')

# Display first few rows and check for missing values
print(df.head())
print(df.isnull().sum())

# Drop customerID column (not useful for prediction)
df = df.drop('customerID', axis=1)

# Convert 'TotalCharges' to numeric, coerce errors to NaN
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Fill missing values (if any) with median
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

# Encode categorical variables
for col in df.columns:
    if df[col].dtype == 'object' and col != 'Churn':
        df[col] = pd.factorize(df[col])[0]

# Encode target variable
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Split features and target
X = df.drop('Churn', axis=1)
y = df['Churn']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Training set shape:", X_train.shape)
print("Test set shape:", X_test.shape)
print("Training target distribution:\n", y_train.value_counts())
print("Test target distribution:\n", y_test.value_counts())

# Train Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# # Hyperparameter tuning using GridSearchCV

# param_grid = {
#     'n_estimators': [100, 200, 300],
#     'max_depth': [None, 10, 20, 30],
#     'min_samples_split': [2, 5, 10]
# }

# grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=3, n_jobs=-1, scoring='accuracy')
# grid_search.fit(X_train, y_train)

# print("Best Parameters:", grid_search.best_params_)
# best_model = grid_search.best_estimator_

# # Predict and evaluate with the best model
# y_pred_best = best_model.predict(X_test)
# print("Tuned Accuracy:", accuracy_score(y_test, y_pred_best))
# print("Tuned Classification Report:\n", classification_report(y_test, y_pred_best))

# Save the best model to a file
# joblib.dump(best_model, 'customer_churn_rf_model.pkl')

