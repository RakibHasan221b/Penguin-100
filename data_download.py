import os
import sqlite3
import pandas as pd
import seaborn as sns  # Required for dataset loading

# ✅ Step 1: Load the Penguins Dataset & Remove Null Values
penguins = sns.load_dataset("penguins").dropna()

# ✅ Step 2: Create 'data' folder if it doesn’t exist
os.makedirs("data", exist_ok=True)

# ✅ Step 3: Save dataset as CSV (for backup)
csv_path = "data/penguins.csv"
penguins.to_csv(csv_path, index=False)
print("✅ Dataset saved as 'data/penguins.csv'")

# ✅ Step 4: Connect to SQLite Database
db_path = "data/penguins.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# ✅ Step 5: Create mappings for species and islands
island_mapping = {name: idx + 1 for idx, name in enumerate(penguins["island"].unique())}
species_mapping = {name: idx + 1 for idx, name in enumerate(penguins["species"].unique())}

# ✅ Step 6: Replace text values with IDs
penguins["island_id"] = penguins["island"].map(island_mapping)
penguins["species_id"] = penguins["species"].map(species_mapping)
penguins.drop(columns=["island", "species"], inplace=True)

# ✅ Step 7: Drop old tables (if they exist)
cursor.executescript('''
    DROP TABLE IF EXISTS islands;
    DROP TABLE IF EXISTS species;
    DROP TABLE IF EXISTS penguins_cleaned;
''')

# ✅ Step 8: Create new tables with Primary & Foreign Keys
cursor.execute('''
    CREATE TABLE islands (
        island_id INTEGER PRIMARY KEY,
        island_name TEXT UNIQUE
    )
''')

cursor.execute('''
    CREATE TABLE species (
        species_id INTEGER PRIMARY KEY,
        species_name TEXT UNIQUE
    )
''')

cursor.execute('''
    CREATE TABLE penguins_cleaned (
        penguin_id INTEGER PRIMARY KEY AUTOINCREMENT,
        species_id INTEGER,
        island_id INTEGER,
        bill_length_mm REAL,
        bill_depth_mm REAL,
        flipper_length_mm REAL,
        body_mass_g REAL,
        sex TEXT,
        FOREIGN KEY (island_id) REFERENCES islands(island_id),
        FOREIGN KEY (species_id) REFERENCES species(species_id)
    )
''')

# ✅ Step 9: Insert data into islands & species tables
for name, idx in island_mapping.items():
    cursor.execute("INSERT INTO islands (island_id, island_name) VALUES (?, ?)", (idx, name))

for name, idx in species_mapping.items():
    cursor.execute("INSERT INTO species (species_id, species_name) VALUES (?, ?)", (idx, name))

# ✅ Step 10: Insert transformed data into `penguins_cleaned`
penguins.to_sql("penguins_cleaned", conn, if_exists="append", index=False)

# ✅ Step 11: Commit changes and close connection
conn.commit()
conn.close()

print("✅ Database structured successfully with foreign keys!")
