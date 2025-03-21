import pandas as pd
import sqlite3

# Load the dataset
df = pd.read_csv("data/penguins.csv")

# Create a SQLite database
conn = sqlite3.connect("data/penguins.db")
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
df.to_sql("penguins", conn, if_exists="replace", index=False)

# Commit and close connection
conn.commit()
conn.close()

print("✅ Database created and data saved to 'data/penguins.db'")
