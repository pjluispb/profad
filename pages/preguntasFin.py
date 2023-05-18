import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from deta import Deta
from PIL import Image
import re
from datetime import datetime
import random
from streamlit_echarts import st_echarts
from google.oauth2 import service_account
import pygsheets
from pathlib import Path

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
try:
    lottie_processing = load_lottieurl(lottie_url_processing)
except:
    st.write('---')

#st_lottie(lottie_processing, key='processing')
#st.write(datper)
# st.write(len(datrpre))
#st.write(precon)
#st.write(datperXdon)
#st.latex('Evaluado: '+datper[1]+' <---> Evaluador: '+datper[0])
#st.latex('Relación: '+datper[2]+' <---> Parentesco: '+datper[3])
#st.latex()
st.header('Test de Dones - Autoevaluación')
col1, col2 = st.columns(2)
col1.info(datper[1])
col2.info(datper[3])

donesDB = deta.Base('dones')
donesDBf = donesDB.fetch()
dfdones = pd.DataFrame(donesDBf.items)
evaluados = dfdones['evaluado'].tolist()

#st.write('----')

dfbus = dfdones.loc[dfdones['evaluado']==datper[1]]
st.write(dfbus)
#st.write(dfdones)
dfper = dfbus[['evaluado','evaluador','fechayhora','key','parentesco','relacion']]
dfdones = dfdones.drop(['evaluado','evaluador','fechayhora','key','parentesco','relacion'],axis=1)
data = dfdones.columns.to_list()
#st.write(dfper)
#st.write(data)
st.write(dfdones)

tval1 = dfbus.loc[0].values.flatten().tolist()
tval = [tval1,[],[]]
options01 = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {
        "data": ["Direct", "Mail Ad", "Affiliate Ad"]
    },
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {"type": "value"},
    "yAxis": {
        "type": "category",
        "data": ['Administración', 'Milagros', 'Hospitalidad', 'Aconsejar', 'Conocimiento', 'Interpretación de lenguas', 'Comunicación Creativa', 'Profecía', 'Sabiduría', 'Apostolado', 'Habilidad en un oficio o arte', 'Lenguas', 'Exhortación', 'Ayudas', 'Misericordia', 'Dar', 'Fe', 'Sanidades', 'Evangelismo', 'Discernimiento', 'Liderazgo', 'Enseñanza', 'Pastor-maestro'],
    },
    "series": [
        {
            "name": "a si mismo",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": tval[0],
            #"data": [320, 302, 301, 334, 390, 330, 320],
        },
        {
            "name": "cercano",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": tval[1],
            #"data": [120, 132, 101, 134, 90, 230, 210],
        },
        {
            "name": "lejano",
            "type": "bar",
            "stack": "total",
            "label": {"show": True},
            "emphasis": {"focus": "series"},
            "data": tval[2],
            #"data": [220, 182, 191, 234, 290, 330, 310],
        },
        
    ],
}
st_echarts(options=options01, height="500px")
option02 = {
    "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
    "legend": {
        "data": ["Direct", "Mail Ad", "Affiliate Ad"]
    },
    'angleAxis': {
        'type': 'category',
        'data': ['Administración', 'Milagros', 'Hospitalidad', 'Aconsejar', 'Conocimiento', 'Interpretación de lenguas', 'Comunicación Creativa', 'Profecía', 'Sabiduría', 'Apostolado', 'Habilidad en un oficio o arte', 'Lenguas', 'Exhortación', 'Ayudas', 'Misericordia', 'Dar', 'Fe', 'Sanidades', 'Evangelismo', 'Discernimiento', 'Liderazgo', 'Enseñanza', 'Pastor-maestro']
    },
    'radiusAxis': {},
    'polar': {},
    'series': [
        { 'type': 'bar',
            'data':tval[0],
        #'data': [1, 2, 3, 4, 3, 5, 1, 2, 4, 6, 1, 3, 2, 1, 1, 2, 3, 4, 1, 2, 5, 4, 6, 7],
        'coordinateSystem': 'polar',
        'stack': 'a',
        'emphasis': { 'focus': 'series' }     },
        { 'type': 'bar',
        #'data': [2, 4, 6, 1, 3, 2, 1, 1, 2, 3, 4, 1, 2, 5,1, 2, 3, 4, 3, 5,2, 4, 6, 1, 3],
        'data':tval[1],
        'coordinateSystem': 'polar',
        'stack': 'a',
        'emphasis': {  'focus': 'series'   }   },
        { 'type': 'bar',
            'data':tval[2],
        #'data': [1, 2, 3, 4, 1, 2, 5, 3, 4, 1, 2, 5,1,0, 0, 0, 5,2, 4, 6, 5, 3, 4,1],
        'coordinateSystem': 'polar',
        'stack': 'a',
        'emphasis': { 'focus': 'series'    }  }
        ],
    'legend': {'show': 'true', 'data': ['A', 'B', 'C'] }
    }
#st.write('---')
st_echarts(options=option02, height="500px")
