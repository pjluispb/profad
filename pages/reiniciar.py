import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from deta import Deta
import pandas as pd
pd.set_option('display.max_colwidth', None)

deta = Deta(st.secrets["deta_key"])

clave = st.session_state['clave']
#st.write(clave)

usuarios = deta.Base('usuarios')
rec1=usuarios.get(clave)
st.info('''Felicitaciones, los datos han sido grabados en la base de datos. 
Aqui los puedes ver :thumb up: ''')
#st.write(rec1)
sdf = pd.Series(rec1)
sdf

volver = st.button('Volver')
if volver:
  switch_page('encuprof03')
