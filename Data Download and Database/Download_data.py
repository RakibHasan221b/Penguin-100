import pandas as pd

# Dataset URL (direct link)
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

# Load dataset from the URL
penguins = pd.read_csv(url)

# Create 'data' folder if it doesn’t exist
import os
os.makedirs("data", exist_ok=True)

# Save the dataset as a CSV file
penguins.to_csv("data/penguins.csv", index=False)

print("✅ Dataset downloaded and saved as 'data/penguins.csv'")
