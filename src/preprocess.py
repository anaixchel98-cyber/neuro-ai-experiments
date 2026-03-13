import pandas as pd

def preprocess_data(df):
    """
    Simple preprocessing: split features and labels
    """
    X = df.drop("label", axis=1)
    y = df["label"]

    return X, y
