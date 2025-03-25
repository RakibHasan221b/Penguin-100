import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# ✅ Load Data from the cleaned database
conn = sqlite3.connect("data/penguins.db")
df = pd.read_sql("SELECT * FROM penguins_cleaned", conn)
conn.close()

# ✅ Ensure no missing values in selected features
df = df.dropna(subset=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "species_id"])

# ✅ Select features and target variable
X = df[["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]]
y = df["species_id"]  # Use numeric species_id instead of species name

# ✅ Stratified train-test split (preserves class distribution)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ✅ Train RandomForest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ✅ Predict on test data
y_pred = model.predict(X_test)

# ✅ Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# ✅ Print classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# ✅ Save trained model
joblib.dump(model, "penguin_classifier.pkl")
print("✅ Model training complete. Model saved as 'penguin_classifier.pkl'.")
