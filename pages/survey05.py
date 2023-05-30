
import streamlit as st
import streamlit_survey as ss
from streamlit_card import card


imagenes = [
    "https://i.postimg.cc/tnxbPkD6/mento04.png",
    "https://i.postimg.cc/t7Kpy0CN/mento02.png",
    "https://i.postimg.cc/6yCwpH8J/mento03.png",
    "https://i.postimg.cc/tnxbPkD6/mento04.png",
    "https://i.postimg.cc/6yCwpH8J/mento03.png",
    "https://i.postimg.cc/tnxbPkD6/mento04.png"]

preguntas = [
    ("Me gusta aprender administración y como funcionan las organizaciones.",'Categoria-1'),
    ("Cuando alguien tiene una lucha espiritual o social, le cuido de tal manera que con tiempo puede resolver su problema prácticamente.",'Categoria-2'),
    ("Cuando pienso en un acontecimiento, puedo visualizarlo y resolver posibles [problemas antes de que ocurran.",'Categoria-1'),
    ("Me gusta que los que me rodean sepan que soy creyente, con la esperanza de que me preguntaran sobre mi relación con Cristo.",'Categoria-2'),
    ("Soy un buen administrador de dinero de manera que puedo apoyar económicamente los ministerios que promocionan la causa de Cristo.",'Categoria-3'),
    ("Tengo tanta paz en cuanto al cuidado y provisión de Dios para mi y para otros que los creyentes han comentado sobre mi fe y confianza.",'Categoria-1'),
    ("Disfruto proveyendo comida y alojamiento a los necesitados.",'Categoria-3')]

def cierre():
    phcierre.write('Cierre de survey')
    phcierre.write(ph.survey.data)
    phcierre.write(ph.survey.data_name)
    

st.info('Información ')
phcierre = st.container()
ph = st.container()

ph.survey = ss.StreamlitSurvey()
with ph.survey.pages(5, on_submit=cierre) as page:
    st.header(preguntas[page.current][0])
    #card(image=imagenes[page.current], text = '-*-', title=preguntas[page.current][0])
    #card(text = '-*-', title=preguntas[page.current][0])
    ph.survey.slider(id = 'id'+str(page.current+2), label = preguntas[page.current][1])
   
    #ph.survey.text_input(preguntas[page.current][1])

