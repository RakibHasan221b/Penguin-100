import requests
import joblib
import pandas as pd
from datetime import datetime

# Fetch new penguin data
response = requests.get("http://130.225.39.127:8000/new_penguin/")

if response.status_code == 200:
    data = response.json()

    sample_data = {
        "bill_length_mm": data['bill_length_mm'],
        "bill_depth_mm": data['bill_depth_mm'],
        "flipper_length_mm": data['flipper_length_mm'],
        "body_mass_g": data['body_mass_g']
    }

    model = joblib.load("penguin_classifier.pkl")
    expected_features = model.feature_names_in_
    sample_input = pd.DataFrame([sample_data], columns=expected_features)

    prediction = model.predict(sample_input)
    species_mapping = {0: "Adelie", 1: "Chinstrap", 2: "Gentoo"}
    predicted_species = species_mapping[prediction[0]]

    # Create Markdown content
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    markdown_content = f"# 🐧 Daily Penguin Prediction\n\n"
    markdown_content += f"**Date:** {timestamp}\n\n"
    markdown_content += f"**Predicted Species:** {predicted_species}\n\n"
    markdown_content += f"**Feature Values:**\n"
    markdown_content += f"- Bill Length (mm): {sample_data['bill_length_mm']}\n"
    markdown_content += f"- Bill Depth (mm): {sample_data['bill_depth_mm']}\n"
    markdown_content += f"- Flipper Length (mm): {sample_data['flipper_length_mm']}\n"
    markdown_content += f"- Body Mass (g): {sample_data['body_mass_g']}\n"

    # Save to prediction.md
    with open("prediction.md", "w") as f:
        f.write(markdown_content)

    print("✅ Prediction saved to prediction.md")

else:
    print("❌ Failed to fetch data from the API")
