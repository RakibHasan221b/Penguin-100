#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import json
import requests
import pandas as pd
import joblib
from datetime import datetime
from pathlib import Path

# API endpoint for new penguin data
API_URL = "http://130.225.39.127:8000/new_penguin/"

# Mapping species numbers to actual names
SPECIES_MAPPING = {1: "Adelie", 2: "Chinstrap", 3: "Gentoo"}

def fetch_new_penguin_data():
    """Fetch new penguin data from the API."""
    print(f"Fetching new penguin data from {API_URL}...")
    
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Remove unnecessary fields (like datetime)
        cleaned_data = {key: value for key, value in data.items() if key in ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']}
        print(f"Successfully fetched cleaned data: {cleaned_data}")
        return cleaned_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def load_model():
    """Load the trained model."""
    model_path = "penguin_classifier.pkl"  # Model is in the main folder
    if not os.path.exists(model_path):
        print(f"Error: Model file not found at {model_path}")
        sys.exit(1)
    
    return joblib.load(model_path)

def make_prediction(model, penguin_data):
    """Make prediction for the new penguin data."""
    print("Making prediction...")

    # Convert to DataFrame
    df = pd.DataFrame([penguin_data])

    # Ensure only required features are present
    required_features = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
    df = df[required_features]

    # Predict species (numerical)
    predicted_species_num = model.predict(df)[0]

    # Convert numerical prediction to species name
    predicted_species = SPECIES_MAPPING.get(predicted_species_num, "Unknown")

    # Get prediction probabilities if available
    if hasattr(model, 'predict_proba'):
        probabilities = model.predict_proba(df)[0]
        proba_dict = {SPECIES_MAPPING[i+1]: float(prob) for i, prob in enumerate(probabilities)}
    else:
        proba_dict = {"Note": "Probability information not available"}

    is_adelie = (predicted_species == 'Adelie')

    # Save prediction results
    prediction_result = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "penguin_data": penguin_data,
        "predicted_species": predicted_species,
        "species_probabilities": proba_dict,
        "is_adelie": is_adelie
    }

    return prediction_result

def save_results(prediction_result):
    """Save prediction results to JSON and update history."""
    print("Saving prediction results...")

    # Create directories if they don't exist
    Path("data/predictions").mkdir(parents=True, exist_ok=True)

    # Save latest prediction
    with open("data/predictions/latest.json", "w") as f:
        json.dump(prediction_result, f, indent=2)

    # Update prediction history
    history_path = "data/predictions/history.json"
    history = []

    if os.path.exists(history_path):
        with open(history_path, "r") as f:
            history = json.load(f)

    history.insert(0, prediction_result)  # Add new prediction at the top

    with open(history_path, "w") as f:
        json.dump(history, f, indent=2)

    print("Prediction saved successfully.")

def main():
    """Run the prediction pipeline."""
    penguin_data = fetch_new_penguin_data()
    if penguin_data is None:
        print("Skipping prediction due to data fetch error.")
        return
    
    model = load_model()
    prediction_result = make_prediction(model, penguin_data)
    save_results(prediction_result)

if __name__ == "__main__":
    main()
