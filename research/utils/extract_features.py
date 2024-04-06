import pandas as pd
import essentia
import essentia.standard as es
from essentia.standard import *

import opensmile
import json
import numpy as np

import sys
sys.path.insert(1, './research/utils')
from paths import *
from const import *

def extract_features_essentia(file):
    features, features_frames = es.MusicExtractor()(file)

    feature_names = features.descriptorNames()
    feature_values = [features[name] for name in feature_names]

    # Create a dictionary with feature names and values
    features_dict = {name: value for name, value in zip(feature_names, feature_values)}
    df_essential_all = pd.json_normalize(features_dict)

    return df_essential_all

def extract_features_opensmile(file, extractor):
    print(extractor)
    feature_set = eval(extractor['feature_set'])
    feature_level = eval(extractor['feature_level'])

    extractor = opensmile.Smile(
        feature_set=feature_set,
        feature_level=feature_level
    )
    
    df_opensmile = extractor.process_file(file)
    df_opensmile.reset_index(drop=True)
    return df_opensmile