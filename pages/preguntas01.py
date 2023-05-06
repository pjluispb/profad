import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from deta import Deta
import random
import time

import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

deta = Deta(st.secrets["deta_key"])

datper = st.session_state['datper']
datrpre = st.session_state['datrpre']
precon = st.session_state['precon']
datperXdon = st.session_state['datperXdon']
dones = st.session_state['dones']

lottie_url_processing = 'https://assets8.lottiefiles.com/packages/lf20_tmnc73b6.json'
lottie_processing = load_lottieurl(lottie_url_processing)

st_lottie(lottie_processing, key='processing')
#st.write(datper)
# st.write(len(datrpre))
#st.write(precon)
#st.write(datperXdon)
st.latex('Evaluador: '+datper[0])
st.latex('Evaluado: '+datper[1])
st.latex('Relación: '+datper[2])
st.latex('Parentesco: '+datper[3])
if (len(datrpre))>0:
    with st.empty():
        for seconds in range(1):
            st.write(f"⏳ {seconds} seconds have passed")
            time.sleep(1)
        st.write("✔️ 1 seconds over!")
        
        st.session_state['selpre'] = random.choice(datrpre)
        switch_page('espera1')
else:
    regDones = {
	"Aconsejar": [bus[1] for bus in datperXdon if bus[0]=='Aconsejar'][0],
	"Administración": [bus[1] for bus in datperXdon if bus[0]=='Administración'][0],
	"Apostolado": [bus[1] for bus in datperXdon if bus[0]=='Apostolado'][0],
	"Ayudas": [bus[1] for bus in datperXdon if bus[0]=='Ayudas'][0],
	"Comunicación Creativa": [bus[1] for bus in datperXdon if bus[0]=='Comunicación Creativa'][0],
	"Conocimiento": [bus[1] for bus in datperXdon if bus[0]=='Conocimiento'][0],
	"Dar": [bus[1] for bus in datperXdon if bus[0]=='Dar'][0],
	"Discernimiento": [bus[1] for bus in datperXdon if bus[0]=='Discernimiento'][0],
	"Enseñanza": [bus[1] for bus in datperXdon if bus[0]=='Enseñanza'][0],
	"Evangelismo": [bus[1] for bus in datperXdon if bus[0]=='Evangelismo'][0],
	"Exhortación": [bus[1] for bus in datperXdon if bus[0]=='Exhortación'][0],
	"Fe": [bus[1] for bus in datperXdon if bus[0]=='Fe'][0],
	"Habilidad en un oficio o arte": [bus[1] for bus in datperXdon if bus[0]=='Habilidad en un oficio o arte'][0],
	"Hospitalidad": [bus[1] for bus in datperXdon if bus[0]=='Hospitalidad'][0],
	"Interpretación de lenguas": [bus[1] for bus in datperXdon if bus[0]=='Interpretación de lenguas'][0],
	"Lenguas": [bus[1] for bus in datperXdon if bus[0]=='Lenguas'][0],
	"Liderazgo": [bus[1] for bus in datperXdon if bus[0]=='Liderazgo'][0],
	"Milagros": [bus[1] for bus in datperXdon if bus[0]=='Milagros'][0],
	"Misericordia": [bus[1] for bus in datperXdon if bus[0]=='Misericordia'][0],
	"Pastor-maestro": [bus[1] for bus in datperXdon if bus[0]=='Pastor-maestro'][0],
	"Profecía": [bus[1] for bus in datperXdon if bus[0]=='Profecía'][0],
	"Sabiduría": [bus[1] for bus in datperXdon if bus[0]=='Sabiduría'][0],
	"Sanidades": [bus[1] for bus in datperXdon if bus[0]=='Sanidades'][0],
	"evaluado": datper[0],
	"evaluador": datper[1],
	"fechayhora": "-",
	"parentesco": datper[3],
	"relacion": datper[2],
    }
    donesDB = deta.Base('dones')
    donesDB.put(regDones)
    switch_page('salidapre')

