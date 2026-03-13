import pandas as pd

def load_eeg_data(path):
    """
    Load EEG dataset from CSV file
    """
    data = pd.read_csv(path)
    return data

if __name__ == "__main__":
    df = load_eeg_data("../data/eeg_sample_data.csv")
    print(df.head())
