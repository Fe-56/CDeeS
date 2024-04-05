import essentia
import essentia.standard as es

import json
import numpy as np
import pandas as pd

from paths import *

def extract_features_from_deam(audio_file):
  # get the feature names
  sample_audio = f'{DEAM_PATH_UTILS}/MEMD_audio/2.mp3'
  print(sample_audio)

  features, features_frames = es.MusicExtractor()(sample_audio)

  # Assuming 'features' is the extracted features object
  feature_names = features.descriptorNames()
  feature_values = [features[name] for name in feature_names]

  # Create a dictionary with feature names and values
  features_dict = {name: value for name, value in zip(feature_names, feature_values)}
  df_essentia_all_sample = pd.json_normalize(features_dict)

