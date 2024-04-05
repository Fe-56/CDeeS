import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def map_va_value_deam(value):
  old_min = 1
  old_max = 9

  new_min = -1
  new_max = 1

  mapped_value = ((value - old_min) * (new_max - new_min) / (old_max - old_min)) + new_min
  return mapped_value

def map_va_value_pmemo(value):
  old_min = 0
  old_max = 1

  new_min = -1
  new_max = 1

  mapped_value = ((value - old_min) * (new_max - new_min) / (old_max - old_min)) + new_min
  return mapped_value

def get_essentia_mean_features(df):
  col_names = df.columns.to_list()
  feature_mean_cols = [col for col in col_names if 'dmean' not in col and 'dmean2' not in col and 'dvar' not in col and 'dvar2' not in col and 'max' not in col and 'median' not in col and 'min' not in col and 'stdev' not in col and 'var' not in col and 'cov' not in col and 'icov' not in col]
  return df[feature_mean_cols]

def get_essentia_string_columns():
  return ['tonal.chords_key',
                  'tonal.chords_scale',
                  'tonal.key_edma.key',
                  'tonal.key_edma.scale',
                  'tonal.key_krumhansl.key',
                  'tonal.key_krumhansl.scale',
                  'tonal.key_temperley.key',
                  'tonal.key_temperley.scale'
                  ]

# Flatten the columns whose values are ndarrays, like tonal.chords_histogram
# Credits to https://stackoverflow.com/questions/45704999/how-to-convert-vector-wrapped-as-string-to-numpy-array-in-pandas-dataframe
def essentia_features_string_to_ndarray(str):
  return np.fromstring(str.replace('\n','')
                       .replace('[','')
                       .replace(']','')
                       .replace('  ',' '), 
                       sep=' '
                       )

def essentia_flatten_columns(df, col):
  print(col)
  result_dict = {}
  num_of_new_cols = max([len(i) for i in df[col]])
  # num_of_new_cols = len(df[col][0])
  num_of_rows = len(df[col])

  for i in range(num_of_new_cols):
    result_col_name = f'{col}_{i}'
    result_dict[result_col_name] = []

  for i in range(num_of_rows):
    for j in range(num_of_new_cols):
      result_col_name = f'{col}_{j}'

      # do padding
      if j >= len(df.iloc[i][col]):
        value = 0
      else:
        value = df.iloc[i][col][j]
      
      result_dict[result_col_name].append(value)

  return pd.DataFrame(result_dict)

# According to https://ieeexplore-ieee-org.library.sutd.edu.sg:2443/stamp/stamp.jsp?tp=&arnumber=8001129
def get_essentia_best_overall_features():
  return [
  'lowlevel.melbands_kurtosis.mean',
  'lowlevel.melbands_skewness.mean',
  'lowlevel.spectral_energy.mean',
  'rhythm.beats_loudness_band_ratio.mean',
  'tonal.chords_strength.mean',
  'tonal.hpcp_entropy.mean',
  'tonal.key_edma.strength', # assuming this refers to 'Key Strength (T)' in the research paper
  'tonal.key_temperley.strength', # assuming this refers to 'Key Strength (T)' in the research paper
  'tonal.chords_histogram'
]

# According to https://ieeexplore-ieee-org.library.sutd.edu.sg:2443/stamp/stamp.jsp?tp=&arnumber=8001129
def get_essentia_best_valence_features():
  return [
  # can't find any feature relating to 'High Frequency Content (L)
  'lowlevel.melbands_kurtosis.mean',
  'lowlevel.melbands_skewness.mean',
  'lowlevel.spectral_energy.mean',
  'lowlevel.zerocrossingrate.mean',
  'lowlevel.gfcc.mean',
  'lowlevel.mfcc.mean',
  'rhythm.beats_loudness.mean',
  'rhythm.onset_rate',
  'rhythm.beats_loudness_band_ratio.mean',
  'tonal.chords_strength.mean',
  'tonal.hpcp_entropy.mean',
  'tonal.key_edma.strength', # assuming this refers to 'Key Strength (T)' in the research paper
  'tonal.key_temperley.strength', # assuming this refers to 'Key Strength (T)' in the research paper
  'tonal.chords_histogram'
]

# According to https://ieeexplore-ieee-org.library.sutd.edu.sg:2443/stamp/stamp.jsp?tp=&arnumber=8001129
def get_essentia_best_arousal_features():
  return [
  'lowlevel.average_loudness',
  'lowlevel.barkbands_spread.mean',
  'lowlevel.melbands_crest.mean',
  'lowlevel.melbands_flatness_db.mean',
  'lowlevel.melbands_kurtosis.mean',
  'lowlevel.melbands_skewness.mean',
  'lowlevel.melbands_spread.mean',
  'lowlevel.spectral_energy.mean',
  'lowlevel.spectral_entropy.mean',
  'lowlevel.spectral_flux.mean',
  'lowlevel.spectral_kurtosis.mean',
  'lowlevel.spectral_rolloff.mean',
  'lowlevel.spectral_skewness.mean',
  'rhythm.bpm_histogram',
  'rhythm.danceability',
  'rhythm.onset_rate',
  'rhythm.beats_loudness_band_ratio.mean',
  'tonal.chords_strength.mean',
  'tonal.hpcp_entropy.mean',
  'tonal.key_edma.strength', # assuming this refers to 'Key Strength (T)' in the research paper
  'tonal.key_temperley.strength', # assuming this refers to 'Key Strength (T)' in the research paper
  'tonal.chords_histogram'
]

def integrate_feature_sets(df1, df2):
  df_integrated = pd.merge(df1, df2, on='song_id', how='inner')

  # Identify identical columns for dropping
  identical_cols = [col for col in df_integrated.columns if '_x' in col or '_y' in col]

  # Drop identical columns
  df_integrated.drop(columns=identical_cols, inplace=True)

  return df_integrated

def standardise_dataframe(df, song_ids):
  scaler = StandardScaler()

  # Fit and transform the selected columns
  df_standardised = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

  df_standardised = df_standardised.drop('song_id', axis=1)
  df_standardised.insert(0, column='song_id', value=song_ids)
  return df_standardised

def normalise_dataframe(df, song_ids):
  scaler = MinMaxScaler()

  # Fit and transform the selected columns
  df_standardised = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

  df_standardised = df_standardised.drop('song_id', axis=1)
  df_standardised.insert(0, column='song_id', value=song_ids)
  return df_standardised