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
encasigleh = deta.Base('asiglehpastores')

st.header('Encuesta del Pastorado ASIGLEH 2023')
st.subheader('Iglesia de Los Hermanos - Venezuela')


# st.markdown('Bienvenido al Sistema etc etc')

st.markdown("<h1 style='text-align: center; color: grey;'>Registro Inicial</h1>", unsafe_allow_html=True)
ph1 = st.empty()
col1, col2 = ph1.columns(2)
with ph1:
    col1.markdown("<h6 style='text-align: center; color: red;'>Ingresa el código de invitación: </h6>", unsafe_allow_html=True)
    with col2:
        vercodinv = st.text_input('Ingrese el código de invitación', label_visibility='collapsed')
vercodinv_out=vercodinv
if vercodinv_out=='123':
    ph1.empty()
    with st.form('fregini'):
        nombreu = st.text_input('Ingrese un nombre de usuario')
        cedulau = st.text_input('Ingrese su número de cédula')
        pastorOlider = st.radio(label='Se registra como Pastor, ó Pastor Asociado, ó como Líder en su congregación ó iglesia?', options=['Pastor', 'Pastor Asociado ó co-Pastor', 'Líder'])
        streg, nom, ced = True, nombreu, cedulau
        ingresaReg = st.form_submit_button('Enviar')
        if ingresaReg:
            verifregDB = encasigleh.fetch({"nombreu":nombreu, "cedulau":cedulau})
            if verifregDB.count==0:
                encasigleh.put({"nombreu":nombreu, "cedulau":cedulau, "key":'asigleh-'+cedulau+'-'+nombreu, "rol":pastorOlider})
                progress_text = "Registrando datos en DB."
                my_bar = st.progress(0, text=progress_text)
                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                switch_page('login01asigleh')
            else:
                st.error('''
                         Datos ya registrados. 

                         NO es posible registrar otro similar.

                         Intente de nuevo''')