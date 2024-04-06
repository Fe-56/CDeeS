import pandas as pd
import opensmile
import numpy as np
import json

import sys
sys.path.insert(1, './research/utils')
from paths import *
from const import *
from extract_features import *

def extract_features(file, best_model):
    f = open(f'{MODELS_PATH}/{best_model}/config.json')
    config = json.load(f)
    extractor = config['extractor']
    extractor_name = extractor['name']

    if (extractor_name == EXTRACTOR_ESSENTIA):
        df_features = extract_features_essentia(file)
    elif (extractor_name == EXTRACTOR_OPENSMILE):
        df_features = extract_features_opensmile(file, extractor)

    return df_features