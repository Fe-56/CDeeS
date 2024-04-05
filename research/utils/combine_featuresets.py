from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

def standarise(df):
  scaler = StandardScaler()
  song_ids = df['song_id'].tolist()
  df = df.drop('song_id', axis=1)

  # Fit and transform the selected columns
  df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

  df.insert(0, column='song_id', value=song_ids)
  return df

def normalise(df):
  scaler = MinMaxScaler()
  song_ids = df['song_id'].tolist()
  df = df.drop('song_id', axis=1)

  # Fit and transform the selected columns
  df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

  df.insert(0, column='song_id', value=song_ids)
  return df

# The combine_featuresets() function will also perform standardisation and normalisation and export both dataframes
def combine_featuresets(deam_df_path, pmemo_df_path, output_path, standardised_output_path, normalised_output_path):
    df_deam = pd.read_csv(deam_df_path)
    df_pmemo = pd.read_csv(pmemo_df_path)

    # modify song_id column values
    df_deam['song_id'] = df_deam['song_id'].apply(lambda x: f'deam_{x}')
    df_pmemo['song_id'] = df_pmemo['song_id'].apply(lambda x: f'pmemo_{x}')

    # combine the two datasets
    df_combined = pd.concat([df_deam, df_pmemo])
    df_combined.to_csv(output_path, index=False)

    # # standardisation and normalisation
    df_combined_standardised = standarise(df_combined)
    df_combined_normalised = normalise(df_combined)

    # # exporting dataframes to .csv
    df_combined_standardised.to_csv(standardised_output_path, index=False)
    df_combined_normalised.to_csv(normalised_output_path, index=False)
    return df_combined_standardised, df_combined_normalised