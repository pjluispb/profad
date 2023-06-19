
import pandas as pd
import streamlit as st
# import streamlit_survey as ss
# from streamlit_echarts import st_echarts

from deta import Deta
from google.oauth2 import service_account
import pygsheets

from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Mentoria ASIGLEH App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

deta = Deta(st.secrets["deta_key"])
SCOPES = ('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive')
service_account_info = st.secrets.gcp_service_account
my_credentials = service_account.Credentials.from_service_account_info(service_account_info, scopes = SCOPES)
gc =pygsheets.authorize(custom_credentials=my_credentials)

sh = gc.open('testeo')
wks = sh.worksheet_by_title('preguntas')
df = pd.DataFrame(wks)
df = df.filter(items=[0,1,2,3,4,5,6,7,8])
#df
dft = df.T
df_rand = df.sample(frac=1).reset_index(drop=True)
df_rand_t = df_rand.T
questions = df_rand_t.to_dict('list')
#st.write(questions)

st.session_state['Preguntas'] = questions

st.info('Información ')
Nombre = st.text_input('Nombre = ')

st.session_state['Nombres'] = Nombre

bseguir = st.button('seguir')
if bseguir:
    st.session_state['tempera'] = '0'
    switch_page('survey20b')
