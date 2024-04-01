import torch
import pandas as pd
from model import NeuralNetwork

def predict(features):
    # set the seed
    seed = 42
    torch.manual_seed(seed)

    features_tensor = torch.tensor(features.values, dtype=torch.float64)

    # load the model
    model_path = './UI/deam_feedforward_nn_essentia_best_valence_mean_normalised.pt'
    model = NeuralNetwork(features_tensor.shape[1])
    model.load_state_dict(torch.load(model_path))
    model.eval()

    features = features_tensor.float()

    with torch.no_grad():
        pred = model(features)

    # Separate the output into valence and arousal
    valence_pred = pred[:, 0]
    arousal_pred = pred[:, 1]
    return valence_pred, arousal_pred