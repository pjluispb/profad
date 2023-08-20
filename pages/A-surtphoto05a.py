

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import cv2
import os
from PIL import Image, ImageDraw, ImageFont
from deta import Deta
import io

deta = Deta(st.secrets.deta_key)

try:
    namefile = st.session_state['nameima']
    st.session_state['nameima']
except:
    st.error('error en el namefile')
clave = st.session_state['clave'] 
nombreu = st.session_state['nombreu']
cedulau = st.session_state['cedulau']

#clave, nombreu, cedulau
#namefile
# st.stop()
picture = st.camera_input("Toma la foto")
st.write(namefile)
if picture:
    # st.image(picture)
    bytes_data = picture.getvalue()
    photos = deta.Drive(name='asiglehphotos')
    photos.put(namefile, io.BytesIO(bytes_data))
    st.session_state['fotoTomada']=True
    st.session_state['clave'] = clave
    st.session_state['nombreu'] = nombreu
    st.session_state['cedulau'] = cedulau   
    switch_page('A-encupast04edit')