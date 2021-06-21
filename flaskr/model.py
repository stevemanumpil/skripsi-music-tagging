import pickle
import pandas as pd
import numpy as np
from tensorflow.keras import models

model_name = "models/Mel-5L-256H-0.25DV-GRU.h5"

model = models.load_model(model_name)

file = open("models/labels.pickle","rb")
labels = pickle.load(file)
file.close()

DURATION = 30

def audio_predict(melgram_segments, name):
    
    melgrams = np.array(melgram_segments).reshape(-1, melgram_segments[0].shape[0], melgram_segments[0].shape[1])

    predicts = model.predict(melgrams)

    result = {}

    for idx, predict in enumerate(predicts):

        categories = np.flip(np.argsort(predict))[:10]

        tags = {}
        for cat_idx in range(len(categories)):
            tags[labels[categories[cat_idx]]] = str(predict[categories[cat_idx]])

        result[f'{name}_{idx*DURATION}-{(idx+1)*DURATION}'] = tags

    return result




    

