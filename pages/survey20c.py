
import streamlit as st
import streamlit_survey as ss
from streamlit_echarts import st_echarts
from streamlit_extras.switch_page_button import switch_page
Nombre = st.session_state['Nombres']
preguntas = st.session_state['Preguntas']
totales = st.session_state['totales']

#st.write(totales)
option = {
    "legend": {"top": "bottom"},
    "toolbox": {
        "show": False,
        "feature": {
            "mark": {"show": True},
            "dataView": {"show": True, "readOnly": False},
            "restore": {"show": False},
            "saveAsImage": {"show": False},
        },
    },
    "series": [
        {
            "name": "Temperamento "+Nombre,
            "type": "pie",
            "radius": [80, 200],
            "center": ["50%", "50%"],
            "roseType": "area",
            "itemStyle": {"borderRadius": 8},
            "data": [
                {"value": totales['Colérico'], "name": "Colérico"},
                {"value": totales['Flemático'], "name": "Flemático"},
                {"value": totales['Melancólico'], "name": "Melancólico"},
                {"value": totales['Sanguíneo'], "name": "Sanguíneo"},
            ],
        }
    ],
}

st.write(Nombre)
st.write(totales)
#st.write(preguntas)
st_echarts(
    options=option, height="500px",
)

bseguir = st.button('ir al inicio')
if bseguir:
    st.session_state['tempera'] = '0'
    switch_page('survey20a')
    
