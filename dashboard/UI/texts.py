def title(st):
  return markdown(st, 
    """<h1> 
      CDeeS: Anthony, Fuo En, Issac, Jia Jun, Timothy
    </h1>"""
  )

def subtitle(st):
  return markdown(st, 
    """<h4>
      🎸 Get personalised music recommendations based on music emotions! 🎵
    </h4>"""
  )

def choose_audio_file(st):
  return markdown(st, 
    """<h2>
      🎶 Choose an audio file!
    </h2>"""
  )

def how_many_recommended(st):
  return markdown(st, 
    """<h2>
      👍 How many songs do you want to be recommended with?
    </h2>"""
  )

def your_music_va(st, valence, arousal):
  markdown(st,
    """<h2>
      Your uploaded audio's emotions:
    </h2>"""
  )

  valence_col, arousal_col = st.columns(2)
  with valence_col:
    markdown(st, 
      f"""<h3>
        <u>Valence</u>
      </h3>"""
    )
    markdown(st,
      f"""<h3>
        {valence} {valence_emoji(valence)}
      </h3>"""
    )
  with arousal_col:
    markdown(st, 
      f"""<h3>
        <u>Arousal</u>
      </h3>"""
    )
    markdown(st,
      f"""<h3>
        {arousal} {arousal_emoji(arousal)}
      </h3>"""
    )

def recommended_songs(st):
  markdown(st,
    """<h2>
      🎼 Here are your song recommendations:
    </h2>"""
  )

def recommended_song(st, index, title, artist, audio_path):
  markdown(st,
    f"""<h3>
      Song {num_emoji(index)}
    </h3>"""
  )

  title_col, artist_col = st.columns(2)
  with title_col:
    markdown(st,
      f"""<h3>
        🎵 <u>Title</u>
      </h3>"""
    )
    markdown(st,
      f"""<h4>
        {title}
      </h4>"""
    )
  with artist_col:
    markdown(st,
      f"""<h3>
        👨‍🎤👩‍🎤 <u>Artist</u>
      </h3>"""
    )
    markdown(st,
      f"""<h4>
        {artist}
      </h4>"""
    )

  st.audio(audio_path, format='audio/mp3')

def valence_emoji(valence):
  if valence > 0.0:
    return "😄"
  else:
    return "😞"
  
def arousal_emoji(arousal):
  if arousal > 0.0:
    return "😝"
  else:
    return "😴"
  
def num_emoji(num):
  match num:
    case 1:
      return "1️⃣"
    case 2:
      return "2️⃣"
    case 3:
      return "3️⃣"
    case 4:
      return "4️⃣"
    case 5:
      return "5️⃣"
    case 6:
      return "6️⃣"
    case 7:
      return "7️⃣"
    case 8:
      return "8️⃣"
    case 9:
      return "9️⃣"
    case 10:
      return "1️⃣0️⃣"

def markdown(st, text):
  return st.markdown(
    text,
    unsafe_allow_html=True
  )