"""
Train machine learning model for cognitive load detection
using simulated EEG-like signals.
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from load_data import load_eeg_data
from preprocess import preprocess_data

data = load_eeg_data("../data/eeg_sample_data.csv")

X, y = preprocess_data(data)

model = RandomForestClassifier()

model.fit(X, y)

print("Model trained successfully")
