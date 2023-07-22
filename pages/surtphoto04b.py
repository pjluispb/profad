

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import cv2
import os
from PIL import Image, ImageDraw, ImageFont
from deta import Deta
import io

deta = Deta(st.secrets.deta_key)

namefile = st.session_state['nameima']

picture = st.camera_input("Toma la foto")
st.write(namefile)
if picture:
    # st.image(picture)
    bytes_data = picture.getvalue()
    photos = deta.Drive(name='asiglehphotos')
    photos.put(namefile, io.BytesIO(bytes_data))
    st.session_state['fotoTomada']=True
    switch_page('encupast02mir')