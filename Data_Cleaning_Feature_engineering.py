import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("data/penguins.db")

# Load data into a DataFrame
df = pd.read_sql("SELECT * FROM penguins", conn)

# Check for missing values
print("Missing values in each column before cleaning:")
print(df.isnull().sum())

# Data Cleaning
# Drop rows with missing critical values
df = df.dropna(subset=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "species"])

# Optionally: Fill missing 'sex' values with "Unknown" if you want to keep it in the model
df["sex"] = df["sex"].fillna("Unknown")

# Check and describe data types of each column
print("\nData types before cleaning:")
print(df.dtypes)

# Feature Engineering
# Convert categorical variables to numerical values for 'sex' and 'species'
df["sex"] = df["sex"].str.strip().str.title().map({"Male": 0, "Female": 1, "Unknown": 2})
df["species"] = df["species"].map({"Adelie": 0, "Chinstrap": 1, "Gentoo": 2})

# Convert 'island' to numerical codes (we can drop this if it's not required for the model)
df["island"] = df["island"].astype("category").cat.codes

# Convert numerical features to the correct data type (if necessary)
df["flipper_length_mm"] = df["flipper_length_mm"].astype(float)
df["body_mass_g"] = df["body_mass_g"].astype(float)

# Drop 'island' and 'sex' if they are not needed for the model
df = df[["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "species"]]

# Check for missing values again after cleaning
print("\nMissing values in each column after cleaning:")
print(df.isnull().sum())

# Check the data types after cleaning
print("\nData types after cleaning:")
print(df.dtypes)

# Save the cleaned and feature-engineered data back to the database
df.to_sql("penguins", conn, if_exists="replace", index=False)

# Commit and close connection
conn.commit()
conn.close()

print("✅ Data cleaning and feature engineering complete. Data updated in 'penguins.db'.")
