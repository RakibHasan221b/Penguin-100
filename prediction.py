import requests
import joblib
import pandas as pd

# Fetch the new penguin data from the API
response = requests.get("http://130.225.39.127:8000/new_penguin/")
print(f"Status Code: {response.status_code}")
print(f"Response JSON: {response.json()}")  # Debug print

if response.status_code == 200:
    data = response.json()

    # Check the data structure before using it
    print("Fetched Data:", data)  # Debug print

    sample_data = {
        "bill_length_mm": data.get('bill_length_mm'),
        "bill_depth_mm": data.get('bill_depth_mm'),
        "flipper_length_mm": data.get('flipper_length_mm'),
        "body_mass_g": data.get('body_mass_g')
    }

    # Ensure all values are present
    if None in sample_data.values():
        print("❌ Error: Missing values in sample_data:", sample_data)
    else:
        # Load the trained model
        model = joblib.load("penguin_classifier.pkl")

        # Get feature names from the trained model
        expected_features = model.feature_names_in_

        # Convert the sample data into a DataFrame
        sample_input = pd.DataFrame([sample_data], columns=expected_features)

        # Make a prediction
        prediction = model.predict(sample_input)

        # Map the predicted label to species name
        species_mapping = {0: "Adelie", 1: "Chinstrap", 2: "Gentoo"}
        predicted_species = species_mapping[prediction[0]]

        print("✅ Predicted Penguin Species:", predicted_species)
else:
    print("❌ Failed to fetch data from the API")
