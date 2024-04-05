import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def make_scaler(type, df, scaler_file_path):
  scaler = get_scaler(type)

  if ('song_id' in df.columns.tolist()):
    temp = df.drop('song_id', axis=1)
  else:
    temp = df

  scaler.fit(temp)

  # save model to disk
  joblib.dump(scaler, scaler_file_path)

def get_scaler(type):
  if (type == 'standardisation'):
    return StandardScaler()
  elif (type == 'normalisation'):
    return MinMaxScaler()
  else:
    return MinMaxScaler()