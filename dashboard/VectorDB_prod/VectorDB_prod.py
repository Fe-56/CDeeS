import chromadb

def get_chromadb_collection():
  client = chromadb.PersistentClient(path='./research/VectorDB_test/')
  collection = client.get_collection(name="DEAM_PMEmo_dataset")
  return collection

def get_recommendations(valence, arousal, num_of_recommendations, collection):
  res = collection.query(
    query_embeddings=[[valence, arousal]],
    n_results=num_of_recommendations,
    include=["distances", "metadatas", "embeddings", "documents"]
  )

  metadatas = []
  audio_paths = []
  va_values = []

  for metadata in res["metadatas"][0]:
    metadatas.append(metadata)

  for audio_path in res["documents"][0]:
    audio_path = audio_path[4:] # to account for the relative file path
    audio_paths.append(audio_path)

  for va_value in res["embeddings"][0]:
    va_values.append(va_value)

  return metadatas, audio_paths, va_values