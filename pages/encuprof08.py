import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from deta import Deta
import pandas as pd
import datetime
#from streamlit_toggle import st_toggleswitch
from streamlit_toggle import st_toggle_switch
from streamlit_extras.stateful_button import button
from datetime import datetime
#import time

st.set_page_config(
    page_title="Profesionales AD Reg App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",

)

deta = Deta(st.secrets["deta_key"])
encprof = deta.Base('liderapta')
#db_content = encprof.fetch().items
#st.write(db_content)
# st.write(st.session_state['nombreu'])
# st.write(st.session_state['cedulau'])
# st.write('---')
clave = 'apta-'+st.session_state['cedulau']+'-'+st.session_state['nombreu']
registro = encprof.get(clave)
#registro

camposreg = ["nombreu", "cedulau", "Nombres", "Apellidos", "Telefono", "Celular", "email", "Whatsapp", "Facebook", "Instagram", "Twitter", "Direccion", "Edo_Civil", "Edad", "Iglesia", "DireccionIglesia", "Pastor",	"nivestudios","estudio1","certifi1","estudio2","certifi2","estudio3","certifi3","estudio4","certifi4","estudio5","certifi5","otrosEstudiosAcademicos", "cargoIgle", "min_damas", "min_caba", "min_diaco", "min_jov", "min_ados", "min_ninos", "min_aa", "min_fami", "min_misio", "min_celu", "min_ense", "min_prof", "otrosMin",  "cargo_tra_1", "empresa_1",  "cargo_tra_2", "empresa_2",  "cargo_tra_3", "empresa_3",  "cargo_tra_4", "empresa_4",  "cargo_tra_5", "empresa_5",  "otrosc", "fec_conversion", "fec_bautismo_agua", "fec_bautismo_Espiritu", "testimonio", "estudiob1", "nivCertBib1", "estudiob2", "nivCertBib2", "estudiob3", "nivCertBib3", "estudiob4", "nivCertBib4", "otrosEstudiosBiblicos", "categomin", "minist_1", "orgigle_1", "tiempominist_1", "descripmin_1", "minist_2", "orgigle_2", "tiempominist_2", "descripmin_2", "minist_3", "orgigle_3", "tiempominist_3", "descripmin_3", "minist_4", "orgigle_4", "tiempominist_4", "descripmin_4", "minist_5", "orgigle_5", "tiempominist_5", "descripmin_5", "otrostrabmin", "tabaq", "cigarrosSlide", "exfumador", "fumadorPasivo", "consumoExposicion", "alcohol", "cantidadXsem", "tiempoDeConsumo", "exalcoholico", "AlcoholicOcasional", "alergias", "queAlergias", "tipoSangre", "farmacodependencia",  "farmacoTiempo", "observaciones", "enfermedadesInfancia", "secuelas", "padeinfa", "parasin", "neurologico", "fiebrereuma", "tuberculosis", "diabemelitus", "fiebreuptiva", "parodiepi", "enfermavene",  "tifoidea", "mentales", "inmunalergi", "vasculares",  "malforcon", "diarreas", "difteria", "artropatias",  "hipertension", "exporadia", "paludismo", "sifilisov", "meningitis",  "polio", "otrospad", "traumaciru", "Inmualertrans", "dispuestoXAPTA"]

valores={}
for t in camposreg:
    try:
        valores[t] = registro[t]
    except:
        valores[t] = ''
    if valores[t]==None:
        valores[t]=''
try:  #normaliza algunos campos para mostrarlos en la app
    if valores['min_damas']=='': valores['min_damas']='ninguna'
    if valores['min_caba']=='': valores['min_caba']='ninguna'
    if valores['min_diaco']=='': valores['min_diaco']='ninguna'
    if valores['min_jov']=='': valores['min_jov']='ninguna'

    if valores['min_ados']=='': valores['min_ados']='ninguna'
    if valores['min_ninos']=='': valores['min_ninos']='ninguna'
    if valores['min_aa']=='': valores['min_aa']='ninguna'
    if valores['min_fami']=='': valores['min_fami']='ninguna'

    if valores['min_misio']=='': valores['min_misio']='ninguna'
    if valores['min_celu']=='': valores['min_celu']='ninguna'
    if valores['min_ense']=='': valores['min_ense']='ninguna'
    if valores['min_prof']=='': valores['min_prof']='ninguna'
    if valores['fec_conversion']=='': valores['fec_conversion']='10/10/1950' 
    if valores['fec_bautismo_agua']=='': valores['fec_bautismo_agua']='10/10/1950' 
    if valores['fec_bautismo_Espiritu']=='': valores['fec_bautismo_Espiritu']='10/10/1950' 
    if valores['cigarrosSlide']=='': valores['cigarrosSlide']=0
    if valores['consumoExposicion']=='': valores['consumoExposicion']=0
    if valores['cantidadXsem']=='': valores['cantidadXsem']=0
    if valores['tiempoDeConsumo']=='': valores['tiempoDeConsumo']=0
    if valores['tipoSangre']=='': valores['tipoSangre']='No se'
    if valores['farmacoTiempo']=='': valores['farmacoTiempo']=0
    if valores['dispuestoXAPTA']=='': valores['dispuestoXAPTA']=False
except:
    st.write('---')
#st.write( 'valores = ', valores)

def update_reg_datper(nombre, apellido, tlf1, celular, email, Whatsapp, faceb, instg, twitter, direccion, Edo_Civil, edad):
    st.toast('actualizando los datos personales')
    #time.sleep(1)
    #st.write(nombre, apellido, tlf1, celular, email, Whatsapp, faceb, instg, twitter, direccion, Edo_Civil, edad)
    encprof.update({'Nombres': nombre, 'Apellidos': apellido, 'Telefono': tlf1, 'Celular': celular, 'email': email, 'nombreu': st.session_state['nombreu'], 'cedulau': st.session_state['cedulau'], 'Whatsapp': Whatsapp, 'Facebook': faceb, 'Instagram': instg, 'Twitter': twitter, 'Direccion': direccion, 'Edo_Civil': Edo_Civil,'Edad': edad}, clave)
    #time.sleep(1)
    st.toast('Listo', icon='🎉')
    
def update_reg_datigle(iglesia,Pastor,DireccionIglesia):
    st.write('update reg-datigle')
    st.write(iglesia, Pastor, DireccionIglesia)
    encprof.update({'Iglesia': iglesia, 'Pastor': Pastor, 'DireccionIglesia': DireccionIglesia, 'nombreu': st.session_state['nombreu'], 'cedulau': st.session_state['cedulau']}, clave)

def update_reg_datacade(marca_de_estudios, estudio1, certifi1, estudio2,certifi2, estudio3, certifi3, estudio4, certifi4, estudio5,certifi5, otrosEstudiosAcademicos):
    st.write('update reg-datacade')
    st.write(marca_de_estudios, estudio1, certifi1, estudio2, certifi2,estudio3, certifi3, estudio4, certifi4, estudio5,certifi5, otrosEstudiosAcademicos)
    encprof.update({'nivestudios':marca_de_estudios, 'estudio1':estudio1, 'certifi1':certifi1, 'estudio2':estudio2, 'certifi2':certifi2, 'estudio3':estudio3, 'certifi3':certifi3, 'estudio4':estudio4, 'certifi4':certifi4, 'estudio5':estudio5, 'certifi5':certifi5, 'otrosEstudiosAcademicos':otrosEstudiosAcademicos, 'nombreu':st.session_state['nombreu'], 'cedulau':st.session_state['cedulau']}, clave)

def update_reg_datpartmi(cargoIgle, min_damas, min_caba, min_diaco, min_jov, min_ados, min_ninos, min_aa, min_fami, min_misio, min_celu, min_ense, min_prof, otrosMin):
    st.write('update reg_datpartmi')
    st.write(cargoIgle, min_damas, min_caba, min_diaco, min_jov, min_ados, min_ninos, min_aa, min_fami, min_misio, min_celu, min_ense, min_prof, otrosMin)
    encprof.update({"cargoIgle":cargoIgle, "min_damas":min_damas, "min_caba":min_caba, "min_diaco":min_diaco, "min_jov":min_jov, "min_ados":min_ados, "min_ninos":min_ninos, "min_aa":min_aa, "min_fami":min_fami, "min_misio":min_misio, "min_celu":min_celu, "min_ense":min_ense, "min_prof":min_prof, "otrosMin":otrosMin, 'nombreu':st.session_state['nombreu'], 'cedulau':st.session_state['cedulau']}, clave)

def update_reg_dattrab(cargo_tra_1, empresa_1,  cargo_tra_2, empresa_2,  cargo_tra_3, empresa_3,  cargo_tra_4, empresa_4,  cargo_tra_5, empresa_5,  otrosc):
    st.write('update reg_dattrab')
    st.write(cargo_tra_1, empresa_1,  cargo_tra_2, empresa_2,  cargo_tra_3, empresa_3,  cargo_tra_4, empresa_4,  cargo_tra_5, empresa_5,  otrosc)
    encprof.update({"cargo_tra_1":cargo_tra_1, "empresa_1":empresa_1,  "cargo_tra_2":cargo_tra_2, "empresa_2":empresa_2,  "cargo_tra_3":cargo_tra_3, "empresa_3":empresa_3,  "cargo_tra_4":cargo_tra_4, "empresa_4":empresa_4,  "cargo_tra_5":cargo_tra_5, "empresa_5":empresa_5,  "otrosc":otrosc, 'nombreu':st.session_state['nombreu'], 'cedulau':st.session_state['cedulau']}, clave)

def update_reg_dattestimonio(fec_conversion, fec_bautismo_agua, fec_bautismo_Espiritu, testimonio):
    st.write('update reg_dattestimonio')
    st.write(fec_conversion, fec_bautismo_agua, fec_bautismo_Espiritu, testimonio)
    #encprof.update({"fec_conversion":fec_conversion, "fec_bautismo_agua":fec_bautismo_agua, "fec_bautismo_Espiritu":fec_bautismo_Espiritu, "testimonio":testimonio, 'nombreu':st.session_state['nombreu'], 'cedulau':st.session_state['cedulau']}, clave)
    encprof.update({'fec_conversion':fec_conversion.strftime("%d/%m/%Y"), 'fec_bautismo_agua':fec_bautismo_agua.strftime("%d/%m/%Y"), 'fec_bautismo_Espiritu':fec_bautismo_Espiritu.strftime("%d/%m/%Y"), 'testimonio':testimonio, 'nombreu':st.session_state['nombreu'], 'cedulau':st.session_state['cedulau']}, clave)


def update_reg_dattestbib(estudiob1, nivCertBib1, estudiob2, nivCertBib2, estudiob3, nivCertBib3, estudiob4, nivCertBib4, otrosEstudiosBiblicos):
    st.write('update_reg_dattestbib')
    st.write(estudiob1, nivCertBib1, estudiob2, nivCertBib2, estudiob3, nivCertBib3, estudiob4, nivCertBib4, otrosEstudiosBiblicos)
    encprof.update({'estudiob1':estudiob1, 'nivCertBib1':nivCertBib1, 'estudiob2':estudiob2, 'nivCertBib2':nivCertBib2, 'estudiob3':estudiob3, 'nivCertBib3':nivCertBib3, 'estudiob4':estudiob4, 'nivCertBib4':nivCertBib4, 'otrosEstudiosBiblicos':otrosEstudiosBiblicos, 'nombreu':st.session_state['nombreu'], 'cedulau':st.session_state['cedulau']}, clave)

def update_reg_datsalud(tabaq, cigarrosSlide, exfumador, fumadorPasivo, consumoExposicion, alcohol, cantidadXsem, tiempoDeConsumo, exalcoholico, AlcoholicOcasional, alergias, queAlergias, tipoSangre, farmacodependencia,  farmacoTiempo, observaciones, enfermedadesInfancia, secuelas, padeinfa, parasin, neurologico, fiebrereuma, tuberculosis, diabemelitus, fiebreuptiva, parodiepi, enfermavene,  tifoidea, mentales, inmunalergi, vasculares,  malforcon, diarreas, difteria, artropatias,  hipertension, exporadia, paludismo, sifilisov, meningitis,  polio, otrospad, traumaciru, Inmualertrans):
    st.write('update_reg_datsalud')
    st.write(tabaq, cigarrosSlide, exfumador, fumadorPasivo, consumoExposicion, alcohol, cantidadXsem, tiempoDeConsumo, exalcoholico, AlcoholicOcasional, alergias, queAlergias, tipoSangre, farmacodependencia,  farmacoTiempo, observaciones, enfermedadesInfancia, secuelas, padeinfa, parasin, neurologico, fiebrereuma, tuberculosis, diabemelitus, fiebreuptiva, parodiepi, enfermavene,  tifoidea, mentales, inmunalergi, vasculares,  malforcon, diarreas, difteria, artropatias,  hipertension, exporadia, paludismo, sifilisov, meningitis,  polio, otrospad, traumaciru, Inmualertrans)

    encprof.update({'tabaq':tabaq, 'cigarrosSlide':cigarrosSlide, 'exfumador':exfumador, 'fumadorPasivo':fumadorPasivo, 'consumoExposicion':consumoExposicion, 'alcohol':alcohol, 'cantidadXsem':cantidadXsem, 'tiempoDeConsumo':tiempoDeConsumo, 'exalcoholico':exalcoholico, 'AlcoholicOcasional':AlcoholicOcasional, 'alergias':alergias, 'queAlergias':queAlergias, 'tipoSangre':tipoSangre, 'farmacodependencia':farmacodependencia,  'farmacoTiempo':farmacoTiempo, 'observaciones':observaciones, 'enfermedadesInfancia':enfermedadesInfancia, 'secuelas':secuelas, 'padeinfa':padeinfa, 'parasin':parasin, 'neurologico':neurologico, 'fiebrereuma':fiebrereuma, 'tuberculosis':tuberculosis, 'diabemelitus':diabemelitus, 'fiebreuptiva':fiebreuptiva, 'parodiepi':parodiepi, 'enfermavene':enfermavene,  'tifoidea':tifoidea, 'mentales':mentales, 'inmunalergi':inmunalergi, 'vasculares':vasculares,  'malforcon':malforcon, 'diarreas':diarreas, 'difteria':difteria, 'artropatias':artropatias,  'hipertension':hipertension, 'exporadia':exporadia, 'paludismo':paludismo, 'sifilisov':sifilisov, 'meningitis':meningitis,  'polio':polio, 'otrospad':otrospad, 'traumaciru':traumaciru, 'Inmualertrans':Inmualertrans, 'nombreu':st.session_state['nombreu'], 'cedulau':st.session_state['cedulau']}, clave)

def update_reg_datadispuesto(dispuesto):
    st.write('---> dispuesto a trabajar en APTA: ', dispuesto)
    encprof.update({'dispuestoXAPTA':dispuesto, 'nombreu':st.session_state['nombreu'], 'cedulau':st.session_state['cedulau']}, clave)



st.header('Encuesta de Liderazgo Eclesial de las Asambleas de Dios 2023')
st.subheader('Distrito Andino - Zona 1')
st.write('Elaborado por APTA - Dtto Andino')
st.text('Ficha de Registro')
#st.text('Bienvenido usuario : '+ st.session_state['nombreu'])
msgBienv = "<h4 style='text-align: left; color: orange;'>Bienvenido usuario : "+ st.session_state['nombreu'] + " </h4>"
#msgBienv
st.markdown(msgBienv, unsafe_allow_html=True)


# with st.form(key='formliderAPTA'):
with st.expander('Datos Personales'):
    with st.form(key='datper'):
        nombre = st.text_input('Nombres ', value=valores["Nombres"], placeholder='Nombres')
        apellido = st.text_input('Apellidos    ', value=valores["Apellidos"], placeholder="Apellidos")
        tlf1 = st.text_input('Número de teléfono  ', value=valores["Telefono"],placeholder='Teléfono')
        celular = st.text_input('Número de celular', value=valores["Celular"],placeholder='# del Celular')
        email = st.text_input('Correo electrónico principal', value=valores["email"],)
        #st.write('WhatsApp = ', valores['Whatsapp'])
        Whatsapp = st.text_input('Whatsapp', value=valores["Whatsapp"],)
        faceb = st.text_input('Facebook', value=valores["Facebook"],)
        instg = st.text_input('Instagram', value=valores["Instagram"],)
        twitter = st.text_input('Twitter', value=valores["Twitter"],)
        direccion = st.text_input('Dirección', value=valores["Direccion"],)
        if valores['Edo_Civil']!='':
            indEdo_Civil = ['Soltero','Casado','Viudo','Otro'].index(valores['Edo_Civil'])
            Edo_Civil = st.selectbox('Estado Civil',['Soltero','Casado','Viudo','Otro'], index=indEdo_Civil)
        else:
            Edo_Civil = st.selectbox('Estado Civil',['Soltero','Casado','Viudo','Otro'])
        #fecnac = st.date_input('Fecha de nacimiento',min_value=datetime.date(1940,1,1))
        if valores['Edad']!='':
            edad = st.slider('Edad', value=valores['Edad'])
        else:
            edad = st.slider('Edad')

        st.write('---')
        guarda01 = st.form_submit_button('Guardar')
        if guarda01:
            #st.write('---guardando Datos Personales---')
            #st.write(nombre, apellido, tlf1, celular, email, Whatsapp, faceb, instg, twitter, direccion, Edo_Civil, edad)
            update_reg_datper(nombre, apellido, tlf1, celular, email, Whatsapp, faceb, instg, twitter, direccion, Edo_Civil, edad)
            st.toast('Los Datos fueron actualizados')

with st.expander('Datos de la iglesia a la que asiste'):
    with st.form(key='datigle'):
        iglesia = st.text_input('Nombre de la iglesia a la cuál asiste', value=valores["Iglesia"])
        Pastor = st.text_input('Nombre del pastor de la iglesia a la cuál asiste', value=valores["Pastor"])
        DireccionIglesia = st.text_input('Dirección de la iglesia a la cuál asiste', value=valores["DireccionIglesia"])
        st.write('---')
        guarda02 = st.form_submit_button('Guardar')
        if guarda02:
            st.write('---guardando Datos de la iglesia---')
            update_reg_datigle(iglesia, Pastor, DireccionIglesia)

with st.expander('Datos académicos'):
    with st.form(key='datacade'):
        if valores["nivestudios"]!='':
            marca_de_estudios = st.multiselect(label='Selecciona el nivel de estudios completados ó en curso ', options=['Ninguno', 'Primaria', 'Secundaria', 'Técnico Medio', 'Técnico Universitario', 'Pregrado Universitario', 'PostGrado Universitario'], default=valores["nivestudios"])
        else:
            marca_de_estudios = st.multiselect(label='Selecciona el nivel de estudios completados ó en curso ', options=['Ninguno', 'Primaria', 'Secundaria', 'Técnico Medio', 'Técnico Universitario', 'Pregrado Universitario', 'PostGrado Universitario'], default="Ninguno")
        st.write('Introduce los estudios académicos realizados o en curso, junto con el título o certificado obtenido')
       

        estudio1 = st.text_input('Estudios realizados ó en curso', key='est1', value=valores['estudio1'])
        certifi1 = st.text_input('Certificado/Título', key='cert1', value=valores['certifi1'])
        estudio2 = st.text_input('Estudios realizados ó en curso', key='est2', value=valores['estudio2'])
        certifi2 = st.text_input('Certificado/Título', key='cert2', value=valores['certifi2'])
        estudio3 = st.text_input('Estudios realizados ó en curso', key='est3', value=valores['estudio3'])
        certifi3 = st.text_input('Certificado/Título', key='cert3', value=valores['certifi3'])
        estudio4 = st.text_input('Estudios realizados ó en curso', key='est4', value=valores['estudio4'])
        certifi4 = st.text_input('Certificado/Título', key='cert4', value=valores['certifi4'])
        estudio5 = st.text_input('Estudios realizados ó en curso', key='est5', value=valores['estudio5'])
        certifi5 = st.text_input('Certificado/Título', key='cert5', value=valores['certifi5'])
        
        otrosEstudiosAcademicos = st.text_area('Escriba información adicional sobre otros estudios académicos realizados ó en proceso', value=valores['otrosEstudiosAcademicos'])
        st.write('---')
        guarda03 = st.form_submit_button('Guardar')
        if guarda03:
            st.write('---guardando Datos académicos---')
            st.write(marca_de_estudios, estudio1, certifi1, estudio2,certifi2, estudio3, certifi3, estudio4, certifi4, estudio5,certifi5, otrosEstudiosAcademicos)
            update_reg_datacade(marca_de_estudios, estudio1, certifi1, estudio2, certifi2, estudio3, certifi3, estudio4, certifi4, estudio5,certifi5, otrosEstudiosAcademicos)

with st.expander('Datos sobre participación en la iglesia'):
    with st.form(key='datparig'):
        cargoIgle =st.text_input('Cargo actual en la iglesia', value=valores["cargoIgle"])
        st.write('Ministerios en los cuales asisto y participo en mi iglesia')
        min_damas = st.select_slider(label="Ministerio/Departamento de Damas", options=["ninguna","asisto","participo","líder"], value=valores['min_damas'])
        min_caba = st.select_slider(label="Ministerio/Departamento de Caballeros",options=["ninguna","asisto","participo","líder"], value=valores['min_caba'])
        min_diaco = st.select_slider("Ministerio/Departamento de Diáconos ó Protocolo",options=["ninguna","asisto","participo","líder"], value=valores['min_diaco'])
        min_jov = st.select_slider("Ministerio de Jovenes",options=["ninguna","asisto","participo","líder"], value=valores['min_jov'])
        min_ados = st.select_slider("Ministerio/Departamento de Adolescentes",options=["ninguna","asisto","participo","lider"], value=valores['min_ados'])
        min_ninos = st.select_slider("Ministerio/Departamento de Niños",options=["ninguna","asisto","participo","líder"], value=valores['min_ninos'])
        min_aa = st.select_slider("Ministerio/Departamento de Alabanza",options=["ninguna","asisto","participo","líder"], value=valores['min_aa'])
        min_fami = st.select_slider("Ministerio/Departamento de Familia ó Matrimonios",options=["ninguna","asisto","participo","líder"], value=valores['min_fami'])
        min_misio = st.select_slider("Ministerio-Departamento de Misiones",options=["ninguna","asisto","participo","líder"], value=valores['min_misio'])
        min_celu = st.select_slider("Ministerio/Departamento de Células",options=["ninguna","asisto","participo","líder"], value=valores['min_celu'])
        min_ense = st.select_slider("Ministerio/Departamento de Enseñanza ó Educación",options=["ninguna","asisto","participo","líder"], value=valores['min_ense'])
        min_prof = st.select_slider("Ministerio/Departamento de Profesionales",options=["ninguna","asisto","participo","líder"], value=valores['min_prof'])
        otrosMin = st.text_area('Otros Ministerios', value=valores["otrosMin"])
        st.write('---')
        guarda04 = st.form_submit_button('Guardar')
        if guarda04:
            st.write('---guardando Datos sobre su participación en la iglesia---')
            st.write(cargoIgle, min_damas, min_caba, min_diaco, min_jov, min_ados, min_ninos, min_aa, min_fami, min_misio, min_celu, min_ense, min_prof, otrosMin)
            update_reg_datpartmi(cargoIgle, min_damas, min_caba, min_diaco, min_jov, min_ados, min_ninos, min_aa, min_fami, min_misio, min_celu, min_ense, min_prof, otrosMin)

with st.expander('Datos acerca del trabajo'):
    with st.form(key='dattrab'):
        col1, col2 = st.columns(2)
        cargo1=st.container()
        cargo_tra_1 = st.text_input('Cargo desempeñado ó actual', key='cargo1', value=valores['cargo_tra_1'])
        empresa_1 = st.text_input('Empresa/institución', key='emp1', value=valores['empresa_1'])
        cargo_tra_2 = st.text_input('Cargo desempeñado ó actual', key='cargo2', value=valores['cargo_tra_2'])
        empresa_2 = st.text_input('Empresa/institución', key='emp2', value=valores['empresa_2'])
        cargo_tra_3 = st.text_input('Cargo desempeñado ó actual', key='cargo3', value=valores['cargo_tra_3'])
        empresa_3 = st.text_input('Empresa/institución', key='emp3', value=valores['empresa_3'])
        cargo_tra_4 = st.text_input('Cargo desempeñado ó actual', key='cargo4', value=valores['cargo_tra_4'])
        empresa_4 = st.text_input('Empresa/institución', key='emp4', value=valores['empresa_4'])
        cargo_tra_5 = st.text_input('Cargo desempeñado ó actual', key='cargo5', value=valores['cargo_tra_5'])
        empresa_5 = st.text_input('Empresa/institución', key='emp5', value=valores['empresa_5'])
        otrosc = st.text_area('Ingrese información adicional sobre otros cargos/trabajos realizados o en curso', value=valores['otrosc'])
        st.write('---')
        guarda05 = st.form_submit_button('Guardar')
        if guarda05:
            st.write('---guardando Datos sobre su trabajo---')
            st.write(cargo_tra_1, empresa_1,  cargo_tra_2, empresa_2,  cargo_tra_3, empresa_3,  cargo_tra_4, empresa_4,  cargo_tra_5, empresa_5,  otrosc)
            update_reg_dattrab(cargo_tra_1, empresa_1,  cargo_tra_2, empresa_2,  cargo_tra_3, empresa_3,  cargo_tra_4, empresa_4,  cargo_tra_5, empresa_5,  otrosc)


with st.expander('Datos acerca de su testimonio'):
    with st.form(key='dattesti'):
        #fec_conversion = st.date_input('Fecha de Conversión', min_value=datetime.datetime(1940,1,1), value=datetime.strptime(valores['fec_conversion'], "%d/%m/%Y"), max_value=datetime.datetime.now())
        fec_conversion = st.date_input('Fecha de Conversión', format = 'DD/MM/YYYY', value=datetime.strptime(valores['fec_conversion'], "%d/%m/%Y"))
        #fec_bautismo_agua = st.date_input('Fecha de Bautismo en agua', min_value=datetime.date(1940,1,1), value=datetime.datetime.strptime(valores['fec_bautismo_agua'], "%d/%m/%Y"), max_value=datetime.datetime.now())
        fec_bautismo_agua = st.date_input('Fecha de Bautismo en agua', format = 'DD/MM/YYYY',)
        fec_bautismo_Espiritu = st.date_input('Fecha de Bautismo en el Espíritu Santo', format = 'DD/MM/YYYY',)
        #fec_bautismo_Espiritu = st.date_input('Fecha de Bautismo en el Espiritu Santo', min_value=datetime.date(1940,1,1), value=datetime.datetime.strptime(valores['fec_bautismo_Espiritu'], "%d/%m/%Y"), max_value=datetime.datetime.now())
        testimonio = st.text_area('Compártenos tu testimonio de salvación', value=valores['testimonio'])
        st.write('---')

        guarda06 = st.form_submit_button('Guardar')
        if guarda06:
            st.write('---guardando Datos sobre su testimonio---')
            st.write(fec_conversion, fec_bautismo_agua, fec_bautismo_Espiritu, testimonio)
            update_reg_dattestimonio(fec_conversion, fec_bautismo_agua, fec_bautismo_Espiritu, testimonio)

with st.expander('Datos sobre estudios biblicos'):
    with st.form(key='datestbib'):
        st.write('Estudios discipulares / bíblicos / teológicos (Completados ó en proceso)')
        col5, col6 = st.columns(2)
        with col5:
            estudiob1 = st.text_input('Estudio bíblico realizado ó en curso', key='estb1', value=valores['estudiob1'])
            nivCertBib1 = st.text_input('Nivel actual ó Certificado', key='ncb1',value=valores['nivCertBib1'])
            estudiob2 = st.text_input('Estudio bíblico realizado ó en curso', key='estb2', value=valores['estudiob2'])
            nivCertBib2 = st.text_input('Nivel actual ó Certificado', key='ncb2', value=valores['nivCertBib2'])
            estudiob3 = st.text_input('Estudio bíblico realizado ó en curso', key='estb3', value=valores['estudiob3'])
            nivCertBib3 = st.text_input('Nivel actual ó Certificado', key='ncb3', value=valores['nivCertBib3'])
            estudiob4 = st.text_input('Estudio bíblico realizado ó en curso', key='estb4', value=valores['estudiob4'])
            nivCertBib4 = st.text_input('Nivel actual ó Certificado', key='ncb4', value=valores['nivCertBib4'])
        otrosEstudiosBiblicos = st.text_area('Escriba información adicional sobre otros estudios discipulares/bíblicos/teológicos realizados', value=valores['otrosEstudiosBiblicos'])
        st.write('---')
        guarda08 = st.form_submit_button('Guardar')
        if guarda08:
            st.write('---guardando Datos sobre estudios bíblicos---')
            try:
                if estudio1==None: estudio1=''
                if estudio2==None: estudio2=''
                if estudio3==None: estudio3=''
                if estudio4==None: estudio4=''
                if nivCertBib1==None: nivCertBib1=''
                if nivCertBib2==None: nivCertBib2=''
                if nivCertBib3==None: nivCertBib3=''
                if nivCertBib4==None: nivCertBib4=''
                if otrosEstudiosBiblicos==None: otrosEstudiosBiblicos=''
            except:
                st.write('---')
            st.write(estudiob1, nivCertBib1, estudiob2, nivCertBib2, estudiob3, nivCertBib3, estudiob4, nivCertBib4, otrosEstudiosBiblicos)
            update_reg_dattestbib(estudiob1, nivCertBib1, estudiob2, nivCertBib2, estudiob3, nivCertBib3, estudiob4, nivCertBib4, otrosEstudiosBiblicos)

with st.expander('Datos acerca de su salud'):
    with st.form(key='datsalud'):
        st.subheader('Antecedentes NO patológicos')
        tabaq = st.checkbox(label='Tabaquismo', value=valores['tabaq'])
        cigarrosSlide = st.slider(label='Cigarros diarios', min_value=0, max_value=100, value=valores['cigarrosSlide'])
        exfumador = st.checkbox(label='Ex-Fumador ', value=valores['exfumador'])
        fumadorPasivo = st.checkbox(label='Fumador Pasivo ', value=valores['fumadorPasivo'])
        consumoExposicion = st.slider('Años de Consumo ó Exposición ', min_value=0, max_value=50, value=valores['consumoExposicion'])
        st.write('---')
        alcohol = st.checkbox(label='Alcohol ', value=valores['alcohol'])
        cantidadXsem = st.slider('Litros de Alcohol por semana ', min_value=0, max_value=50, value=valores['cantidadXsem'])
        tiempoDeConsumo = st.slider('Años de consumo ', min_value=0, max_value=50, value=valores['tiempoDeConsumo'])
        exalcoholico = st.checkbox(label='Ex-Alcohólico ', value=valores['exalcoholico'])
        AlcoholicOcasional = st.checkbox(label='Alcohólico Ocasional ', value=valores['AlcoholicOcasional'])
        st.write('---')
        alergias = st.checkbox(label='Alergias ', value=valores['alergias'])
        queAlergias = st.text_area(label='¿Cuáles alergias? ', value=valores['queAlergias'])
        st.write('---')
        indtipoSangre = ['A+','A-','B+','B-','AB+','AB-','O+','O-', 'No se'].index(valores['tipoSangre'])
        tipoSangre = st.radio(label='Tipo de Sangre : ', options=['A+','A-','B+','B-','AB+','AB-','O+','O-', 'No se'], horizontal=True, index=indtipoSangre)
        st.write('---')
        farmacodependencia = st.checkbox(label='Farmacodependiente ', value=valores['farmacodependencia'])
        farmacoTiempo = st.slider(label='Años de consumo', min_value=0, max_value=20, value=valores['farmacoTiempo'])
        observaciones = st.text_input('Observaciones ', value='observaciones')
        st.write('---')
        enfermedadesInfancia = st.text_area(label='Enfermedades de la Infancia', value=valores['enfermedadesInfancia'])
        secuelas = st.text_area(label='Secuelas ', value=valores['secuelas'])
        st.write('---')
        st.subheader('Antecedentes Personales Patológicos')
        col7, col8, col9 = st.columns(3)
        with col7:
            padeinfa = st.checkbox(label='Padecimientos de infancia', value=valores['padeinfa'])
            parasin = st.checkbox(label='Parásitos intestinales', value=valores['parasin'])
            neurologico = st.checkbox(label='Neurológicos', value=valores['neurologico'])
            fiebrereuma = st.checkbox(label='Fiebre reumática', value=valores['fiebrereuma'])
            tuberculosis = st.checkbox(label='Tuberculosis', value=valores['tuberculosis'])
            diabemelitus = st.checkbox(label='Diábetes mellitus', value=valores['diabemelitus'])
            fiebreuptiva = st.checkbox(label='Fiebres eruptivas', value=valores['fiebreuptiva'])
            parodiepi = st.checkbox(label='Paroditis Epidémica', value=valores['parodiepi'])
        with col8:
            enfermavene = st.checkbox(label='Enfermedades venéreas', value=valores['enfermavene'])
            tifoidea = st.checkbox(label='Tifoidea', value=valores['tifoidea'])
            mentales = st.checkbox(label='Mentales', value=valores['mentales'])
            inmunalergi = st.checkbox(label='Inmuno-alergias e hipersensibilidad', value=valores['inmunalergi'])
            vasculares = st.checkbox(label='Vasculares', value=valores['vasculares'])
            malforcon = st.checkbox(label='Malformaciones congénitas', value=valores['malforcon'])
            diarreas = st.checkbox(label='Diarreas', value=valores['diarreas'])
            difteria = st.checkbox(label='Difteria', value=valores['difteria'])
        with col9:
            artropatias = st.checkbox(label='Artropatías', value=valores['artropatias'])
            hipertension = st.checkbox(label='Hipertensión Arterial', value=valores['hipertension'])
            exporadia = st.checkbox(label='Exposición a radiación', value=valores['exporadia'])
            paludismo = st.checkbox(label='Paludismo', value=valores['paludismo'])
            sifilisov = st.checkbox(label='Sífilis y otras enfermedades venéreas', value=valores['sifilisov'])
            meningitis = st.checkbox(label='Meningitis', value=valores['meningitis'])
            polio = st.checkbox(label='Poliomielitis', value=valores['polio'])
            otrospad = st.checkbox(label='Otros padecimientos de importancia', value=valores['otrospad'])
        traumaciru = st.text_area(label='Trumatismos y Cirugías', value=valores['traumaciru'])
        Inmualertrans = st.text_area(label='Inmunizaciones, Alergias y Transfusiones', value=valores['Inmualertrans'])

        st.write('---')
        guarda07 = st.form_submit_button('Guardar')
        if guarda07:
            st.write('---guardando Datos sobre su salud---')
            st.write(tabaq, cigarrosSlide, exfumador, fumadorPasivo, consumoExposicion, alcohol, cantidadXsem, tiempoDeConsumo, exalcoholico, AlcoholicOcasional, alergias, queAlergias, tipoSangre, farmacodependencia,  farmacoTiempo, observaciones, enfermedadesInfancia, secuelas, padeinfa, parasin, neurologico, fiebrereuma, tuberculosis, diabemelitus, fiebreuptiva, parodiepi, enfermavene,  tifoidea, mentales, inmunalergi, vasculares,  malforcon, diarreas, difteria, artropatias,  hipertension, exporadia, paludismo, sifilisov, meningitis,  polio, otrospad, traumaciru, Inmualertrans)

            update_reg_datsalud(tabaq, cigarrosSlide, exfumador, fumadorPasivo, consumoExposicion, alcohol, cantidadXsem, tiempoDeConsumo, exalcoholico, AlcoholicOcasional, alergias, queAlergias, tipoSangre, farmacodependencia,  farmacoTiempo, observaciones, enfermedadesInfancia, secuelas, padeinfa, parasin, neurologico, fiebrereuma, tuberculosis, diabemelitus, fiebreuptiva, parodiepi, enfermavene,  tifoidea, mentales, inmunalergi, vasculares,  malforcon, diarreas, difteria, artropatias,  hipertension, exporadia, paludismo, sifilisov, meningitis,  polio, otrospad, traumaciru, Inmualertrans)


if valores['dispuestoXAPTA']:
    st.success('Dios te bendiga. Sabemos que estás dispuesto a trabajar con APTA. Pronto te estaremos contactando')
else:
    preclave1 = st.checkbox('¿Estarías dispuesto a servir al Señor con tus talentos y profesión en el Departamento de Profesionales y Técnicos de las Asambleas de Dios en el distrito Andino?')

    if preclave1:
        st.success('Genial. Te estaremos contactando a ti y a tu pastor para conversar acerca del tema')
        st.success('Que Dios te bendiga')
        dispuesto = True
        update_reg_datadispuesto(dispuesto)

# CheckyEnvia = st.button('Enviar Datos')
# #CheckyEnvia = st.form_submit_button('Enviar Datos')

# if CheckyEnvia:
#     st.write('Verificando data')
#     registro = {
#         "nombre": nombre,
#         "tlf1": tlf1,
#         "celular": celular,
#         "email": email,
#         "whatsapp": whatsapp,
#         "faceb": faceb,
#         "instg": "",
#         "twitter": "",
#         "direccion": direccion,
#         "Edo_Civil": Edo_Civil,
#         "edad": edad,
#         "iglesia": iglesia,
#         "Pastor": Pastor,
#         "DireccionIglesia": DireccionIglesia,
#         "estudio1": estudio1,
#         "certifi1": certifi1,
#         "estudio2": estudio2,
#         "certifi2": certifi2,
#         "otrosEstudiosAcademicos": otrosEstudiosAcademicos
#         }
#     #print(otrosEstudiosAcademicos)
#     #st.write(otrosEstudiosAcademicos)
#     #registro
#     st.write('Enviando data')

#     #encprof.put(registro)
#     encprof.put({
#         "nombre": nombre,
#         "tlf1": tlf1,
#         "celular": celular,
#         "email": email,
#         "whatsapp": whatsapp,
#         "faceb": faceb,
#         "instg": "",
#         "twitter": "",
#         "direccion": direccion,
#         "Edo_Civil": Edo_Civil,
#         "edad": edad,
#         "iglesia": iglesia,
#         "Pastor": Pastor,
#         "DireccionIglesia": DireccionIglesia,
#         "estudio1": estudio1,
#         "certifi1": certifi1,
#         "estudio2": estudio2,
#         "certifi2": certifi2,
#         "otrosEstudiosAcademicos": otrosEstudiosAcademicos,
#         "cargoIgle": cargoIgle,
#         "min_damas": min_damas,
#         "min_caba": min_caba,
#         "min_diaco": min_diaco,
#         "min_jov": min_jov,
#         "min_ados": min_ados,
#         "min_ninos": min_ninos,
#         "min_aa": min_aa,
#         "min_fami": min_fami,
#         "min_misio": min_misio,
#         "min_celu": min_celu,
#         "min_ense": min_ense,
#         "min_prof": min_prof,
#         "otrosMin": otrosMin
#         })


#     db_content = encprof.fetch().items
#     regdb = encprof.fetch({"nombre?contains": nombre}).items
#     st.write(regdb)
#     #sdf = pd.Series(registro)
#     sdf = pd.Series(regdb[0])
#     st.write(sdf)
#     clave = regdb[0]['key']
#     st.session_state['clave'] = clave
#     switch_page('salidas')
    
    
volver = st.button('Salir')
if volver:
    #st.experimental_rerun()
    #update_reg_datper(nombre,tlf1,celular,email)
    #update_reg_datigle(iglesia,Pastor,DireccionIglesia)
    #update_reg_datacade(marca_de_estudios, estudio1,certifi1,estudio2,certifi2,estudio3,certifi3)
    
    switch_page('login01')
