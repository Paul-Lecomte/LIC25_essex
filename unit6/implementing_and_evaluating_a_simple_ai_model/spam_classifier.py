"""
Spam Email Classification using Scikit-learn

This script downloads the SpamAssassin dataset from the UCI Machine Learning Repository,
trains a Naive Bayes classifier to predict whether an email is spam or not,
and evaluates the model's performance.

Dataset: Spambase dataset (https://archive.ics.uci.edu/ml/datasets/Spambase)
Source: Hopkins University, donated by Mark George, 1999.
"""

import numpy as np
import pandas as pd
import urllib.request
import os
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# URL for the Spambase dataset from UCI
DATA_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data"
DATA_FILE = "spambase.data"

def download_dataset():
    """Download the dataset if it doesn't exist locally."""
    if not os.path.exists(DATA_FILE):
        print(f"Downloading dataset from {DATA_URL}...")
        try:
            urllib.request.urlretrieve(DATA_URL, DATA_FILE)
            print("Download completed.")
        except Exception as e:
            print(f"Error downloading dataset: {e}")
            exit(1)
    else:
        print("Dataset already exists locally.")

def load_dataset():
    """Load the dataset into a pandas DataFrame."""
    # The dataset has 57 features and 1 class label (0=not spam, 1=spam)
    column_names = [f'feature_{i}' for i in range(57)] + ['is_spam']
    df = pd.read_csv(DATA_FILE, header=None, names=column_names)
    return df

def main():
    # Step 1: Download and load data
    download_dataset()
    df = load_dataset()

    print(f"Dataset shape: {df.shape}")
    print(f"First few rows:\n{df.head()}")

    # Step 2: Prepare features and target
    X = df.drop('is_spam', axis=1)  # Features
    y = df['is_spam']               # Target (0: not spam, 1: spam)

    # Step 3: Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    print(f"Training set size: {X_train.shape}")
    print(f"Test set size: {X_test.shape}")

    # Step 4: Train the model
    model = GaussianNB()
    model.fit(X_train, y_train)

    # Step 5: Make predictions
    y_pred = model.predict(X_test)

    # Step 6: Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print("\nModel Performance Metrics:")
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-Score:  {f1:.4f}")
    print("\nConfusion Matrix:")
    print(cm)
    print("(Rows: Actual, Columns: Predicted)")
    print("                 Predicted")
    print("           Not Spam  Spam")
    print(f"Actual Not Spam  {cm[0,0]:4d}   {cm[0,1]:4d}")
    print(f"Actual Spam      {cm[1,0]:4d}   {cm[1,1]:4d}")

if __name__ == "__main__":
    main()