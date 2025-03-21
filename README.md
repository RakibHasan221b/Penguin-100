# Project: Penguin Classification and Prediction

## 1. Overview
This project automates the daily prediction of penguin species using machine learning. It fetches new data from an API, processes it, makes a prediction using a trained classifier, and stores the results. The workflow runs every morning at 7:30 AM CET via GitHub Actions.

## 2. Files and Descriptions

### 2.1. GitHub Actions Workflow
- **`.github/workflows/daily_prediction.yml`**: Automates the daily prediction task by running the prediction script every day at 7:30 AM CET.

### 2.2. Data Processing and Storage
- **`data_processing.py`**: A consolidated script that handles:
  - Downloads the penguin data from the API.
  - Cleans the raw data, handling missing values.
  - Performs feature engineering (e.g., encoding categorical values, scaling features).
  - Stores the processed data in an SQLite database (`data/penguins.db`).

### 2.3. Penguin Classification
- **`train_test.py`**: 
  - Trains a Random Forest classifier on the cleaned penguin dataset.
  - Saves the trained model as `penguin_classifier.pkl`.

### 2.4. Prediction System
- **`prediction.py`**: 
  - Loads the trained classifier model (`penguin_classifier.pkl`).
  - Fetches new data from the API.
  - Cleans and preprocesses the data to handle missing values.
  - Makes a prediction on the penguin species.
  - Outputs the predicted species.

### 2.5. Data and Model Storage
- **`data/`**: Contains the raw and processed data files.
  - `penguins.csv`: The original dataset used for model training.
  - `penguins.db`: SQLite database storing cleaned and processed data.
- **`penguin_classifier.pkl`**: The saved Random Forest classifier model used for daily predictions.

### 2.6. Dependencies
- **`requirements.txt`**: Lists the necessary Python dependencies such as pandas, scikit-learn, Flask, joblib, etc.

## 3. How It Works
1. GitHub Actions triggers the workflow daily at 7:30 AM CET.
2. The `prediction.py` script fetches new data from the API.
3. The data is cleaned to handle any missing values.
4. The trained model (`penguin_classifier.pkl`) predicts the species.
5. The results are displayed and stored for future analysis.

## 4. Setup Instructions
1. Clone the repository:
   ```sh
   git clone https://github.com/RakibHasan221b/Penguin-100.git
   cd Penguin-100
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the data processing script (optional, if you want to preprocess data manually):
   ```sh
   python data_processing.py
   ```
4. Run the prediction script manually:
   ```sh
   python prediction.py
   ```

## 5. Notes
- Ensure your API endpoint is accessible before running the prediction script.
- The `prediction.py` script now includes data cleaning to handle missing values before making predictions.
- The GitHub Actions workflow automates the prediction daily, but you can trigger it manually if needed.

---
This project showcases a full pipeline for automating machine learning predictions on real-time data, integrating data processing, model training, and deployment via GitHub Actions.

