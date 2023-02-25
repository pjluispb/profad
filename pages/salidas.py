import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from deta import Deta
import pandas as pd

pd.set_option('display.max_colwidth', None)

deta = Deta(st.secrets["deta_key"])

#clave = st.session_state['clave']
#st.write('clave = ',clave)
try:
    clave = st.session_state['clave']
except:
    st.error('Error en la conexion')
    st.warning('Error en la conexion. Volviendo a pagina de inicio')
    switch_page('encuprof05')

usuarios = deta.Base('usuarios')
rec1=usuarios.get(clave)
#st.info('''Felicitaciones, los datos han sido grabados en la base de datos. Aqui los puedes ver :thumb up: ''')
#st.write(rec1)
sdf = pd.Series(rec1)
#sdf

registro = {
  "DireccionIglesia": "Al lado de mi casa #121",
  "Edo_Civil": "Soltero",
  "Pastor": "Exit oque",
  "cargoIgle": "",
  "celular": "01422555652",
  "certifi1": "",
  "certifi2": "",
  "direccion": "En algun lugar del barrio chino de Merida calle sin nombre # 45-12b. Los Sauzales. Mérida. Estado Mérida. 51011. Venezuela",
  "edad": 29,
  "email": "Lunchau123@jos.elu",
  "estudio1": "",
  "estudio2": "",
  "faceb": "Lun Chau Chino",
  "iglesia": "Sin Salida",
  "instg": "",
  "key": "dbxvjwbhxf2n",
  "min_aa": "ninguna",
  "min_ados": "ninguna",
  "min_caba": "ninguna",
  "min_celu": "participo",
  "min_damas": "ninguna",
  "min_diaco": "participo",
  "min_ense": "ninguna",
  "min_fami": "ninguna",
  "min_jov": "lider",
  "min_misio": "ninguna",
  "min_ninos": "ninguna",
  "min_prof": "ninguna",
  "nombre": "Lun Chau",
  "otrosEstudiosAcademicos": "Estudios por internet y a distancia de los institutos de preparacion para la vida en todo el continente americano, pero en especial de Ecuador",
  "otrosMin": "  ",
  "tlf1": "54646546464",
  "twitter": "",
  "whatsapp": "+58 456 321 7496"
}

registro = rec1

#st.snow()
st.header('Encuesta de Liderazgo Eclesial de las Asambleas de Dios 2023')
st.subheader('Distrito Andino - Zona 1')
st.write('Elaborado por APTA - Dtto Andino')
st.text('Ficha de Registro')
st.write('** **')
st.subheader('Datos Personales')
col1, col2 = st.columns(2)

with col1:
    st.write('**Nombre Completo**')
    st.success(registro['nombre'], icon="✅")
    st.write('**celular**')
    st.info(registro['celular'], icon="ℹ️")
    st.write('**Whatsapp**')
    st.success(registro['whatsapp'], icon="✅")
    st.write('**Instagram**')
    st.info(registro['instg'], icon="ℹ️")

with col2:
    st.write('**Telefono**')
    st.info(registro['tlf1'], icon="ℹ️")
    st.write('**Correo**')
    st.success(registro['email'], icon="✅")
    st.write('**Facebook**')
    st.info(registro['faceb'], icon="ℹ️")
    st.write('**Twitter**')
    st.success(registro['twitter'], icon="✅")
   
st.write('****Direccion****')
st.warning(registro['direccion'], icon="⚠️")
col3, col4 = st.columns(2)
with col3:
    st.write('**Estado Civil**')
    st.success(registro['Edo_Civil'], icon="✅")
with col4:
    st.write('**Edad**')
    st.info(registro['edad'], icon="ℹ️")

st.write('** **')
st.subheader('Datos de la iglesia a la que asiste')
st.write('**Nombre de la iglesia a la cual asiste**')
st.success(registro['iglesia'], icon="✅")
st.write('**Nombre del pastor de la iglesia a la cual asiste**')
st.info(registro['Pastor'], icon="ℹ️")
st.write('**Direccion de la iglesia a la cual asiste**')
st.success(registro['DireccionIglesia'], icon="✅")

st.write('** **')
st.subheader('Datos Academicos')
st.write('Estudios academicos completados o en curso')
st.write('**Estudios**')
st.info(registro['estudio1'], icon="ℹ️")
st.write('**Certificado/Titulo**')
st.success(registro['certifi1'], icon="✅")
st.write('**Estudios**')
st.info(registro['estudio2'], icon="ℹ️")
st.write('**Certificado/Titulo**')
st.success(registro['certifi2'], icon="✅")
st.write('**informacion adicional sobre otros estudios academicos realizados**')
st.warning(registro['otrosEstudiosAcademicos'], icon="⚠️")

st.write('** **')
st.subheader('Datos sobre participacion en la iglesia')
st.write('**Cargo actual en la iglesia**')
st.info(registro['cargoIgle'], icon="ℹ️")
st.write('**Ministerios en los cuales participo/asisto en mi iglesia**')
col5, col6, col7, col8 = st.columns(4)

with col5:
    st.write('**Damas**')
    if registro['min_damas'] == 'ninguna':st.warning(registro['min_damas'], icon="🚨")
    if registro['min_damas'] == 'asisto':st.warning(registro['min_damas'], icon="⚠️")
    if registro['min_damas'] == 'participo':st.info(registro['min_damas'], icon="ℹ️")
    if registro['min_damas'] == 'lider':st.success(registro['min_damas'], icon="✅")
    #st.info(registro['min_damas'], icon="ℹ️")
    st.write('**Caballeros**')
    if registro['min_caba'] == 'ninguna':st.warning(registro['min_caba'], icon="🚨")
    if registro['min_caba'] == 'asisto':st.warning(registro['min_caba'], icon="⚠️")
    if registro['min_caba'] == 'participo':st.info(registro['min_caba'], icon="ℹ️")
    if registro['min_caba'] == 'lider':st.success(registro['min_caba'], icon="✅")
    #st.success(registro['min_caba'], icon="✅")
    st.write('**Diaconos**')
    if registro['min_diaco'] == 'ninguna':st.warning(registro['min_diaco'], icon="🚨")
    if registro['min_diaco'] == 'asisto':st.warning(registro['min_diaco'], icon="⚠️")
    if registro['min_diaco'] == 'participo':st.info(registro['min_diaco'], icon="ℹ️")
    if registro['min_diaco'] == 'lider':st.success(registro['min_diaco'], icon="✅")
    #st.info(registro['min_diaco'], icon="ℹ️")


with col6:
    st.write('**Jovenes**')
    if registro['min_jov'] == 'ninguna':st.warning(registro['min_jov'], icon="🚨")
    if registro['min_jov'] == 'asisto':st.warning(registro['min_jov'], icon="⚠️")
    if registro['min_jov'] == 'participo':st.info(registro['min_jov'], icon="ℹ️")
    if registro['min_jov'] == 'lider':st.success(registro['min_jov'], icon="✅")
    #st.success(registro['min_jov'], icon="✅")
    st.write('**Adolescentes**')
    if registro['min_ados'] == 'ninguna':st.warning(registro['min_ados'], icon="🚨")
    if registro['min_ados'] == 'asisto':st.warning(registro['min_ados'], icon="⚠️")
    if registro['min_ados'] == 'participo':st.info(registro['min_ados'], icon="ℹ️")
    if registro['min_ados'] == 'lider':st.success(registro['min_ados'], icon="✅")
    #st.info(registro['min_ados'], icon="ℹ️")
    st.write('**Ninnos**')
    if registro['min_ninos'] == 'ninguna':st.warning(registro['min_ninos'], icon="🚨")
    if registro['min_ninos'] == 'asisto':st.warning(registro['min_ninos'], icon="⚠️")
    if registro['min_ninos'] == 'participo':st.info(registro['min_ninos'], icon="ℹ️")
    if registro['min_ninos'] == 'lider':st.success(registro['min_ninos'], icon="✅")
    #st.success(registro['min_ninos'], icon="✅")

with col7:
    st.write('**Alabanza**')
    if registro['min_aa'] == 'ninguna':st.warning(registro['min_aa'], icon="🚨")
    if registro['min_aa'] == 'asisto':st.warning(registro['min_aa'], icon="⚠️")
    if registro['min_aa'] == 'participo':st.info(registro['min_aa'], icon="ℹ️")
    if registro['min_aa'] == 'lider':st.success(registro['min_aa'], icon="✅")
    #st.info(registro['min_aa'], icon="ℹ️")
    st.write('**Familia**')
    if registro['min_fami'] == 'ninguna':st.warning(registro['min_fami'], icon="🚨")
    if registro['min_fami'] == 'asisto':st.warning(registro['min_fami'], icon="⚠️")
    if registro['min_fami'] == 'participo':st.info(registro['min_fami'], icon="ℹ️")
    if registro['min_fami'] == 'lider':st.success(registro['min_fami'], icon="✅")
    #st.success(registro['min_fami'], icon="✅")
    st.write('**Misiones**')
    if registro['min_misio'] == 'ninguna':st.warning(registro['min_misio'], icon="🚨")
    if registro['min_misio'] == 'asisto':st.warning(registro['min_misio'], icon="⚠️")
    if registro['min_misio'] == 'participo':st.info(registro['min_misio'], icon="ℹ️")
    if registro['min_misio'] == 'lider':st.success(registro['min_misio'], icon="✅")
    #st.info(registro['min_misio'], icon="ℹ️")

with col8:
    st.write('**Celular**')
    if registro['min_celu'] == 'ninguna':st.warning(registro['min_celu'], icon="🚨")
    if registro['min_celu'] == 'asisto':st.warning(registro['min_celu'], icon="⚠️")
    if registro['min_celu'] == 'participo':st.info(registro['min_celu'], icon="ℹ️")
    if registro['min_celu'] == 'lider':st.success(registro['min_celu'], icon="✅")
    st.write('**Ensenanza**')
    if registro['min_ense'] == 'ninguna':st.warning(registro['min_ense'], icon="🚨")
    if registro['min_ense'] == 'asisto':st.warning(registro['min_ense'], icon="⚠️")
    if registro['min_ense'] == 'participo':st.info(registro['min_ense'], icon="ℹ️")
    if registro['min_ense'] == 'lider':st.success(registro['min_ense'], icon="✅")
    #st.info(registro['min_ense'], icon="ℹ️")
    st.write('**Profesionales**')
    if registro['min_prof'] == 'ninguna':st.warning(registro['min_prof'], icon="🚨")
    if registro['min_prof'] == 'asisto':st.warning(registro['min_prof'], icon="⚠️")
    if registro['min_prof'] == 'participo':st.info(registro['min_prof'], icon="ℹ️")
    if registro['min_prof'] == 'lider':st.success(registro['min_prof'], icon="✅")
    #st.success(registro['min_prof'], icon="✅")

st.write('**Otros ministerios**')
st.warning(registro['otrosMin'], icon="⚠️")

st.write('** **')
#st.error('This is an error', icon="🚨")
col9, col10, col11 = st.columns(3)
with col9:
    continuar = st.button('Continuar')
    if continuar:
        switch_page('encuprof05')
with col10:
    editar = st.button('Editar')
    if editar:
        #switch_page('encuprof05')
        st.error('modulo en construccion')
with col11:
    salir = st.button('Salir')
    if salir:
        st.error('modulo en construccion')
        #switch_page('encuprof05')
