import pandas as pd
import opensmile
from preprocess_opensmile import process_song
from joblib import Parallel, delayed
import numpy as np

smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.GeMAPS,
    feature_level=opensmile.FeatureLevel.Functionals,
)

def extract_features(file):
    df_opensmile = smile.process_file(file)
    df_opensmile = df_opensmile.reset_index(drop=True)
    processed = process_song(df_opensmile)
    return processed