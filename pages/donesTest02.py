
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

deta = Deta(st.secrets["deta_key"])
SCOPES = ('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive')
service_account_info = st.secrets.gcp_service_account
my_credentials = service_account.Credentials.from_service_account_info(service_account_info, scopes = SCOPES)
gc =pygsheets.authorize(custom_credentials=my_credentials)

sh = gc.open('DonesTest')
wks = sh.worksheet_by_title('preguntas')
df = pd.DataFrame(wks)
df.drop(index=2,)
st.write(df)
regdf = df.to_dict()
#st.write(regdf)
evalus = [['Pedro','Maria'],['Jose', 'Sonia'],['Jaime','Carmen'],['Carlos','Sobeida'],['Emilio','Graciela'],['Ensi','Marce'],['Victor','Flor'],['Gilbert','Rosa']]
evalus2 = [[x[1],x[0]] for x in evalus]
evalus3 = evalus+evalus2
#print(evalus3)
#st.write(evalus3)
# for t in evalus3:
#     print(t)
pers1 = [x[0] for x in evalus3]
pers2 = [x[1] for x in evalus3]
pers3 = pers1+pers2
spers3  = set(pers3)
lpers3 = list(spers3)
trip = []
for t in evalus3:
    nott = [x for x in lpers3 if x not in t]
    third = random.choice(nott)
    etri = [t[0], t[1], third]
    trip.append(etri)
for t in trip:
    #print('\n','-----------','\n',t)
    #print('regdf = ',regdf)
    # Número 1 = no mucho o nada; Número 2 = un poquito; Número 3 = algo; Número 4 = mucho
    st.write(t[0])
    tval=[]
    for elem in t:
        #print('==>',elem,'<==')
        #st.write('==>',elem,'<==')
        lidonpre, dones = [], []
        for reg in regdf:
            donb = reg[0]
            pregunta = reg[1]
            #print(donb,'< - >',pregunta)
            lidonpre.append((donb,pregunta))
            dones.append(donb)
        #st.write('dones = ', dones)
        random_lip = random.sample(lidonpre,k=len(lidonpre))
        #print(random_lip)
        solodones = set(dones)
        #print(len(solodones),solodones)
        #st.write(len(solodones),solodones)
        lres = []
        for t in random_lip:
            don = t[0]
            preg = t[1]
            sel = random.randint(1,4)*5
            tup=[don,preg,sel]
            lres.append(tup)
        # for dpre in lres:
        #     print(dpre)
        # print('Dones = ', solodones)
        resuldon, resultados = [], []
        for donesp in solodones:
            resXdon = [r[2] for r in lres if r[0]==donesp]
            suma=0
            for num in resXdon:
                suma+=num
            #print(donesp,resXdon,'=',suma)
            #print(donesp, suma)
            resuldon.append((donesp,suma))
            resultados.append(suma)
        #print(resuldon)
        #st.write(resultados)
        tval.append(resultados)
    #st.write(tval)
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
            'name': 'A',
            'stack': 'a',
            'emphasis': { 'focus': 'series' }     },
            { 'type': 'bar',
            #'data': [2, 4, 6, 1, 3, 2, 1, 1, 2, 3, 4, 1, 2, 5,1, 2, 3, 4, 3, 5,2, 4, 6, 1, 3],
            'data':tval[1],
            'coordinateSystem': 'polar',
            'name': 'B',
            'stack': 'a',
            'emphasis': {  'focus': 'series'   }   },
            { 'type': 'bar',
             'data':tval[2],
            #'data': [1, 2, 3, 4, 1, 2, 5, 3, 4, 1, 2, 5,1,0, 0, 0, 5,2, 4, 6, 5, 3, 4,1],
            'coordinateSystem': 'polar',
            'name': 'C',
            'stack': 'a',
            'emphasis': { 'focus': 'series'    }  }
            ],
        'legend': {'show': 'true', 'data': ['A', 'B', 'C'] }
        }
    st.write('---')
    st_echarts(options=option02, height="500px")
