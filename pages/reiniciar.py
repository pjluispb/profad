import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#st.sidebar_state['collapsed']

clave = st.session_state['clave']
st.write(clave)
volver = st.button('Volver')
if volver:
  switch_page('encuprof03')
