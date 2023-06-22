import streamlit as st
from deta import Deta
import io

deta = Deta(st.secrets.deta_key)

img_file_buffer = st.camera_input("Toma una foto")

if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    photos = deta.Drive(name='phot01')
    photos.put('ima12.jpg', io.BytesIO(bytes_data))
