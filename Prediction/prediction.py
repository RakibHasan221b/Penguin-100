import requests
import joblib
import pandas as pd

# Fetch the new penguin data from the API
response = requests.get("http://130.225.39.127:8000/new_penguin/")

# If the request is successful (status code 200), proceed
if response.status_code == 200:
    # Parse the JSON response from the API
    data = response.json()

    # Map the features from the API response to a DataFrame
    sample_data = {
        "bill_length_mm": data['bill_length_mm'],
        "bill_depth_mm": data['bill_depth_mm'],
        "flipper_length_mm": data['flipper_length_mm'],
        "body_mass_g": data['body_mass_g']
    }

    # Load the trained model
    model = joblib.load("penguin_classifier.pkl")

    # Get feature names from the trained model
    expected_features = model.feature_names_in_  # This ensures correct order

    # Convert the sample data into a DataFrame with correct feature names
    sample_input = pd.DataFrame([sample_data], columns=expected_features)

    # Make a prediction
    prediction = model.predict(sample_input)

    # Map the predicted label to species name
    species_mapping = {0: "Adelie", 1: "Chinstrap", 2: "Gentoo"}
    predicted_species = species_mapping[prediction[0]]

    print("Predicted Penguin Species:", predicted_species)

else:
    print("Failed to fetch data from the API")
