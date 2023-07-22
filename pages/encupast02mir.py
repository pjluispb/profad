


import streamlit as st
from streamlit_extras.switch_page_button import switch_page
# import extra_streamlit_components as stx
import cv2
import os
from PIL import Image, ImageDraw, ImageFont
from deta import Deta
import pandas as pd
import io
import random

st.set_page_config(
    page_title="ASIGLEH app",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",

)

deta = Deta(st.secrets.deta_key)
photos = deta.Drive(name='asiglehphotos')
encuasigleh = deta.Base('asiglehpastores')

try:
    nombreu = st.session_state['nombreu']
    cedulau = st.session_state['cedulau']
    clave = st.session_state['clave']
    rol = st.session_state['rol']
except:
    st.write('error recuperando variables de sesión')

# st.write(nombreu, cedulau, clave, rol)
registro = encuasigleh.get(key=clave)
# st.write(registro)

def shootfoto(cond):
    if cond:
        st.write('tomafoto')
        st.stop()
        switch_page('surtphoto04b')
    return

st.header('Encuesta del Pastorado ASIGLEH 2023')
st.subheader('Iglesia de Los Hermanos - Venezuela')
st.write(' Bienvenido usuario '+nombreu)
st.text('Ficha de Registro')

st.subheader('Datos Personales')
with st.expander('Datos Personales'):
    dfper = pd.DataFrame(
    [
       {"item": "Nombres", "valor": registro["Nombres"]},
       {"item": "Apellidos", "valor": registro["Apellidos"]},
       {"item": "Teléfono", "valor": registro["Telefono"]},
       {"item": "Celular", "valor": registro["Celular"]},
       {"item": "email", "valor": registro["email"]},
       {"item": "Whatsapp", "valor": registro["Whatsapp"]},
       {"item": "Facebook", "valor": registro["Facebook"]},
       {"item": "Instagram", "valor": registro["Instagram"]},
       {"item": "Twitter", "valor": registro["Twitter"]},
       {"item": "Dirección", "valor": registro["Direccion"]},
       {"item": "Edo Civil", "valor": registro["Edo_Civil"]},
       {"item": "Edad", "valor": registro["Edad"]},
   ]
)
    st.dataframe(data=dfper, hide_index=True, width=1000)
    fotoper = clave+'_'+'dper_ima01_s100.png'
    try:
        imagenPer = photos.get(fotoper)
        conten = imagenPer.read()
        st.image(conten)
    except:
        btFotoPer = st.button('Tomar foto personal')
        if btFotoPer:
            st.session_state['nameima'] = fotoper
            switch_page('surtphoto04b')
        st.write('***')
    editar_per = st.button('Editar datos personales')
    if editar_per:
        switch_page('encupast02edit')

st.subheader('Ministerio ó Iglesia que pastorea')
with st.expander('Datos de la iglesia/ministerio que pastorea ó desempeña'):
    dfima = pd.DataFrame(
    [
       {"item": "Iglesia/Ministerio", "valor": registro["Iglesia"]},
       {"item": "Dirección ", "valor": registro["DireccionIglesia"]},
   ]
)
    st.dataframe(data=dfima, hide_index=True, width=1000)
    editar_igle = st.button('Editar datos de la iglesia/ministerio')
    if editar_igle:
        switch_page('encupast02edit')

st.subheader('Datos Académicos')
with st.expander('Datos académicos'):
    st.info('Estudios en curso ó concluidos')
    st.success(registro["nivestudios"])
    st.write('***')
    col1, col2= st.columns(2)
    if registro['estudio1']!=None:
        col1.info(registro['estudio1'])
        if registro['certifi1']==None:
            certificado = 'N/A'
        else:
            certificado = registro['certifi1']
        col2.success(certificado)
        fotoCerA1 = clave+'_eAcademico_ima01_si00.png'
        try:
            imagenCer = photos.get(fotoCerA1)
            content = imagenCer.read()
            st.image(content)
        except:
            btcer1 = st.button('tomar foto del Certificado')
            if btcer1:
                st.session_state['nameima'] = fotoCerA1
                switch_page('surtphoto04b')
            st.write('***')
    col1, col2= st.columns(2)
    if registro['estudio2']!=None:
        col1.info(registro['estudio2'])
        if registro['certifi2']==None:
            certificado = 'N/A'
        else:
            certificado = registro['certifi2']
        col2.success(certificado)
        fotoCerA1 = clave+'_eAcademico_ima02_si00.png'
        try:
            imagenCer = photos.get(fotoCerA1)
            content = imagenCer.read()
            st.image(content)
        except:
            btcer1 = st.button('tomar foto del Certificado')
            if btcer1:
                st.session_state['nameima'] = fotoCerA1
                switch_page('surtphoto04b')
            st.write('***')
    col1, col2= st.columns(2)
    if registro['estudio3']!=None:
        col1.info(registro['estudio3'])
        if registro['certifi3']==None:
            certificado = 'N/A'
        else:
            certificado = registro['certifi3']
        col2.success(certificado)
        fotoCerA1 = clave+'_eAcademico_ima03_si00.png'
        try:
            imagenCer = photos.get(fotoCerA1)
            content = imagenCer.read()
            st.image(content)
        except:
            btcer1 = st.button('tomar foto del Certificado')
            if btcer1:
                st.session_state['nameima'] = fotoCerA1
                switch_page('surtphoto04b')
            st.write('***')
    col1, col2= st.columns(2)
    if registro['estudio4']!=None:
        col1.info(registro['estudio4'])
        if registro['certifi4']==None:
            certificado = 'N/A'
        else:
            certificado = registro['certifi4']
        col2.success(certificado)
        fotoCerA1 = clave+'_eAcademico_ima04_si00.png'
        try:
            imagenCer = photos.get(fotoCerA1)
            content = imagenCer.read()
            st.image(content)
        except:
            btcer1 = st.button('tomar foto del Certificado')
            if btcer1:
                st.session_state['nameima'] = fotoCerA1
                switch_page('surtphoto04b')
            st.write('***')
    col1, col2= st.columns(2)
    if registro['estudio5']!=None:
        col1.info(registro['estudio5'])
        if registro['certifi5']==None:
            certificado = 'N/A'
        else:
            certificado = registro['certifi5']
        col2.success(certificado)
        fotoCerA1 = clave+'_eAcademico_ima05_si00.png'
        try:
            imagenCer = photos.get(fotoCerA1)
            content = imagenCer.read()
            st.image(content)
        except:
            btcer1 = st.button('tomar foto del Certificado')
            if btcer1:
                st.session_state['nameima'] = fotoCerA1
                switch_page('surtphoto04b')
            st.write('***')
    if registro['otrosEstudiosAcademicos']!=None:
        st.info(registro['otrosEstudiosAcademicos'])
    editar_dataca = st.button('Editar datos académicos')

st.subheader('Datos sobre participación en su iglesia')
with st.expander('Datos sobre participación en los ministerios de su iglesia'):
    dfpartmini = pd.DataFrame(
    [
       {"item": "Ministerio de Damas", "valor": registro["min_damas"]},
       {"item": "Ministerio de Caballeros ", "valor": registro["min_caba"]},
       {"item": "Ministerio de Diáconos", "valor": registro["min_diaco"]},
       {"item": "Ministerio de Jóvenes ", "valor": registro["min_jov"]},
       {"item": "Ministerio de Adolescentes", "valor": registro["min_ados"]},
       {"item": "Ministerio de Niños ", "valor": registro["min_ninos"]},
       {"item": "Ministerio de Alabanza", "valor": registro["min_aa"]},
       {"item": "Ministerio de Familia ó Matrimonios ", "valor": registro["min_fami"]},
       {"item": "Ministerio de Misiones", "valor": registro["min_misio"]},
       {"item": "Ministerio Celular ", "valor": registro["min_celu"]},
       {"item": "Ministerio de Educación Cristiana", "valor": registro["min_ense"]},
       {"item": "Ministerio de Profesionales ", "valor": registro["min_prof"]},
   ]
)   
    st.dataframe(data=dfpartmini, hide_index=True, width=1000)
    if registro['otrosMin']!=None:
        st.info('Otros Ministerios/Departamentos de mi iglesia en los que participo')
        st.success(registro['otrosMin'])
    editar_partmini = st.button('Editar sobre participación en los ministerios de su iglesia')

st.subheader('Datos sobre su trabajo ministerial')
with st.expander('Datos sobre su trabajo ministerial'):
    col1, col2= st.columns(2)
    if registro['minist_1']!=None:
        col1.info('Ministerio: '+registro['minist_1'])
        if registro['orgigle_1']==None:
            orgigle = 'N/A'
        else:
            orgigle = registro['orgigle_1']
        col2.success('Organización ó Iglesia: '+orgigle)
        timin = 'Tiempo en dicho ministerio: '+str(registro['tiempominist_1'])
        st.write(timin)
        st.write('Descripción: '+registro['descripmin_1'])
    col1, col2= st.columns(2)
    if registro['minist_2']!=None:
        col1.info('Ministerio: '+registro['minist_2'])
        if registro['orgigle_2']==None:
            orgigle = 'N/A'
        else:
            orgigle = registro['orgigle_2']
        col2.success('Organización ó Iglesia: '+orgigle)
        timin = 'Tiempo en dicho ministerio: '+str(registro['tiempominist_2'])
        st.write(timin)
        st.write('Descripción: '+registro['descripmin_2'])
    col1, col2= st.columns(2)
    if registro['minist_3']!=None:
        col1.info('Ministerio: '+registro['minist_3'])
        if registro['orgigle_3']==None:
            orgigle = 'N/A'
        else:
            orgigle = registro['orgigle_3']
        col2.success('Organización ó Iglesia: '+orgigle)
        timin = 'Tiempo en dicho ministerio: '+str(registro['tiempominist_3'])
        st.write(timin)
        st.write('Descripción: '+registro['descripmin_3'])
    col1, col2= st.columns(2)
    if registro['minist_4']!=None:
        col1.info('Ministerio: '+registro['minist_4'])
        if registro['orgigle_4']==None:
            orgigle = 'N/A'
        else:
            orgigle = registro['orgigle_4']
        col2.success('Organización ó Iglesia: '+orgigle)
        timin = 'Tiempo en dicho ministerio: '+str(registro['tiempominist_4'])
        st.write(timin)
        st.write('Descripción: '+registro['descripmin_4'])
    col1, col2= st.columns(2)
    if registro['minist_5']!=None:
        col1.info('Ministerio: '+registro['minist_5'])
        if registro['orgigle_5']==None:
            orgigle = 'N/A'
        else:
            orgigle = registro['orgigle_5']
        col2.success('Organización ó Iglesia: '+orgigle)
        timin = 'Tiempo en dicho ministerio: '+str(registro['tiempominist_5'])
        st.write(timin)
        st.write('Descripción: '+registro['descripmin_5'])
    st.write('Otros ministerios en los que he servido: ' +registro['otrostrabmin'])

st.subheader('Datos acerca de su testimonio')
with st.expander('Datos acerca de su testimonio'):
    dftestimonio = pd.DataFrame(
    [
       {"item": "Fecha de Conversión", "valor": registro["fec_conversion"]},
       {"item": "Fecha de Bautismo en agua ", "valor": registro["fec_bautismo_agua"]},
       {"item": "Fecha de Bautismo en el Espiritu Santo", "valor": registro["fec_bautismo_Espiritu"]},
   ]
)   
    st.dataframe(data=dftestimonio, hide_index=True, width=1000)
    if registro['testimonio']!=None:
        st.info('Testimonio de salvación')
        st.success(registro['testimonio'])
    if registro['llamado']!=None:
        st.info('Testimonio de llamado ministerial')
        st.success(registro['llamado'])
    editar_testimonio = st.button('Editar datos acerca de su testimonio')

st.subheader('Datos acerca de su salud')
with st.expander('Datos acerca de su salud'):
    #{ 'traumaciru':traumaciru, 'Inmualertrans':Inmualertrans, 

    st.subheader('Antecedentes NO patológicos')
    dfsalud1 = pd.DataFrame(
    [
       {"item": "Tabaquismo", "valor": registro["tabaq"]},
       {"item": "Cigarros diarios ", "valor": registro["cigarrosSlide"]},
       {"item": "Ex-Fumador", "valor": registro["exfumador"]},
       {"item": "Fumador Pasivo", "valor": registro["fumadorPasivo"]},
       {"item": "Años de Consumo ó Exposición", "valor": registro["consumoExposicion"]},
       {"item": "Alcohol", "valor": registro["alcohol"]},
       {"item": "Litros de Alcohol por semana", "valor": registro["cantidadXsem"]},
       {"item": "Años de consumo", "valor": registro["tiempoDeConsumo"]},
       {"item": "Ex-Alcohólico", "valor": registro["exalcoholico"]},
       {"item": "Alcohólico Ocasional", "valor": registro["AlcoholicOcasional"]},
       {"item": "Alergias", "valor": registro["alergias"]},
   ]
)   
    st.dataframe(data=dfsalud1, hide_index=True, width=1000)
    if registro['queAlergias']!=None:
        st.info('¿Cuáles alergias?')
        st.success(registro['queAlergias'])
    dfsalud2 = pd.DataFrame(
    [
       {"item": "Tipo de Sangre ", "valor": registro["tipoSangre"]},
       {"item": "Farmacodependiente ", "valor": registro["farmacodependencia"]},
       {"item": "Años de consumo", "valor": registro["farmacoTiempo"]},
   ]
)   
    st.dataframe(data=dfsalud2, hide_index=True, width=1000)
    if registro['observaciones']!=None:
        st.info('Observaciones: '+registro['observaciones'])
    if registro['enfermedadesInfancia']!=None:
        st.info('Enfermedades de Infancia: '+registro['enfermedadesInfancia'])
    if registro['secuelas']!=None:
        st.info('Secuelas: '+registro['secuelas'])
    st.subheader('Antecedentes personales patológicos')
    dfsalud3 = pd.DataFrame(
    [
       {"item": "Padecimientos de Infancia ", "valor": registro["padeinfa"]},
       {"item": "Parásitos intestinales ", "valor": registro["parasin"]},
       {"item": "Neurológicos", "valor": registro["neurologico"]},
       {"item": "Fiebre reumática", "valor": registro["fiebrereuma"]},
       {"item": "Tubercolosis ", "valor": registro["tuberculosis"]},
       {"item": "Diábetes mellitus", "valor": registro["diabemelitus"]},
       {"item": "Fiebres eruptivas ", "valor": registro["fiebreuptiva"]},
       {"item": "Paroditis Epidémica", "valor": registro["parodiepi"]},

       {"item": "Enfermedades venéreas ", "valor": registro["enfermavene"]},
       {"item": "Tifoidea ", "valor": registro["tifoidea"]},
       {"item": "Mentales", "valor": registro["mentales"]},
       {"item": "Inmuno-alergias e hipersensibilidad", "valor": registro["inmunalergi"]},
       {"item": "Vaculares ", "valor": registro["vasculares"]},
       {"item": "Malformaciones congénitas", "valor": registro["malforcon"]},
       {"item": "Diarreas ", "valor": registro["diarreas"]},
       {"item": "Difteria", "valor": registro["difteria"]},

       {"item": "Artropatías ", "valor": registro["artropatias"]},
       {"item": "Hipertensión arterial ", "valor": registro["hipertension"]},
       {"item": "Exposición a radiación", "valor": registro["exporadia"]},
       {"item": "Paludismo", "valor": registro["paludismo"]},
       {"item": "Sífilis y otras enfermedades venéreas ", "valor": registro["sifilisov"]},
       {"item": "Meningitis", "valor": registro["meningitis"]},
       {"item": "Poliomielitis ", "valor": registro["polio"]},
       {"item": "Otros Padecimientos de importancia", "valor": registro["otrospad"]},
   ]
)   
    st.dataframe(data=dfsalud3, hide_index=True)
    if registro['traumaciru']!=None:
        st.info('Trumatismos y Cirugías')
        st.success(registro['traumaciru'])
    if registro['Inmualertrans']!=None:
        st.info('Inmunizaciones, Alergias y Transfusiones')
        st.success(registro['Inmualertrans'])
    editar_datsalud = st.button('Editar datos acerca de su salud')

st.subheader('Datos sobre estudios bíblicos')
with st.expander('Datos sobre estudios bíblicos'):
    # st.subheader('Estudios Bíblicos/discipulares/Teológicos en curso ó concluidos')
    col1, col2= st.columns(2)
    if registro['estudiob1']!=None:
        col1.info(registro['estudiob1'])
        if registro['nivCertBib1']==None:
            certificado = 'N/A'
        else:
            certificado = registro['nivCertBib1']
        col2.success(certificado)
        fotoCerA1 = clave+'_eBiblico_ima01_si00.png'
        try:
            imagenCer = photos.get(fotoCerA1)
            content = imagenCer.read()
            st.image(content)
        except:
            btcerb1 = st.button('tomar foto del Certificado', key='btcerb1')
            if btcerb1:
                st.session_state['nameima'] = fotoCerA1
                switch_page('surtphoto04b')
            st.write('***')
    col1, col2= st.columns(2)
    if registro['estudiob2']!=None:
        col1.info(registro['estudiob2'])
        if registro['nivCertBib2']==None:
            certificado = 'N/A'
        else:
            certificado = registro['nivCertBib2']
        col2.success(certificado)
        fotoCerA1 = clave+'_eBiblico_ima02_si00.png'
        try:
            imagenCer = photos.get(fotoCerA1)
            content = imagenCer.read()
            st.image(content)
        except:
            btcerb2 = st.button('tomar foto del Certificado', key='btcerb2')
            if btcerb2:
                st.session_state['nameima'] = fotoCerA1
                switch_page('surtphoto04b')
            st.write('***')
    col1, col2= st.columns(2)
    if registro['estudiob3']!=None:
        col1.info(registro['estudiob3'])
        if registro['nivCertBib3']==None:
            certificado = 'N/A'
        else:
            certificado = registro['nivCertBib3']
        col2.success(certificado)
        fotoCerA1 = clave+'_eBiblico_ima03_si00.png'
        try:
            imagenCer = photos.get(fotoCerA1)
            content = imagenCer.read()
            st.image(content)
        except:
            btcerb3 = st.button('tomar foto del Certificado', key='btcerb3')
            if btcerb3:
                st.session_state['nameima'] = fotoCerA1
                switch_page('surtphoto04b')
            st.write('***')
    col1, col2= st.columns(2)
    if registro['estudiob4']!=None:
        col1.info(registro['estudiob4'])
        if registro['nivCertBib4']==None:
            certificado = 'N/A'
        else:
            certificado = registro['nivCertBib4']
        col2.success(certificado)
        fotoCerA1 = clave+'_eBiblico_ima04_si00.png'
        try:
            imagenCer = photos.get(fotoCerA1)
            content = imagenCer.read()
            st.image(content)
        except:
            btcerb4 = st.button('tomar foto del Certificado', key='btcerb4')
            if btcerb4:
                st.session_state['nameima'] = fotoCerA1
                switch_page('surtphoto04b')
            st.write('***')
    if registro['otrosEstudiosBiblicos']!=None:
        st.info('Otros Estudios Bíblicos')
        st.success(registro['otrosEstudiosBiblicos'])
    editar_datebib = st.button('Editar datos de estudios bíblicos')


