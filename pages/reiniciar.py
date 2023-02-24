import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from deta import Deta
import pandas as pd

deta = Deta(st.secrets["deta_key"])

clave = st.session_state['clave']
st.write(clave)

usuarios = deta.Base('usuarios')
rec1=usuarios.get(clave)

st.write(rec1)

volver = st.button('Volver')
if volver:
  switch_page('encuprof03')
