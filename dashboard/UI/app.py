import streamlit as st
from write_audio_file import write_audio_file
from recommend_button import recommend_button
from texts import *

import sys
sys.path.insert(1, './research/utils')
from paths import *

sys.path.insert(1, './dashboard/VectorDB_prod')
from VectorDB_prod import *

# write the name of the best model here!
best_model = 'opensmile_gemaps_normalised'

num_recommendations = 5

st.set_page_config(page_title='CDeeS Music Recommendation from Emotions')
title(st)
subtitle(st)
st.divider()
choose_audio_file(st)
uploaded_audio = st.file_uploader('', type=['mp3', 'wav'])
uploaded_audio_path = write_audio_file(st, uploaded_audio)
st.divider()

# if an audio file has been uploaded, show the recommend button
if uploaded_audio_path:
    how_many_recommended(st)
    num_recommendations = st.slider(
        key="num_recommendations_slider",
        label='',
        min_value=1, 
        max_value=10,
        value=num_recommendations
    )
    recommend_button(st, best_model, uploaded_audio_path, num_recommendations)