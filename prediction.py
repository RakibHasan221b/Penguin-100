import pandas as pd
import joblib
import requests
import numpy as np

# Load model
model = joblib.load("penguin_classifier.pkl")

# Fetch new data
response = requests.get("API_ENDPOINT_HERE")  # Replace with your API endpoint
if response.status_code == 200:
    data = response.json()
    sample_input = pd.DataFrame([data])

    # Handle missing values by filling NaNs with the mean (or another strategy)
    sample_input.fillna(sample_input.mean(), inplace=True)

    # Make prediction
    prediction = model.predict(sample_input)

    # Save prediction
    with open("prediction.md", "w") as f:
        f.write(f"Predicted Penguin Species: {prediction[0]}\n")

else:
    print(f"Failed to fetch data, status code: {response.status_code}")
