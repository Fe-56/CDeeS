import pandas as pd
import essentia
import essentia.standard as es
from essentia.standard import *
from UI.preprocess_essentia import process_song

import numpy as np

def extract_features(file):
    features, features_frames = es.MusicExtractor()(file)

    feature_names = features.descriptorNames()
    feature_values = [features[name] for name in feature_names]

    # Create a dictionary with feature names and values
    features_dict = {name: value for name, value in zip(feature_names, feature_values)}
    df_essential_all = pd.json_normalize(features_dict)
    processed = process_song(df_essential_all)

    return processed