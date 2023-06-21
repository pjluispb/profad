
import streamlit as st
from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (2000, 1414), color='orange')
d = ImageDraw.Draw(img)

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

    st.write(picture)
    picture.write('c:/users/user/Desktop/python/minec/Certificados/ima01')
    #fotoname = picture.write
    #st.write(fotoname)
    #img.save('c:/users/user/Desktop/python/minec/Certificados/'+fotoname) # guarda la imagen local
            