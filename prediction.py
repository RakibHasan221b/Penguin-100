import requests
import pandas as pd
import joblib
import numpy as np

# Load the trained model
model = joblib.load("penguin_classifier.pkl")

# Fetch new penguin data from API
API_URL = "http://130.225.39.127:8000/new_penguin/"
response = requests.get(API_URL)

if response.status_code == 200:
    data = response.json()
    print("Fetched Data:", data)

    # Convert data to DataFrame
    df = pd.DataFrame([data])

    # Ensure correct feature order (update if needed)
    feature_columns = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
    df = df[feature_columns]

    # Handle missing values
    df.fillna(df.mean(), inplace=True)

    # Make prediction
    prediction = model.predict(df)
    print("Predicted Species:", prediction[0])

else:
    print("Failed to fetch data. Status Code:", response.status_code)
