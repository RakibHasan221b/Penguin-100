import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("data/penguins.db")

# Load data into a DataFrame
df = pd.read_sql("SELECT * FROM penguins", conn)

# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum())

# Close connection
conn.close()
