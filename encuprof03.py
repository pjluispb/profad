import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from deta import Deta
import pandas as pd
import datetime

st.set_page_config(
    page_title="Profesionales AD Reg App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",

)

deta = Deta(st.secrets["deta_key"])
encprof = deta.Base('usuarios')
#db_content = encprof.fetch().items
#st.write(db_content)


st.header('Encuesta de Profesionales y Tecnicos de las Asambleas de Dios 2023')

with st.form(key='miform'):
    with st.expander('Datos Personales'):
        nombre = st.text_input('Nombre Completo ---- Obligatorio')
        tlf1 = st.text_input('Nro de telefono   ---- Obligatorio')
        celular = st.text_input('Nro de celular')
        email = st.text_input('Correo electronico principal')
        whatsapp = st.text_input('whatsApp')
        faceb = st.text_input('Facebook')
        instg = st.text_input('Instagram')
        twitter = st.text_input('Twitter')
        direccion = st.text_input('Direccion')
        Edo_Civil = st.selectbox('Estado Civil',['Soltero','Casado','Viudo','Otro'])
        #fecnac = st.date_input('Fecha de nacimiento',min_value=datetime.date(1940,1,1))
        edad = st.slider('edad')

    with st.expander('Datos de la iglesia a la que asiste'):
        iglesia = st.text_input('Nombre de la iglesia a la cual asiste')
        Pastor = st.text_input('Nombre del pastor de la iglesia a la cual asiste')
        DireccionIglesia = st.text_input('Direccion de la iglesia a la cual asiste')

    with st.expander('Datos academicos'):
        marca_de_estudios = st.multiselect('Selecciona los estudios completados',
        ['Primaria','Secundaria','Tecnico Medio','Tecnico Universitario','Pregrado Universitario','PostGrado Universitario'])
        st.write('Introduce los estudios academicos realizados o en curso, junto con el titulo o certificado obtenido')
        col3, col4 = st.columns(2)
        with col3:
            estudio1 = st.text_input('estudios', key='est1')
            estudio2 = st.text_input('estudios', key='est2')
            #estudio3 = st.text_input('estudios', key='est3')
        with col4:
            certifi1 = st.text_input('Certificado/Titulo', key='cert1')
            certifi2 = st.text_input('Certificado/Titulo', key='cert2')
            #certifi3 = st.text_input('Certificado/Titulo', key='cert3')
        otrosEstudiosAcademicos = st.text_area('Escriba informacion adicional sobre otros estudios academicos realizados','''   ----   ''')

    with st.expander('Datos sobre participacion en la iglesia'):
        cargoIgle =st.text_input('Cargo actual en la iglesia')
        st.write('Ministerios en los cuales participo/asisto en mi iglesia')
        min_damas = st.radio("Ministerio de Damas",["ninguna","asisto","participo","lider"],horizontal=True)
        min_caba = st.radio("Ministerio de Caballeros",["ninguna","asisto","participo","lider"],horizontal=True)
        min_diaco = st.radio("Ministerio de Diaconos",["ninguna","asisto","participo","lider"],horizontal=True)
        min_jov = st.radio("Ministerio de Jovenes",["ninguna","asisto","participo","lider"],horizontal=True)
        min_ados = st.radio("Ministerio de Adolescentes",["ninguna","asisto","participo","lider"],horizontal=True)
        min_ninos = st.radio("Ministerio de Ninnos",["ninguna","asisto","participo","lider"],horizontal=True)
        min_aa = st.radio("Ministerio de Alabanza",["ninguna","asisto","participo","lider"],horizontal=True)
        min_fami = st.radio("Ministerio de Familia",["ninguna","asisto","participo","lider"],horizontal=True)
        min_misio = st.radio("Ministerio de Misiones",["ninguna","asisto","participo","lider"],horizontal=True)
        min_celu = st.radio("Ministerio de Celular",["ninguna","asisto","participo","lider"],horizontal=True)
        min_ense = st.radio("Ministerio de Ensenanza",["ninguna","asisto","participo","lider"],horizontal=True)
        min_prof = st.radio("Ministerio de Profesionales",["ninguna","asisto","participo","lider"],horizontal=True)
        otrosMin = st.text_area('Otros Ministerios', '''  ''')


    with st.expander('Datos acerca del trabajo'):
        col1, col2 = st.columns(2)
        cargo1=st.container()
        with col1:
            cargo_tra_1 = st.text_input('cargo-1', key='cargo1')
            cargo_tra_2 = st.text_input('cargo-2', key='cargo2')
            cargo_tra_3 = st.text_input('cargo-3', key='cargo3')
            cargo_tra_4 = st.text_input('cargo-4', key='cargo4')
        with col2:
            empresa_1 = st.text_input('empresa/institucion', key='emp1')
            empresa_2 = st.text_input('empresa/institucion', key='emp2')
            empresa_3 = st.text_input('empresa/institucion', key='emp3')
            empresa_4 = st.text_input('empresa/institucion', key='emp4')
        otrosc = st.text_area('Ingrese informacion adicional sobre otros cargos/trabajos realizados',''' -----''')


    with st.expander('Datos acerca de su testimonio'):
        fec_conversion = st.date_input('Fecha de Conversion', min_value=datetime.date(1940,1,1))
        fec_bautismo_agua = st.date_input('Fecha de Bautismo en agua', min_value=datetime.date(1940,1,1))
        fec_bautismo_Espiritu = st.date_input('Fecha de Bautismo en el Espiritu Santo', min_value=datetime.date(1940,1,1))
        testimonio = st.text_area('compartenos tu breve testimonio', '''  ''')



    with st.expander('Datos acerca de estudios biblicos'):
        st.write('Estudios discipulares / biblicos / teologicos (Completados o en proceso)')
        col5, col6 = st.columns(2)
        with col5:
            estudiob1 = st.text_input('estudio biblico', key='estb1')
            estudiob2 = st.text_input('estudio biblico', key='estb2')
            estudiob3 = st.text_input('estudio biblico', key='estb3')
            estudiob4 = st.text_input('estudio biblico', key='estb4')
        with col6:
            nivCertBib1 = st.text_input('Nivel actual o Certificado', key='ncb1')
            nivCertBib2 = st.text_input('Nivel actual o Certificado', key='ncb2')
            nivCertBib3 = st.text_input('Nivel actual o Certificado', key='ncb3')
            nivCertBib4 = st.text_input('Nivel actual o Certificado', key='ncb4')
        otrosEstudiosBibllicos = st.text_area('Escriba informacion adicional sobre otros estudios discipulares/biblicos/teologicos realizados','''
        ----''')

    preclave1 = st.checkbox('Estarias dispuesto a servir al Senor con tus talentos y profesion en el departamento de profesionales y tecnicos de las Asambleas de Dios en el  distrito Andino?')

    if preclave1:
        st.write('Genial. Te estaremos contactando a ti y a tu pastor para conversar acerca del tema')
        st.write('Que Dios te bendiga')

    #CheckyEnvia = st.button('Enviar Datos')
    CheckyEnvia = st.form_submit_button('Enviar Datos')

    if CheckyEnvia:
        st.write('Verificando data')
        registro = {
            "nombre": nombre,
            "tlf1": tlf1,
            "celular": celular,
            "email": email,
            "whatsapp": whatsapp,
            "faceb": faceb,
            "instg": "",
            "twitter": "",
            "direccion": direccion,
            "Edo_Civil": Edo_Civil,
            "edad": edad,
            "iglesia": iglesia,
            "Pastor": Pastor,
            "DireccionIglesia": DireccionIglesia,
            "estudio1": estudio1,
            "certifi1": certifi1,
            "estudio2": estudio2,
            "certifi2": certifi2,
            "otrosEstudiosAcademicos": otrosEstudiosAcademicos
            }
        #print(otrosEstudiosAcademicos)
        #st.write(otrosEstudiosAcademicos)
        #registro
        st.write('Enviando data')

        #encprof.put(registro)
        encprof.put({
            "nombre": nombre,
            "tlf1": tlf1,
            "celular": celular,
            "email": email,
            "whatsapp": whatsapp,
            "faceb": faceb,
            "instg": "",
            "twitter": "",
            "direccion": direccion,
            "Edo_Civil": Edo_Civil,
            "edad": edad,
            "iglesia": iglesia,
            "Pastor": Pastor,
            "DireccionIglesia": DireccionIglesia,
            "estudio1": estudio1,
            "certifi1": certifi1,
            "estudio2": estudio2,
            "certifi2": certifi2,
            "otrosEstudiosAcademicos": otrosEstudiosAcademicos,
            "cargoIgle": cargoIgle,
            "min_damas": min_damas,
            "min_caba": min_caba,
            "min_diaco": min_diaco,
            "min_jov": min_jov,
            "min_ados": min_ados,
            "min_ninos": min_ninos,
            "min_aa": min_aa,
            "min_fami": min_fami,
            "min_misio": min_misio,
            "min_celu": min_celu,
            "min_ense": min_ense,
            "min_prof": min_prof,
            "otrosMin": otrosMin
            })


        db_content = encprof.fetch().items
        regdb = encprof.fetch({"nombre?contains": nombre}).items
        st.write(regdb)
        #sdf = pd.Series(registro)
        sdf = pd.Series(regdb)
        st.write(sdf)
        clave = regdb['key']
        session_state['clave'] = clave
        
        
volver = st.button('Volver')
if volver:
    #st.experimental_rerun()
    switch_page('reiniciar')
