import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from deta import Deta
import pandas as pd
import datetime
#from streamlit_toggle import st_toggleswitch
from streamlit_toggle import st_toggle_switch
from streamlit_extras.stateful_button import button

st.set_page_config(
    page_title="ASIGLEH app",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",

)

deta = Deta(st.secrets["deta_key"])
encprof = deta.Base('asiglehpastores')
photos = deta.Drive(name='asiglehphotos')

def update_reg_datper(nombre,tlf1,celular,email,whatsapp, faceb, instg, twitter, direccion, Edo_Civil, edad):
    st.write('update reg-datper')
    st.write(nombre, tlf1, celular, email, whatsapp, faceb, instg, twitter, direccion, Edo_Civil, edad)
    encprof.update({'Nombres': nombre, 'Telefono': tlf1, 'Celular': celular,'email': email, 'nombreu': st.session_state['nombreu'], 'cedulau': st.session_state['cedulau'], 'Whatsapp': whatsapp, 'Facebook': faceb, 'Instagram': instg, 'Twitter': twitter, 'Direccion': direccion, 'Edo_Civil': Edo_Civil,'Edad': edad}, clave)
    

def update_reg_datigle(iglesia, DireccionIglesia):
    st.write('update reg-datigle')
    st.write(iglesia, DireccionIglesia)
    encprof.update({'Iglesia': iglesia, 'DireccionIglesia': DireccionIglesia, 'nombreu': st.session_state['nombreu'], 'cedulau': st.session_state['cedulau']}, clave)

def update_reg_datacade(marca_de_estudios, estudio1, certifi1, estudio2, certifi2, estudio3, certifi3, estudio4, certifi4, estudio5,certifi5, otrosEstudiosAcademicos):
    st.write('update reg-datacade')
    st.write(marca_de_estudios, estudio1, certifi1, estudio2, certifi2,estudio3, certifi3, estudio4, certifi4, estudio5,certifi5, otrosEstudiosAcademicos)
    encprof.update({'nivestudios':marca_de_estudios, 'estudio1':estudio1, 'certifi1':certifi1, 'estudio2':estudio2, 'certifi2':certifi2, 'estudio3':estudio3, 'certifi3':certifi3, 'estudio4':estudio4, 'certifi4':certifi4, 'estudio5':estudio5, 'certifi5':certifi5, 'otrosEstudiosAcademicos':otrosEstudiosAcademicos, 'nombreu':st.session_state['nombreu'], 'cedulau':st.session_state['cedulau']}, clave)

def update_reg_datminigle(min_damas, min_caba, min_diaco, min_jov, min_ados, min_ninos,  min_aa, min_fami, min_misio, min_celu, min_ense, min_prof, otrosMin):
    st.write('update_reg_datminigle')
    st.write(min_damas, min_caba, min_diaco, min_jov, min_ados, min_ninos,  min_aa, min_fami, min_misio, min_celu, min_ense, min_prof, otrosMin)
    encprof.update({'min_damas':min_damas, 'min_caba':min_caba, 'min_diaco':min_diaco, 'min_jov':min_jov, 'min_ados':min_ados, 'min_ninos':min_ninos,  'min_aa':min_aa, 'min_fami':min_fami, 'min_misio':min_misio, 'min_celu':min_celu, 'min_ense':min_ense, 'min_prof':min_prof, 'otrosMin':otrosMin, 'nombreu':st.session_state['nombreu'], 'cedulau':st.session_state['cedulau']}, clave)

def update_reg_dattrabmini(minist_1, orgigle_1, tiempominist_1, descripmin_1, minist_2, orgigle_2, tiempominist_2, descripmin_2, minist_3, orgigle_3, tiempominist_3, descripmin_3, minist_4, orgigle_4, tiempominist_4, descripmin_4, minist_5, orgigle_5, tiempominist_5, descripmin_5, otrostrabmin):
    st.write('update_reg_dattrabmini')
    st.write(minist_1, orgigle_1, tiempominist_1, descripmin_1, minist_2, orgigle_2, tiempominist_2, descripmin_2, minist_3, orgigle_3, tiempominist_3, descripmin_3, minist_4, orgigle_4, tiempominist_4, descripmin_4, minist_5, orgigle_5, tiempominist_5, descripmin_5, otrostrabmin)
    encprof.update({'minist_1':minist_1, 'orgigle_1':orgigle_1, 'tiempominist_1':tiempominist_1, 'descripmin_1':descripmin_1, 'minist_2':minist_2, 'orgigle_2':orgigle_2, 'tiempominist_2':tiempominist_2, 'descripmin_2':descripmin_2, 'minist_3':minist_3, 'orgigle_3':orgigle_3, 'tiempominist_3':tiempominist_3, 'descripmin_3':descripmin_3, 'minist_4':minist_4, 'orgigle_4':orgigle_4, 'tiempominist_4':tiempominist_4, 'descripmin_4':descripmin_4, 'minist_5':minist_5, 'orgigle_5':orgigle_5, 'tiempominist_5':tiempominist_5, 'descripmin_5':descripmin_5, 'otrostrabmin':otrostrabmin, 'nombreu':st.session_state['nombreu'], 'cedulau':st.session_state['cedulau']}, clave)

def update_reg_dattestimonio(fec_conversion, fec_bautismo_agua, fec_bautismo_Espiritu, testimonio, llamado):
    st.write('update_reg_dattestimonio')
    st.write(fec_conversion, fec_bautismo_agua, fec_bautismo_Espiritu, testimonio, llamado)
    encprof.update({'fec_conversion':str(fec_conversion), 'fec_bautismo_agua':str(fec_bautismo_agua), 'fec_bautismo_Espiritu':str(fec_bautismo_Espiritu), 'testimonio':testimonio, 'llamado':llamado, 'nombreu':st.session_state['nombreu'], 'cedulau':st.session_state['cedulau']}, clave)

def update_reg_datsalud(tabaq, cigarrosSlide, exfumador, fumadorPasivo, consumoExposicion, alcohol, cantidadXsem, tiempoDeConsumo, exalcoholico, AlcoholicOcasional, alergias, queAlergias, tipoSangre, farmacodependencia,  farmacoTiempo, observaciones, enfermedadesInfancia, secuelas, padeinfa, parasin, neurologico, fiebrereuma, tuberculosis, diabemelitus, fiebreuptiva, parodiepi, enfermavene,  tifoidea, mentales, inmunalergi, vasculares,  malforcon, diarreas, difteria, artropatias,  hipertension, exporadia, paludismo, sifilisov, meningitis,  polio, otrospad, traumaciru, Inmualertrans):
    st.write('update_reg_datsalud')
    st.write(tabaq, cigarrosSlide, exfumador, fumadorPasivo, consumoExposicion, alcohol, cantidadXsem, tiempoDeConsumo, exalcoholico, AlcoholicOcasional, alergias, queAlergias, tipoSangre, farmacodependencia,  farmacoTiempo, observaciones, enfermedadesInfancia, secuelas, padeinfa, parasin, neurologico, fiebrereuma, tuberculosis, diabemelitus, fiebreuptiva, parodiepi, enfermavene,  tifoidea, mentales, inmunalergi, vasculares,  malforcon, diarreas, difteria, artropatias,  hipertension, exporadia, paludismo, sifilisov, meningitis,  polio, otrospad, traumaciru, Inmualertrans)

    encprof.update({'tabaq':tabaq, 'cigarrosSlide':cigarrosSlide, 'exfumador':exfumador, 'fumadorPasivo':fumadorPasivo, 'consumoExposicion':consumoExposicion, 'alcohol':alcohol, 'cantidadXsem':cantidadXsem, 'tiempoDeConsumo':tiempoDeConsumo, 'exalcoholico':exalcoholico, 'AlcoholicOcasional':AlcoholicOcasional, 'alergias':alergias, 'queAlergias':queAlergias, 'tipoSangre':tipoSangre, 'farmacodependencia':farmacodependencia,  'farmacoTiempo':farmacoTiempo, 'observaciones':observaciones, 'enfermedadesInfancia':enfermedadesInfancia, 'secuelas':secuelas, 'padeinfa':padeinfa, 'parasin':parasin, 'neurologico':neurologico, 'fiebrereuma':fiebrereuma, 'tuberculosis':tuberculosis, 'diabemelitus':diabemelitus, 'fiebreuptiva':fiebreuptiva, 'parodiepi':parodiepi, 'enfermavene':enfermavene,  'tifoidea':tifoidea, 'mentales':mentales, 'inmunalergi':inmunalergi, 'vasculares':vasculares,  'malforcon':malforcon, 'diarreas':diarreas, 'difteria':difteria, 'artropatias':artropatias,  'hipertension':hipertension, 'exporadia':exporadia, 'paludismo':paludismo, 'sifilisov':sifilisov, 'meningitis':meningitis,  'polio':polio, 'otrospad':otrospad, 'traumaciru':traumaciru, 'Inmualertrans':Inmualertrans, 'nombreu':st.session_state['nombreu'], 'cedulau':st.session_state['cedulau']}, clave)


def update_reg_dattestbib(estudiob1, nivCertBib1, estudiob2, nivCertBib2, estudiob3, nivCertBib3, estudiob4, nivCertBib4, otrosEstudiosBiblicos):
    st.write('update_reg_dattestbib')
    st.write(estudiob1, nivCertBib1, estudiob2, nivCertBib2, estudiob3, nivCertBib3, estudiob4, nivCertBib4, otrosEstudiosBiblicos)
    encprof.update({'estudiob1':estudiob1, 'nivCertBib1':nivCertBib1, 'estudiob2':estudiob2, 'nivCertBib2':nivCertBib2, 'estudiob3':estudiob3, 'nivCertBib3':nivCertBib3, 'estudiob4':estudiob4, 'nivCertBib4':nivCertBib4, 'otrosEstudiosBiblicos':otrosEstudiosBiblicos, 'nombreu':st.session_state['nombreu'], 'cedulau':st.session_state['cedulau']}, clave)


st.header('Encuesta del Pastorado ASIGLEH 2023')
st.subheader('Iglesia de Los Hermanos - Venezuela')
st.text('Ficha de Registro')

nombreu = st.session_state['nombreu']
cedulau = st.session_state['cedulau']
clave = st.session_state['clave']
rol = st.session_state['rol']
clavei = nombreu+'_'+cedulau
st.write('Bienvenido '+clavei+'    -    '+clave+'  <->  '+rol)
# with st.form(key='formliderAPTA'):
with st.expander('Datos Personales'):
    with st.form(key='datper'):
        nombre = st.text_input('Nombres ---- Obligatorio', placeholder='Nombres')
        apellido = st.text_input('Apellidos    ----   Obligatorio', placeholder='Apellidos')
        tlf1 = st.text_input('Número de teléfono   ---- Obligatorio', placeholder='Teléfono')
        celular = st.text_input('Número de celular', placeholder='# del Celular')
        email = st.text_input('Correo electrónico principal')
        whatsapp = st.text_input('WhatsApp')
        faceb = st.text_input('Facebook')
        instg = st.text_input('Instagram')
        twitter = st.text_input('Twitter')
        direccion = st.text_input('Dirección')
        Edo_Civil = st.selectbox('Estado Civil',['Soltero','Casado','Viudo','Otro'])
        #fecnac = st.date_input('Fecha de nacimiento',min_value=datetime.date(1940,1,1))
        edad = st.slider('Edad')
        
        st.write('---')
        guarda01 = st.form_submit_button('Guardar')
        if guarda01:
            st.write('---guardando Datos Personales---')
            update_reg_datper(nombre, tlf1, celular, email, whatsapp, faceb, instg, twitter, direccion, Edo_Civil, edad)


with st.expander('Datos de la iglesia/ministerio que pastorea o desempeña'):
    with st.form(key='datigle'):
        iglesia = st.text_input('Iglesia/Ministerio')
        DireccionIglesia = st.text_input('Dirección física de la Iglesia/Ministerio')
        st.write('---')
        guarda02 = st.form_submit_button('Guardar')
        if guarda02:
            st.write('---guardando Datos de la iglesia---')
            update_reg_datigle(iglesia,  DireccionIglesia)

with st.expander('Datos académicos'):
    with st.form(key='datacade'):
        marca_de_estudios = st.multiselect(label='Selecciona el nivel de estudios completados ó en curso ', options=['Ninguno', 'Primaria', 'Secundaria', 'Técnico Medio', 'Técnico Universitario', 'Pregrado Universitario', 'PostGrado Universitario'], default='Ninguno')
        st.write('Introduce los estudios académicos realizados o en curso, junto con el título o certificado obtenido')
        estudio1 = st.text_input('Estudios realizados ó en curso', key='est1')
        certifi1 = st.text_input('Certificado/Título', key='cert1')
        estudio2 = st.text_input('Estudios realizados ó en curso', key='est2')
        certifi2 = st.text_input('Certificado/Título', key='cert2')
        estudio3 = st.text_input('Estudios realizados ó en curso', key='est3')
        certifi3 = st.text_input('Certificado/Título', key='cert3')
        estudio4 = st.text_input('Estudios realizados ó en curso', key='est4')
        certifi4 = st.text_input('Certificado/Título', key='cert4')
        estudio5 = st.text_input('Estudios realizados ó en curso', key='est5')
        certifi5 = st.text_input('Certificado/Título', key='cert5')
        
        otrosEstudiosAcademicos = st.text_area('Escriba información adicional sobre otros estudios académicos realizados ó en proceso','''   ----   ''')
        st.write('---')
        guarda03 = st.form_submit_button('Guardar')
        if guarda03:
            st.write('---guardando Datos académicos---')
            st.write(marca_de_estudios, estudio1, certifi1, estudio2, certifi2, estudio3, certifi3, estudio4, certifi4, estudio5, certifi5, otrosEstudiosAcademicos)
            update_reg_datacade(marca_de_estudios, estudio1, certifi1, estudio2, certifi2, estudio3, certifi3, estudio4, certifi4, estudio5, certifi5, otrosEstudiosAcademicos)

with st.expander('Datos sobre participación en los ministerios de su iglesia'):
    with st.form(key='datparig'):
        # cargoIgle =st.text_input('Cargo actual en la iglesia')
        st.write('Ministerios en los cuales como pastor, asisto y participo en mi iglesia actualmente')
        min_damas = st.select_slider(label="Ministerio/Departamento de Damas", options=["ninguna","asisto","participo","líder"])
        min_caba = st.select_slider(label="Ministerio/Departamento de Caballeros",options=["ninguna","asisto","participo","líder"])
        min_diaco = st.select_slider("Ministerio/Departamento de Diáconos ó Protocolo",options=["ninguna","asisto","participo","líder"])
        min_jov = st.select_slider("Ministerio de Jovenes",options=["ninguna","asisto","participo","líder"])
        min_ados = st.select_slider("Ministerio/Departamento de Adolescentes",options=["ninguna","asisto","participo","lider"])
        min_ninos = st.select_slider("Ministerio/Departamento de Niños",options=["ninguna","asisto","participo","líder"])
        min_aa = st.select_slider("Ministerio/Departamento de Alabanza",options=["ninguna","asisto","participo","líder"])
        min_fami = st.select_slider("Ministerio/Departamento de Familia ó Matrimonios",options=["ninguna","asisto","participo","líder"])
        min_misio = st.select_slider("Ministerio-Departamento de Misiones",options=["ninguna","asisto","participo","líder"])
        min_celu = st.select_slider("Ministerio/Departamento de Células",options=["ninguna","asisto","participo","líder"])
        min_ense = st.select_slider("Ministerio/Departamento de Enseñanza ó Educación",options=["ninguna","asisto","participo","líder"])
        min_prof = st.select_slider("Ministerio/Departamento de Profesionales",options=["ninguna","asisto","participo","líder"])
        otrosMin = st.text_area('Otros Ministerios', '''  ''')
        st.write('---')
        guarda04 = st.form_submit_button('Guardar')
        if guarda04:
            st.write('---guardando Datos sobre su participación en la iglesia---')
            st.write(min_damas, min_caba, min_diaco, min_jov, min_ados, min_ninos,  min_aa, min_fami, min_misio, min_celu, min_ense, min_prof, otrosMin)
            update_reg_datminigle(min_damas, min_caba, min_diaco, min_jov, min_ados, min_ninos,  min_aa, min_fami, min_misio, min_celu, min_ense, min_prof, otrosMin)

with st.expander('Datos sobre su trabajo ministerial'):
    with st.form(key='dattrab'):
        col1, col2 = st.columns(2)
        #cargo1=st.container()
        minist_1 = st.text_input('Ministerio desempeñado ó actual', key='minist1')
        orgigle_1 = st.text_input('Iglesia / Organización / Departamento ó Ministerio', key='iglem1')
        tiempominist_1 = st.slider(label='Tiempo en dicho ministerio (Desde - Hasta)', key='timem1', min_value=1950, max_value=2023, value=(1990, 2010))
        descripmin_1 = st.text_area('Breve descripción del trabajo desempeñado', key='descri1')
        st.write('---')
        minist_2 = st.text_input('Ministerio desempeñado ó actual', key='minist2')
        orgigle_2 = st.text_input('Iglesia / Organización / Departamento ó Ministerio', key='iglem2')
        tiempominist_2 = st.slider(label='Tiempo en dicho ministerio (Desde - Hasta)', key='timem2', min_value=1950, max_value=2023, value=(1990, 2010))
        descripmin_2 = st.text_area('Breve descripción del trabajo desempeñado', key='descri2')
        st.write('---')
        minist_3 = st.text_input('Ministerio desempeñado ó actual', key='minist3')
        orgigle_3 = st.text_input('Iglesia / Organización / Departamento ó Ministerio', key='iglem3')
        tiempominist_3 = st.slider(label='Tiempo en dicho ministerio (Desde - Hasta)', key='timem3', min_value=1950, max_value=2023, value=(1990, 2010))
        descripmin_3 = st.text_area('Breve descripción del trabajo desempeñado', key='descri3')
        st.write('---')
        minist_4 = st.text_input('Ministerio desempeñado ó actual', key='minist4')
        orgigle_4 = st.text_input('Iglesia / Organización / Departamento ó Ministerio', key='iglem4')
        tiempominist_4 = st.slider(label='Tiempo en dicho ministerio (Desde - Hasta)', key='timem4', min_value=1950, max_value=2023, value=(1990, 2010))
        descripmin_4 = st.text_area('Breve descripción del trabajo desempeñado', key='descri4')
        st.write('---')
        minist_5 = st.text_input('Ministerio desempeñado ó actual', key='minist5')
        orgigle_5 = st.text_input('Iglesia / Organización / Departamento ó Ministerio', key='iglem5')
        tiempominist_5 = st.slider(label='Tiempo en dicho ministerio (Desde - Hasta)', key='timem5', min_value=1950, max_value=2023, value=(1990, 2010))
        descripmin_5 = st.text_area('Breve descripción del trabajo desempeñado', key='descri5')
        st.write('---')
        
        otrostrabmin = st.text_area('Ingrese información adicional sobre otros trabajos ministeriales realizados o en curso',''' -----''')
        st.write('---')
        guarda05 = st.form_submit_button('Guardar')
        if guarda05:
            st.write('---guardando Datos sobre su trabajo ministerial---')
            st.write(minist_1, orgigle_1, tiempominist_1, descripmin_1, minist_2, orgigle_2, tiempominist_2, descripmin_2, minist_3, orgigle_3, tiempominist_3, descripmin_3, minist_4, orgigle_4, tiempominist_4, descripmin_4, minist_5, orgigle_5, tiempominist_5, descripmin_5, otrostrabmin)
            update_reg_dattrabmini(minist_1, orgigle_1, tiempominist_1, descripmin_1, minist_2, orgigle_2, tiempominist_2, descripmin_2, minist_3, orgigle_3, tiempominist_3, descripmin_3, minist_4, orgigle_4, tiempominist_4, descripmin_4, minist_5, orgigle_5, tiempominist_5, descripmin_5, otrostrabmin)

with st.expander('Datos acerca de su testimonio'):
    with st.form(key='dattesti'):
        fec_conversion = st.date_input('Fecha de Conversión', min_value=datetime.date(1940,1,1))
        fec_bautismo_agua = st.date_input('Fecha de Bautismo en agua', min_value=datetime.date(1940,1,1))
        fec_bautismo_Espiritu = st.date_input('Fecha de Bautismo en el Espiritu Santo', min_value=datetime.date(1940,1,1))
        testimonio = st.text_area('Compártenos tu testimonio de salvación', '''  ''')
        st.write('---')
        llamado = st.text_area('Compártenos tu testimonio acerca de tu llamado ministerial. ¿Cómo, cuándo y dónde  inició su ministerio?', '''  ''')
        st.write('---')
        guarda06 = st.form_submit_button('Guardar')
        if guarda06:
            st.write('---guardando Datos sobre su testimonio---')
            st.write(fec_conversion, fec_bautismo_agua, fec_bautismo_Espiritu, testimonio, llamado)
            update_reg_dattestimonio(fec_conversion, fec_bautismo_agua, fec_bautismo_Espiritu, testimonio, llamado)

with st.expander('Datos acerca de su salud'):
    with st.form(key='datsalud'):
        st.subheader('Antecedentes NO patológicos')
        tabaq = st.checkbox(label='Tabaquismo', value=False)
        cigarrosSlide = st.slider(label='Cigarros diarios', min_value=0, max_value=100)
        exfumador = st.checkbox(label='Ex-Fumador ', value=False)
        fumadorPasivo = st.checkbox(label='Fumador Pasivo ', value=False)
        consumoExposicion = st.slider('Años de Consumo ó Exposición ', min_value=0, max_value=50)
        st.write('---')
        alcohol = st.checkbox(label='Alcohol ', value=False)
        cantidadXsem = st.slider('Litros de Alcohol por semana ', min_value=0, max_value=50)
        tiempoDeConsumo = st.slider('Años de consumo ', min_value=0, max_value=50)
        exalcoholico = st.checkbox(label='Ex-Alcohólico ', value=False)
        AlcoholicOcasional = st.checkbox(label='Alcohólico Ocasional ', value=False)
        st.write('---')
        alergias = st.checkbox(label='Alergias ', value=False)
        queAlergias = st.text_area(label='¿Cuáles alergias? ')
        st.write('---')
        tipoSangre = st.radio(label='Tipo de Sangre : ', options=['A+','A-','B+','B-','AB+','AB-','O+','O-', 'No se'], horizontal=True)
        st.write('---')
        farmacodependencia = st.checkbox(label='Farmacodependiente ', value=False)
        farmacoTiempo = st.slider(label='Años de consumo', min_value=0, max_value=20)
        observaciones = st.text_input('Observaciones ')
        st.write('---')
        enfermedadesInfancia = st.text_area(label='Enfermedades de la Infancia')
        secuelas = st.text_area(label='Secuelas ')
        st.write('---')
        st.subheader('Antecedentes Personales Patológicos')
        col7, col8, col9 = st.columns(3)
        with col7:
            padeinfa = st.checkbox(label='Padecimientos de infancia', value=False)
            parasin = st.checkbox(label='Parásitos intestinales', value=False)
            neurologico = st.checkbox(label='Neurológicos', value=False)
            fiebrereuma = st.checkbox(label='Fiebre reumática', value=False)
            tuberculosis = st.checkbox(label='Tuberculosis', value=False)
            diabemelitus = st.checkbox(label='Diábetes mellitus', value=False)
            fiebreuptiva = st.checkbox(label='Fiebres eruptivas', value=False)
            parodiepi = st.checkbox(label='Paroditis Epidémica', value=False)
        with col8:
            enfermavene = st.checkbox(label='Enfermedades venéreas', value=False)
            tifoidea = st.checkbox(label='Tifoidea', value=False)
            mentales = st.checkbox(label='Mentales', value=False)
            inmunalergi = st.checkbox(label='Inmuno-alergias e hipersensibilidad', value=False)
            vasculares = st.checkbox(label='Vasculares', value=False)
            malforcon = st.checkbox(label='Malformaciones congénitas', value=False)
            diarreas = st.checkbox(label='Diarreas', value=False)
            difteria = st.checkbox(label='Difteria', value=False)
        with col9:
            artropatias = st.checkbox(label='Artropatías', value=False)
            hipertension = st.checkbox(label='Hipertensión Arterial', value=False)
            exporadia = st.checkbox(label='Exposición a radiación', value=False)
            paludismo = st.checkbox(label='Paludismo', value=False)
            sifilisov = st.checkbox(label='Sífilis y otras enfermedades venéreas', value=False)
            meningitis = st.checkbox(label='Meningitis', value=False)
            polio = st.checkbox(label='Poliomielitis', value=False)
            otrospad = st.checkbox(label='Otros padecimientos de importancia', value=False)
        traumaciru = st.text_area(label='Trumatismos y Cirugías')
        Inmualertrans = st.text_area(label='Inmunizaciones, Alergias y Transfusiones')
        st.write('---')
        guarda07 = st.form_submit_button('Guardar')
        if guarda07:
            st.write('---guardando Datos sobre su salud---')
            st.write(tabaq, cigarrosSlide, exfumador, fumadorPasivo, consumoExposicion, alcohol, cantidadXsem, tiempoDeConsumo, exalcoholico, AlcoholicOcasional, alergias, queAlergias, tipoSangre, farmacodependencia,  farmacoTiempo, observaciones, enfermedadesInfancia, secuelas, padeinfa, parasin, neurologico, fiebrereuma, tuberculosis, diabemelitus, fiebreuptiva, parodiepi, enfermavene,  tifoidea, mentales, inmunalergi, vasculares,  malforcon, diarreas, difteria, artropatias,  hipertension, exporadia, paludismo, sifilisov, meningitis,  polio, otrospad, traumaciru, Inmualertrans)

            update_reg_datsalud(tabaq, cigarrosSlide, exfumador, fumadorPasivo, consumoExposicion, alcohol, cantidadXsem, tiempoDeConsumo, exalcoholico, AlcoholicOcasional, alergias, queAlergias, tipoSangre, farmacodependencia,  farmacoTiempo, observaciones, enfermedadesInfancia, secuelas, padeinfa, parasin, neurologico, fiebrereuma, tuberculosis, diabemelitus, fiebreuptiva, parodiepi, enfermavene,  tifoidea, mentales, inmunalergi, vasculares,  malforcon, diarreas, difteria, artropatias,  hipertension, exporadia, paludismo, sifilisov, meningitis,  polio, otrospad, traumaciru, Inmualertrans)

with st.expander('Datos sobre estudios biblicos'):
    with st.form(key='datestbib'):
        st.write('Estudios discipulares / bíblicos / teológicos (Completados ó en proceso)')
        col5, col6 = st.columns(2)
        with col5:
            estudiob1 = st.text_input('Estudio bíblico realizado ó en curso', key='estb1')
            nivCertBib1 = st.text_input('Nivel actual ó Certificado', key='ncb1')
            estudiob2 = st.text_input('Estudio bíblico realizado ó en curso', key='estb2')
            nivCertBib2 = st.text_input('Nivel actual ó Certificado', key='ncb2')
            estudiob3 = st.text_input('Estudio bíblico realizado ó en curso', key='estb3')
            nivCertBib3 = st.text_input('Nivel actual ó Certificado', key='ncb3')
            estudiob4 = st.text_input('Estudio bíblico realizado ó en curso', key='estb4')
            nivCertBib4 = st.text_input('Nivel actual ó Certificado', key='ncb4')
        otrosEstudiosBiblicos = st.text_area('Escriba información adicional sobre otros estudios discipulares/bíblicos/teológicos realizados','''
        ----''')
        st.write('---')
        guarda08 = st.form_submit_button('Guardar')
        if guarda08:
            st.write('---guardando Datos sobre estudios bíblicos---')
            st.write(estudiob1, nivCertBib1, estudiob2, nivCertBib2, estudiob3, nivCertBib3, estudiob4, nivCertBib4, otrosEstudiosBiblicos)
            update_reg_dattestbib(estudiob1, nivCertBib1, estudiob2, nivCertBib2, estudiob3, nivCertBib3, estudiob4, nivCertBib4, otrosEstudiosBiblicos)

with st.expander('Registro Documental'):
    st.write('''
             A continuación se mostrará la información recopilada hasta el momento
             En algunos casos podrá tomar una foto de los certificados/diplomas/títulos
             que haya obtenido y que servirán como prueba documental-digital.
             Acá es necesario tener un buen acceso a internet para tomar la foto y subirla
             a nuestra base de datos en la nube.
             Recuerde que esta información estará disponible para usted en la nube y que la
             misma será evaluada por el comité evaluador de ASIGLEH en los lapsos establecidos.
             ''')
    st.write('---')
    mostraryregistrar = st.button('Mostrar Informacion Recopilada')
    if mostraryregistrar:
        st.write('---guardando todos los datos y accesando a minfor---')
        # update_reg_datper(nombre, tlf1, celular, email, whatsapp, faceb, instg, twitter, direccion, Edo_Civil, edad)

    

CheckyEnvia = st.button('Enviar Datos')
#CheckyEnvia = st.form_submit_button('Enviar Datos')

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
       # "Pastor": Pastor,
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
       # "Pastor": Pastor,
        "DireccionIglesia": DireccionIglesia,
        "estudio1": estudio1,
        "certifi1": certifi1,
        "estudio2": estudio2,
        "certifi2": certifi2,
        "otrosEstudiosAcademicos": otrosEstudiosAcademicos,
       # "cargoIgle": cargoIgle,
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
    sdf = pd.Series(regdb[0])
    st.write(sdf)
    clave = regdb[0]['key']
    st.session_state['clave'] = clave
    switch_page('salidas')
    
    
volver = st.button('Guardar y salir')
if volver:
    #st.experimental_rerun()
    update_reg_datper(nombre,tlf1,celular,email)
    update_reg_datigle(iglesia,DireccionIglesia)
    update_reg_datacade(marca_de_estudios, estudio1,certifi1,estudio2,certifi2,estudio3,certifi3)
    
    # switch_page('salidas')