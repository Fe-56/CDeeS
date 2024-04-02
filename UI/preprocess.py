import pandas as pd
import numpy as np
from essentia_best_features import *
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def process_song(df_essentia_features):
    df_essentia_features = df_essentia_features[df_essentia_features.columns[1:]]
    df_essentia_features = get_mean_features(df_essentia_features)
    metadata_columns = [col for col in df_essentia_features.columns if 'metadata' in col]
    df_essentia_features = df_essentia_features.drop(columns=metadata_columns)
    df_essentia_features.select_dtypes(exclude=['int64', 'float64'])

    string_columns = ['tonal.chords_key',
                    'tonal.chords_scale',
                    'tonal.key_edma.key',
                    'tonal.key_edma.scale',
                    'tonal.key_krumhansl.key',
                    'tonal.key_krumhansl.scale',
                    'tonal.key_temperley.key',
                    'tonal.key_temperley.scale'
                    ]

    df_essentia_features_ndarray_columns = df_essentia_features.select_dtypes(exclude=['int64', 'float64'])
    ndarray_columns = df_essentia_features_ndarray_columns.columns.difference(string_columns)
    df_essentia_features_ndarray_columns = df_essentia_features_ndarray_columns[ndarray_columns]

    # df_essentia_features_ndarray_columns = df_essentia_features_ndarray_columns.applymap(string_to_ndarray)

    ndarray_columns = df_essentia_features_ndarray_columns.columns.to_list()
    df_ndarray_columns = []

    for column in ndarray_columns:
        df_ndarray_column = flatten_column(df_essentia_features_ndarray_columns, column)
        df_ndarray_columns.append(df_ndarray_column)


    df_essentia_features_ndarray_columns = pd.concat(df_ndarray_columns, axis=1)
    
    df_essentia_features_string_columns = df_essentia_features[string_columns]

    for col in df_essentia_features_string_columns.columns:
        df_essentia_features_string_columns[col] = df_essentia_features_string_columns[col].astype('category')
        df_essentia_features_string_columns[col] = df_essentia_features_string_columns[col].cat.codes

    df_essentia_features_numerical_columns = df_essentia_features.select_dtypes(include=['int64', 'float64'])

    df_temp = pd.concat([df_essentia_features_numerical_columns, df_essentia_features_ndarray_columns], axis=1)
    df_essentia_features_flattened = pd.concat([df_temp, df_essentia_features_string_columns], axis=1)


    # since our best model is trained on the Essentia Best Valence Normalised featureset
    valence_columns = [col for col in df_essentia_features_flattened.columns if any(substring in col for substring in deam_essentia_valence_features)]
    df_essentia_best_valence_features = df_essentia_features_flattened[valence_columns]
    
    # normalisation
    scaler = get_normalisation_scaler()

    df_essentia_best_valence_features_normalised = pd.DataFrame(scaler.transform(df_essentia_best_valence_features))

    return df_essentia_best_valence_features_normalised

# helper functions

def get_mean_features(df):
    col_names = df.columns.to_list()
    feature_mean_cols = [col for col in col_names if 'dmean' not in col and 'dmean2' not in col and 'dvar' not in col and 'dvar2' not in col and 'max' not in col and 'median' not in col and 'min' not in col and 'stdev' not in col and 'var' not in col and 'cov' not in col and 'icov' not in col]
    return df[feature_mean_cols]

def string_to_ndarray(str):
    return np.fromstring(str.replace('\n','')
                        .replace('[','')
                        .replace(']','')
                        .replace('  ',' '), 
                        sep=' '
                        )

def flatten_column(df, col):
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
            if j >= len(df[col][i]):
                value = 0
            else:
                value = df[col][i][j]
        
            result_dict[result_col_name].append(value)

    return pd.DataFrame(result_dict)

def get_normalisation_scaler():
    df_best_model_trained_features = pd.read_csv('./UI/essentia_best_valence_features.csv')
    
    # drop Unnamed:0 column
    df_best_model_trained_features = df_best_model_trained_features[df_best_model_trained_features.columns[1:]]

    df_best_model_trained_features = df_best_model_trained_features.drop('song_id', axis=1)
    scaler = MinMaxScaler()
    scaler.fit(df_best_model_trained_features)

    return scaler