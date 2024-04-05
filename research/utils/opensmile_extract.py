import opensmile
from paths import *

smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.ComParE_2016,
    feature_level=opensmile.FeatureLevel.Functionals,
)

def extract_gemaps(song_id):
  smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.GeMAPS,
    feature_level=opensmile.FeatureLevel.Functionals,
  )
  print(f'Extracting features from song_id: {song_id}')
  # df_opensmile_temp = smile.process_file(f'{}')
  return df_opensmile_temp