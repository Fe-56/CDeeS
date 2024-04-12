from feature_extraction import extract_features
from preprocess import process_song
from prediction import predict
from visualisations import plot_va_graph
from texts import *

import sys
sys.path.insert(1, './dashboard/VectorDB_prod')
from VectorDB_prod import *

def recommend_button(st, best_model, uploaded_audio_path, num_recommendations):
  if st.button("👍 Recommend me songs!"):
      st.divider()

      # MER phase
      features = extract_features(uploaded_audio_path, best_model)
      processed_features = process_song(features, best_model)
      valence, arousal = predict(processed_features, best_model)

      rounded_valence = round(valence.item(), 4)
      rounded_arousal = round(arousal.item(), 4)
      your_music_va(st, rounded_valence, rounded_arousal)
      st.divider()

      # personalised music recommendation phase
      collection = get_chromadb_collection()
      recommended_metadatas, recommended_audio_paths, recommended_va_values = get_recommendations(rounded_valence, rounded_arousal, num_recommendations, collection)
      recommended_songs(st)
      recommendations_va = []

      for i in range(num_recommendations):
          artist = recommended_metadatas[i]['artist']
          title = recommended_metadatas[i]['title']
          audio_path = recommended_audio_paths[i]
          recommended_valence = round(recommended_va_values[i][0], 4)
          recommended_arousal = round(recommended_va_values[i][1], 4)
          recommendations_va.append((recommended_valence, recommended_arousal))
          
          recommended_song(st, i+1, title, artist, audio_path)

      st.divider()
      st.pyplot(plot_va_graph(valence, arousal, recommendations_va))
