import os
import pandas as pd
import sqlite3

# Dataset URL (direct link)
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

# Load dataset from the URL
penguins = pd.read_csv(url)

# Create 'data' folder if it doesn’t exist
os.makedirs("data", exist_ok=True)

# Save the dataset as a CSV file
csv_path = "data/penguins.csv"
penguins.to_csv(csv_path, index=False)
print("✅ Dataset downloaded and saved as 'data/penguins.csv'")

# Create a SQLite database
db_path = "data/penguins.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create a table (if not exists)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS penguins (
        species TEXT,
        island TEXT,
        bill_length_mm REAL,
        bill_depth_mm REAL,
        flipper_length_mm REAL,
        body_mass_g REAL,
        sex TEXT
    )
''')

# Insert data into the table
penguins.to_sql("penguins", conn, if_exists="replace", index=False)
print("✅ Database created and data saved to 'data/penguins.db'")

# Close connection
conn.close()
