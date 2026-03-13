import numpy as np

def predict_cognitive_load(model, sample):
    prediction = model.predict([sample])
    return prediction
