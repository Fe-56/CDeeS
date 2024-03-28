# according to https://ieeexplore-ieee-org.library.sutd.edu.sg:2443/stamp/stamp.jsp?tp=&arnumber=8001129

deam_essentia_arousal_features = [
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

deam_essentia_valence_features = [
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

deam_essentia_overall_features = [
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
