
import streamlit as st
import streamlit_survey as ss
from streamlit_echarts import st_echarts
from streamlit_extras.switch_page_button import switch_page


Nombre = st.session_state['Nombres']
preguntas = st.session_state['Preguntas']

def cierre():
    #ph.survey.data.items()
    st.session_state['SurveyDataItems'] = ph.survey.data.items()
    totales = {'Colérico':0, 'Melancólico':0, 'Sanguíneo':0, 'Flemático':0}

    # json = ph.survey.to_json()
    # st.json(json)
    # col1, col2 = st.columns(2)
    # with col1:
    for clave, valor in ph.survey.data.items():
        # st.write(valor)
        for c,v in preguntas.items():
            if v[0]==valor['label']:
                if v[1]==valor['value']:tempera=v[2]
                elif v[3]==valor['value']:tempera=v[4]
                elif v[5]==valor['value']:tempera=v[6]
                else:tempera=v[8]
                # st.write(tempera)
                for key, value in totales.items():
                    if key==tempera:
                        totales[key]+=1
    st.write(totales)
    st.session_state['totales']=totales
    switch_page('survey20c')
                
    # with col2:
    #     preguntas

    st.session_state['page'] = 1
    for i in range(2, 22):
        st.session_state[f'id{i}'] = 0
    st.stop()

# Restablecer la página actual a 1 y los valores de los sliders a 0
if 'page' not in st.session_state:
    st.session_state['page'] = 1
    for i in range(2, 22):
        st.session_state[f'id{i}'] = 0

# Obtener la página actual del estado de la sesión
current_page = st.session_state['page']

st.info('Información : '+ Nombre)
phcierre = st.container()
ph = st.container()

# Crear la encuesta con la página actual y la función de cierre
totales = {'colerico':0, 'melancolico':0, 'flematico':0, 'sanguineo':0}
ph.survey = ss.StreamlitSurvey()

with ph.survey.pages(20, on_submit=cierre) as page:
    st.header(preguntas[page.current][0])
    seleccion = ph.survey.radio(id=f'id{page.current+2}', label = preguntas[page.current][0], options=[preguntas[page.current][1], preguntas[page.current][3], preguntas[page.current][5], preguntas[page.current][7]])



    # ph.survey.slider(id=f'id{page.current+2}', label = preguntas[page.current][0], label_visibility="hidden" )

# Actualizar la página actual en el estado de la sesión
st.session_state['page'] = current_page