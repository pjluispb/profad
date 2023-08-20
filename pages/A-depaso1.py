import streamlit as st
from deta import Deta
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import time
from streamlit_extras.switch_page_button import switch_page

deta = Deta(st.secrets["deta_key"])
encuasigleh = deta.Base('asiglehpastores')

clave = st.session_state['clave'] 
# newvalwork = st.session_state['newvalwork']
# newvalea = st.session_state['newvalea'] 
# nombreu = st.session_state['nombreu']
# cedulau = st.session_state['cedulau']

# clave, newvalwork

registro = []
# for key in newvalea:
#     for k,v in key.items():
#         # 'subkey = ', k, v
#         registro.append((k,v))
# # 'registro = ', registro
# dregistro = dict(registro)
'----'
#st.write(dregistro)

# encuasigleh.update(dregistro, clave)

with st.spinner('Espere un momento...'):
    time.sleep(1)
    st.session_state['clave'] = clave
    # st.session_state['newvalea'] = newvalea
    # st.session_state['nombreu'] = nombreu
    # st.session_state['cedulau'] = cedulau
st.success('Listo!')
switch_page('A-encupast04edit')

