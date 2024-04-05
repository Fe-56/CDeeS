import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def process_song(df_opensmile_features):
    # normalisation
    scaler = get_normalisation_scaler()

    df_opensmile_gemaps_features_normalised = pd.DataFrame(scaler.transform(df_opensmile_features))

    return df_opensmile_gemaps_features_normalised

# helper functions

def get_normalisation_scaler():
    df_best_model_trained_features = pd.read_csv('./UI/opensmile_gemaps_features.csv')
    
    df_best_model_trained_features = df_best_model_trained_features.drop('song_id', axis=1)
    scaler = MinMaxScaler()
    scaler.fit(df_best_model_trained_features)

    return scaler