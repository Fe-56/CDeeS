import torch
import pandas as pd
import json

import os
import importlib
import sys
sys.path.insert(1, './research/utils')
from paths import *

def predict(features, best_model):
    f = open(f'{MODELS_PATH}/{best_model}/config.json')
    config = json.load(f)
    model_arch = config['model_arch']
    model_weights = config['model_weights']

    # set the seed
    seed = 42
    torch.manual_seed(seed)

    features_tensor = torch.tensor(features.values, dtype=torch.float64)
    
    # load the model
    sys.path.insert(1, './research/models')
    import feedforward_nn_combined

    model = feedforward_nn_combined.NeuralNetworkCombined(features_tensor.shape[1])
    model.load_state_dict(torch.load(model_weights))
    model.eval()

    features = features_tensor.float()

    with torch.no_grad():
        pred = model(features)

    # Separate the output into valence and arousal
    valence_pred = pred[:, 0]
    arousal_pred = pred[:, 1]
    return valence_pred, arousal_pred