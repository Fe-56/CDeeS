import torch
import pd

def predict(data):
    model_path = '../models/deam_feedforward_nn_essentia_best_overall_opensmile_gemaps_normalised.pt'
    model = torch.load(model_path)
    
    # load the feature set
    features = pd.read_csv(data)
    # drop Unnamed:0 column
    features = features[features.columns[1:]]
    features = features.drop('song_id', axis=1)
    features_tensor = torch.tensor(features.values, dtype=torch.float64)

    input_test_data = features_tensor.float()

    with torch.no_grad():
        test_pred = model(input_test_data)

    # Separate the output into valence and arousal
    valence_pred = test_pred[0]
    arousal_pred = test_pred[1]
    return valence_pred, arousal_pred