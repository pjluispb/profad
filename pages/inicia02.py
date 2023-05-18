import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from deta import Deta
from PIL import Image
import random
from google.oauth2 import service_account
import pygsheets

deta = Deta(st.secrets["deta_key"])
SCOPES = ('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive')
service_account_info = st.secrets.gcp_service_account
my_credentials = service_account.Credentials.from_service_account_info(service_account_info, scopes = SCOPES)
gc =pygsheets.authorize(custom_credentials=my_credentials)

sh = gc.open('DonesTest')
wks = sh.worksheet_by_title('preguntas')
df = pd.DataFrame(wks)
df = df.filter(items=[0,1])
#st.write(df)
dft = df.T
regdft = dft.to_dict('list')

with st.form('Datos Personales'):
    st.header('Test de Dones')
    evaluador = st.text_input('Introduce tu nombre completo')
    iglesia = st.text_input('Iglesia/Ministerio')
    rol = st.text_input('Rol/cargo/ministerio en la congregación')
    cedula = st.text_input('Introduce tu # cédula')
    aquien = evaluador
    relacion = 'Auto' 
    parentesco = 'A si mismo'
    lregdft = list(regdft.values())                                   # convierto el dict de preguntas en una lista
    random_lip = random.sample(lregdft,k=len(lregdft))                # lista random de preguntas

    st.session_state['datper'] = [evaluador,aquien,relacion,parentesco]
    st.session_state['datrpre'] = random_lip
    st.session_state['precon'] = [0]
    st.session_state['datperXdon'] = [[0,0]]
    st.session_state['dones'] = [['Administración',0], ['Milagros',0], ['Hospitalidad',0], ['Aconsejar',0], ['Conocimiento',0], ['Interpretación de lenguas',0], ['Comunicación Creativa',0], ['Profecía',0], ['Sabiduría',0], ['Apostolado',0], ['Habilidad en un oficio o arte',0], ['Lenguas',0], ['Exhortación',0], ['Ayudas',0], ['Misericordia',0], ['Dar',0], ['Fe',0], ['Sanidades',0], ['Evangelismo',0], ['Discernimiento',0], ['Liderazgo',0], ['Enseñanza',0], ['Pastor-maestro',0]]

    btn = st.form_submit_button('iniciar test')
    if btn:
        switch_page('preguntas02')
