import sys
sys.path.insert(1, './research/utils')
from paths import *

def write_audio_file(st, uploaded_file):
    uploaded_audio_path = None

    if uploaded_file:
        st.audio(uploaded_file, format='audio/mp3')

        uploaded_audio_path = f'{UPLOADED_AUDIO_PATH}/{uploaded_file.name}'

        with open(uploaded_audio_path, "wb") as f:
            f.write(uploaded_file.getvalue())

    return uploaded_audio_path