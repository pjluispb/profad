import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from deta import Deta
import pandas as pd
import time

st.set_page_config(
    page_title="ASIGLEH app",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",

)

deta = Deta(st.secrets["deta_key"])
encprof = deta.Base('asiglehpastores')

st.header('Encuesta Eclesiastica ASIGLEH 2023')
st.markdown("<h4 style='text-align: left; color: grey;'>Pastorado y Liderazgo</h4>", unsafe_allow_html=True)
st.subheader('Iglesia de Los Hermanos - Venezuela')

#st.write('Elaborado por APTA - Dtto Andino')

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
                st.session_state['clave'] = verifregDB.items[0]['key']
                st.session_state['rol'] = verifregDB.items[0]['rol']
                st.write(verifregDB.count)
                st.write(verifregDB.items)
                #st.stop()
                if st.session_state['rol']=='Pastor':
                    #switch_page('encupast02')
                    switch_page('encupast02mir')
                    #switch_page('encupast02edit')
                else:
                    switch_page('enculidAsigleh')
                
            else:
                st.error('''
                         Error en los datos ingresados.
                         Intente de nuevo''')