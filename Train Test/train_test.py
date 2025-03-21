import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Connect to database & load the data
conn = sqlite3.connect("data/penguins.db")
df = pd.read_sql("SELECT * FROM penguins", conn)
conn.close()

# Feature selection - Choose relevant features
X = df.drop(columns=["species"])  # Features: remove target column
y = df["species"]  # Target variable (classification)

# Split dataset into training (80%) and testing (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a classification model (Random Forest)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Save the trained model
joblib.dump(clf, "penguin_classifier.pkl")
print("✅ Model trained and saved as 'penguin_classifier.pkl'!")
