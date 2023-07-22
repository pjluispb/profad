import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from deta import Deta
import pandas as pd
import time

st.set_page_config(
    page_title="Profesionales AD Reg App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",

)

deta = Deta(st.secrets["deta_key"])
encprof = deta.Base('liderapta')

st.header('Encuesta de Liderazgo Eclesial de las Asambleas de Dios 2023')
st.subheader('Distrito Andino - Zona 1')
st.write('Elaborado por APTA - Dtto Andino')

#st.markdown('Bienvenido al Sistema etc etc')

st.markdown("<h1 style='text-align: center; color: grey;'>Login</h1>", unsafe_allow_html=True)
col1,col2,col3 = st.columns(3)
with col2:
    with st.form('fregini'):
        st.markdown("<h3 style='text-align: center; color: red;'>Usuario </h2>", unsafe_allow_html=True)
        nombreu = st.text_input(label='nombreu', label_visibility='collapsed')
        st.markdown("<h3 style='text-align: center; color: red;'>Cédula </h2>", unsafe_allow_html=True)
        cedulau = st.text_input(label='cedulau', label_visibility='collapsed')
        streg, nom, ced = True, nombreu, cedulau
        ingresaReg = st.form_submit_button('Enviar')
        if ingresaReg:
            verifregDB = encprof.fetch({"nombreu":nombreu, "cedulau":cedulau})
            if verifregDB.count==1:
                st.session_state['nombreu'] = nombreu
                st.session_state['cedulau'] = cedulau
                st.write(verifregDB.count)
                st.write(verifregDB.items)
                #switch_page('encuprof08')
                switch_page('encupast01')
            else:
                st.error('''
                         Error en los datos ingresados.
                         Intente de nuevo''')