import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("data/penguins.db")

# Load data into a DataFrame
df = pd.read_sql("SELECT * FROM penguins", conn)

# Drop rows with missing numerical values
df = df.dropna(subset=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"])

# Fill missing 'sex' values with "Unknown"
df["sex"] = df["sex"].fillna("Unknown")

# Save the cleaned data back to the database
df.to_sql("penguins", conn, if_exists="replace", index=False)

# Close connection
conn.close()

print("✅ Data cleaned and saved back to the database!")
