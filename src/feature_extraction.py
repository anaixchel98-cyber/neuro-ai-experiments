"""
Feature extraction for EEG-like signals using Fourier Transform
"""

import numpy as np
import pandas as pd


def extract_frequency_features(df, feature_names):

    frequency_features = []

    for _, row in df[feature_names].iterrows():

        signal = row.values

        fft_vals = np.abs(np.fft.fft(signal))

        mean_freq = np.mean(fft_vals)
        max_freq = np.max(fft_vals)
        std_freq = np.std(fft_vals)

        frequency_features.append(
            {
                "fft_mean": mean_freq,
                "fft_max": max_freq,
                "fft_std": std_freq
            }
        )

    freq_df = pd.DataFrame(frequency_features)

    return freq_df
