# run this script to create the config .json file

import json
import pandas as pd

from ...utils.paths import *
from ...utils.make_scaler import *
from ...utils.get_columns import *
from ...utils.const import *

CURRENT_PATH = f'./research/models/essentia_best_valence_normalised'
FEATURE_SET_CSV = 'essentia_best_valence_features.csv'
FEATURE_SET_CSV_PATH = f'{COMBINED_PATH}/features/{FEATURE_SET_CSV}'
MODEL_ARCH_PATH = f'./research/models/feedforward_nn_combined.py'
MODEL_WEIGHTS_PATH = f'{CURRENT_PATH}/combined_feedforward_nn_essentia_best_valence_mean_normalised.pt'
SCALER_FILE_PATH = f'{CURRENT_PATH}/scaler.sav'
JSON_OUTPUT_PATH = f'{CURRENT_PATH}/config.json'

# get column names
df = pd.read_csv(FEATURE_SET_CSV_PATH)
FEATURE_COLS = get_columns_no_song_id(df)

make_scaler(
  type='normalisation',
  df=df,
  scaler_file_path=SCALER_FILE_PATH
)

test = {
  "extractor": {
    "name": EXTRACTOR_ESSENTIA, 
    "feature_set": None,
    "feature_level": None
  },
  "model_arch": MODEL_ARCH_PATH,
  "model_weights": MODEL_WEIGHTS_PATH,
  "columns": FEATURE_COLS,
  "scaler": SCALER_FILE_PATH
}

# Convert and write JSON object to file
with open(JSON_OUTPUT_PATH, "w") as outfile: 
  json.dump(test, outfile, default=vars)

# to load a .json file
# with open('configv2.json') as json_file:
#   data = json.load(json_file)
