import streamlit as st
import time
from streamlit_extras.switch_page_button import switch_page
import random

datper = st.session_state['datper']
datrpre = st.session_state['datrpre']
precon = st.session_state['precon']
selpre = st.session_state['selpre']
datperXdon = st.session_state['datperXdon']
dones = st.session_state['dones']

#st.write(dones)
st.header('Test de Dones')
col1, col2 = st.columns(2)
col1.info(datper[1])
#col2.warning('🔀 	   🔀 	    🔀🔀 	   🔀 	    🔀')
col2.info(datper[3])

st.subheader(selpre[1])
don = selpre[0]
#st.write(datperXdon)
for t in datperXdon:
    if t[0]==don:
        encontrado = True
        break
    else:
        encontrado = False
#st.write('encontrado = ', encontrado)
# Número 1 = no mucho o nada; Número 2 = un poquito; Número 3 = algo; Número 4 = mucho
#selecion = st.radio('opciones',[0,'poco','bajo','alto','mucho'], horizontal=True, index=0)

# ------>> lineasel = st.slider(label='porcentaje',min_value=0,max_value=100)
vlinea = random.randint(1,100)
lineasel = st.slider(label='porcentaje',min_value=0,max_value=100, value=vlinea)

if lineasel==0: selecion='-'
elif lineasel in range(0,30): selecion='poco'
elif lineasel in range(30,50): selecion='bajo'
elif lineasel in range(50,75): selecion='alto'
else: selecion='mucho'
st.latex(selecion)
if lineasel>0:
    precon.append(selpre)
    datrpre.remove(selpre)
    if selecion=='poco': valor = 5
    elif selecion=='bajo': valor = 10
    elif selecion=='alto': valor = 15
    else: valor = 20
        # st.write('Don = ',don)
    if encontrado==False:
        nr = [don, valor]
        datperXdon.append(nr)
        #st.write(encontrado)
        #st.write(datperXdon)
    else:
        #st.write(encontrado)
        for t in datperXdon:
            if t[0]==don:
                t[1]+=valor

    #st.write('Debe marcar alguna opción')
else:
    st.warning('Debe registrar un porcentaje')
    st.stop()
with st.empty():
    for seconds in range(2):
        st.write(f"⏳")
        time.sleep(1)
    st.write("✔️")
    st.session_state['precon']=precon
    st.session_state['dartpre']=datrpre

switch_page('preguntas02')
