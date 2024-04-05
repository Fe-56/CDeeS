import pandas as pd

def get_columns(df):
  return df.columns.tolist()

def get_columns_no_song_id(df):
  temp = df.drop('song_id', axis=1)
  return temp.columns.tolist()