


import streamlit as st
from streamlit_extras.switch_page_button import switch_page
# import extra_streamlit_components as stx
import cv2
import os
from PIL import Image, ImageDraw, ImageFont
from deta import Deta
import io
import random

deta = Deta(st.secrets.deta_key)
photos = deta.Drive(name='asiglehphotos')

def shootfoto(cond):
    if cond:
        st.write('tomafoto')
        st.stop()
        switch_page('surtphoto04b')
    return

st.subheader('Información Académica')
col1, col2= st.columns(2)
col1.info('Estudios de Secundaria en Liceos Tulio Febres Cordero en Colon estado Tachira (1er año, 1975) y Liceo Fray Juan Ramos de Lora en Mérida estado Mérida(2d0 a 5to año, entre 1976 y 1980)')
col2.success('Certificado : Diploma de Bachiller en Ciencias')
try:
    imagenDeta = photos.get('75362_ebiblicos_ima01_si00.png')
    content = imagenDeta.read()
    col2.image(content, width=300)
except:
    btn1 = col2.button('tomar foto del Certificado')
    if btn1:
        st.session_state['nameima'] = '75362_ebiblicos_ima01_si00.png'
        switch_page('surtphoto04b')
    st.write('***')
st.write('---')
col3,col4 = st.columns(2)
col3.success('Estudios Biblicos de Teologia en el Institutu Biblico Mizpa. Iglesia de Dios Pentecostal. Merida')
col4.info('Certificado de aprobacion')
try:
    imagenDeta = photos.get('E-78452_personales_ima02_si01.png')
    content = imagenDeta.read()
    col4.image(content, width=300)
except:
    btn1 = col3.button('tomar foto del Certificado')
    st.write('***')
st.write('---')
# st.write('st.session_state[nameima] = ', st.session_state['nameima'])
# btfot = st.button('Tomar Foto')
# if btfot:
#     switch_page('surtphoto04b')
# try:
#     imagenDeta = photos.get(st.session_state['nameima'])
#     content = imagenDeta.read()
#     st.image(content, width=300)
# except:
#     st.write('***')



