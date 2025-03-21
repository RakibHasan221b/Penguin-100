import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("data/penguins.db")

# Load data into a DataFrame
df = pd.read_sql("SELECT * FROM penguins", conn)

# 🛠️ Convert categorical variables to numerical values
df["sex"] = df["sex"].str.strip().str.title().map({"Male": 0, "Female": 1, "Unknown": 2})  # Fix case sensitivity
df["species"] = df["species"].map({"Adelie": 0, "Chinstrap": 1, "Gentoo": 2})
df["island"] = df["island"].astype("category").cat.codes  # Encode islands

# 🛠️ Remove unnecessary decimal points from flipper length & body mass
df["flipper_length_mm"] = df["flipper_length_mm"].astype(int)
df["body_mass_g"] = df["body_mass_g"].astype(int)

# Save the processed data back to the database
df.to_sql("penguins", conn, if_exists="replace", index=False)

# Commit and close connection
conn.commit()
conn.close()

print("✅ Feature engineering complete. Data updated in 'penguins.db'.")
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("data/penguins.db")

# Load data into a DataFrame
df = pd.read_sql("SELECT * FROM penguins", conn)

# 🛠️ Convert categorical variables to numerical values
df["sex"] = df["sex"].str.strip().str.title().map({"Male": 0, "Female": 1, "Unknown": 2})  # Fix case sensitivity
df["species"] = df["species"].map({"Adelie": 0, "Chinstrap": 1, "Gentoo": 2})
df["island"] = df["island"].astype("category").cat.codes  # Encode islands

# 🛠️ Remove unnecessary decimal points from flipper length & body mass
df["flipper_length_mm"] = df["flipper_length_mm"].astype(int)
df["body_mass_g"] = df["body_mass_g"].astype(int)

# Save the processed data back to the database
df.to_sql("penguins", conn, if_exists="replace", index=False)

# Commit and close connection
conn.commit()
conn.close()

print("✅ Feature engineering complete. Data updated in 'penguins.db'.")
