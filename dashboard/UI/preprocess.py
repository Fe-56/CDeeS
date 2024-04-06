import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import joblib
import json

import sys
sys.path.insert(1, './research/utils')
from preprocessing import *
from paths import *
from const import *

def process_song(df_features, best_model):
    f = open(f'{MODELS_PATH}/{best_model}/config.json')
    config = json.load(f)
    extractor = config['extractor']
    extractor_name = extractor['name']
    scaler_path = config['scaler']

    if (extractor_name == EXTRACTOR_ESSENTIA):
        essentia_feature_set = extractor['essentia_feature_set']
        df_features_processed = preprocess_essentia(df_features, scaler_path, essentia_feature_set)
    elif (extractor_name == EXTRACTOR_OPENSMILE):
        df_features_processed  = preprocess_opensmile(df_features, scaler_path)

    return df_features_processed
