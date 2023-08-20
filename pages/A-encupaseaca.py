
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from deta import Deta

st.set_page_config(
    page_title="ASIGLEH app",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",

)

def abrerecursosdeta():
    deta = Deta(st.secrets["deta_key"])
    encuasigleh = deta.Base('asiglehpastores')
    photos = deta.Drive(name='asiglehphotos')
    photosys = deta.Drive(name='modphotos')
    return(encuasigleh, photos, photosys)


newvalea=[]
param1 = ''

def dnewXitem(item, vals, contador):
    st.write('dnewXitem : ', item, vals, contador)
    if contador == 1:
        st.write('***')
        newcont = st.container()
        with newcont:
            for vl in vals:
                tik = vl[0]
                btk = 'btn-'+vl[0]
                param1 = st.text_input(label=vl[2], key=tik)
                newvalea.append({tik:param1})
        st.write('***')
    if contador == 2:
        st.write('***')
        newcont = st.container()
        with newcont:
            for vl in vals:
                #'vl = ',vl
                tik = vl[0]
                btk = 'btn-'+vl[0]
                if vl[1]=='texto': param1 = st.text_input(label=vl[2], key=tik)
                elif vl[1]=='slider1': param1 = st.select_slider(label=vl[2], key='sl'+tik, options=['ninguna', 'asisto', 'participo', 'lider'])
                else: param1 = st.text_area(label=vl[2], key='ta-'+tik)

                newvalea.append({tik:param1})
    if contador == 3:
        st.write('***')
        newcont = st.container()
        with newcont:
            for vl in vals:
                #'vl = ',vl
                tik = vl[0]
                btk = 'btn-'+vl[0]
                if vl[1]=='texto': param1 = st.text_input(label=vl[2], key=tik)
                elif vl[1]=='radio': param1 = st.radio(label=vl[2], key='sl'+tik, options=['Lider', 'Asociado', 'Miembro'])
                else: param1 = st.text_area(label=vl[2], key='ta-'+tik)

                newvalea.append({tik:param1})
    if contador == 5:
        st.write('***')
        newcont = st.container()
        with newcont:
            for vl in vals:
                #'vl = ',vl
                tik = vl[0]
                btk = 'btn-'+vl[0]
                if vl[1]=='texto': param1 = st.text_input(label=vl[2], key=tik)
                elif vl[1]=='textarea': param1 = st.text_area(label=vl[2], key='ta-'+tik)
                elif vl[1]=='sliderange': param1 = st.slider(label=vl[2], key='sr-'+tik)
                else:
                    #fotoCerT = clave+'_certea'+tik+'_ima01_si00.png'
                    fotoCerT = 'photo'+tik+'_ima01_si00.png'
                    try:
                        imagenCer = photos.get(fotoCerT)
                        content = imagenCer.read()
                        st.image(content)
                        btcer1 = st.button('Actualizar foto del Certificado de estudio', key='foto-'+btk)
                    except:
                        btcer1 = st.button('Tomar foto del Certificado de estudio', key='foto-'+btk)
                    if btcer1:
                        st.session_state['nameima'] = fotoCerT
                        fotoCerT
                        # st.session_state['clave'] = clave
                        # st.session_state['nombreu'] = nombreu
                        # st.session_state['cedulau'] = cedulau 
                        # switch_page('surtphoto05a')
                    st.write('***')

                newvalea.append({tik:param1})
        #st.write('***')
        #st.write('***')
    bguardar = st.button(label='Guardar', key=btk, use_container_width=True)
    st.write(newvalea)
    return 

def newtexto(datTexto, num):  # datTexto = ['telefonoNro', 'texto', 'Teléfono', '-']
    tik = datTexto[0]+'-'+str(num)
    if datTexto[1]=='texto':
        param = st.text_input(label=datTexto[2], value=datTexto[4], key='keyt-'+tik+datTexto[3])
        newvalea.append({tik:param})
        #st.toast(newvalea)
    if datTexto[1]=='textarea':
        param = st.text_area(label=datTexto[2], value=datTexto[3], key='keyta-'+tik)
        newvalea.append({tik:param})
        #st.toast(newvalea)
    if datTexto[1]=='radio':
        param1 = st.radio(label=datTexto[2], options=datTexto[3], index=0, horizontal=True, key='keyr-'+tik)
        if param1=='Otra': param2 = st.text_input(datTexto[4])
        else: param2 = param1
        param = param2
        newvalea.append({tik:param})
        #st.toast(newvalea)
    if datTexto[1]=='radio + texto':
        param1 = st.radio(label=datTexto[2], options=datTexto[3], index=3, horizontal=True, key='keyrt-'+tik)
        if param1=='Otra': param2 = st.text_input(datTexto[4])
        else: param2 = param1
        if param1 != '-' : idRedS = st.text_input(label='Ingresa tu ID(nombre, teléfono, etc) en la red social')
        else: idRedS='-'
        param = [param2, idRedS]
        newvalea.append({tik:param})
        #st.toast(newvalea)
    if datTexto[1]=='select slider':
        param = st.select_slider(label=datTexto[2], key='keyss-'+tik, options=datTexto[3])
        newvalea.append({tik:param})
        #st.toast(newvalea)
    if datTexto[1]=='range slider':
        param = st.slider(label=datTexto[2], key='keyrs-'+tik, min_value=datTexto[3], max_value=datTexto[4], value=datTexto[5])
        newvalea.append({tik:param})
        #st.toast(newvalea)
    return(newvalea)
    
def estudioBaseA(etiescuela,eticertificadonivelAc, nivel):
    #st.write('****Estudio Base Académico****')
    st.write('***')
    escuelaField = 'escuelaAc#'+str(nivel)
    clavetxtAc = 'escAc1'
    #etiescuela = 'Nombre del colegio/escuela'
    valnewescuelaField = newtexto([escuelaField, 'texto', etiescuela, clavetxtAc, '-'], 1)

    sedeField = 'sedeAc#'+str(nivel)
    clavetxtsede = 'escAcSede1'
    etisedelu = 'Lugar/Sede'
    valnewSedeField = newtexto([sedeField, 'texto', etisedelu, clavetxtsede, '-'], 1)

    namemodoAcField = 'modoAc#'+str(nivel)
    opcionesmodoAc = ['presencial', 'en línea /a distancia', 'híbrido']
    etiquetamodoAc = 'Modalidad de estudio'
    valnewmodoAc = newtexto([namemodoAcField, 'select slider', etiquetamodoAc, opcionesmodoAc], 1)

    tiempoAcField = 'tiempoAc#'+str(nivel)
    etiquetaTiempoAc = 'Tiempo de estudio (Desde...Hasta)'
    minimo = 1960
    maximo = 2023
    desde = 1990
    hasta = 2000
    valnewtiempoAc = newtexto([tiempoAcField, 'range slider', etiquetaTiempoAc, minimo, maximo, (desde, hasta)], 1)

    certificadonivelAcField = 'certificadonivelAc#'+str(nivel)
    clavecerAc = 'certAc1'
    #eticertificadonivelAc = 'Certificado y/o último nivel alcanzado'
    valnewcertificadonivelAcField = newtexto([certificadonivelAcField, 'texto', eticertificadonivelAc, clavecerAc, '-'], 1)


    btfoto = st.checkbox(label='tomar foto')
    if btfoto:
        nombreFoto = 'fotoCertAc'+'##'+str(nivel)+'-clave-ima01-seq01.png'
        st.write('nameFoto = ', nombreFoto)
    
    describeAcField = 'describeAc#'+str(nivel)
    etidescribeAc = 'Breves comentarios sobre la experiencia educativa'
    valor = '-'
    valnewdescribeAcField = newtexto([describeAcField, 'textarea', etidescribeAc, valor], 1)
    return(valnewescuelaField)



def showestudios(cuales):
    if cuales=='Infantil':
        st.caption('se muestran los estudios nivel Básico de Prescolar')
    elif cuales=='Primaria':
        st.caption('se muestran los estudios nivel Básico de Primaria')
    elif cuales=='Secundaria':
        st.caption('se muestran los estudios nivel Media de Secundaria')
    elif cuales=='Técnica(Media)':
        st.caption('se muestran los estudios nivel Media de Técnica(Media)')
    elif cuales=='Técnico Universitario':
        st.caption('se muestran los estudios nivel Superior/Universitario de Técnico Universitario')
    elif cuales=='Pregrado Universitario / Licenciatura':
        st.caption('se muestran los estudios nivel Superior/Universitario de Pregrado Universitario / Licenciatura')
    elif cuales=='Maestría':
        st.caption('se muestran los estudios nivel Superior/Universitario de Maestría')
    elif cuales=='Doctorado':
        st.caption('se muestran los estudios nivel Superior/Universitario de Doctorado')
    elif cuales=='Post-Doctorado':
        st.caption('se muestran los estudios nivel Post-Doctorado')
    elif cuales=='Estudios Transversales':
        st.caption('se muestran los  Estudios Transversales')

lregk = ['nombre', 'apellido']
parametro = 'estudioa'
valis = [x for x in lregk if x.startswith(parametro)]

ncamposreg = []
for t in valis:
    cert = 'certificadoa'+t[8:]
    tiet = 'tiempoea'+t[8:]
    ncamposreg.append(t)
    ncamposreg.append(cert)
    ncamposreg.append(tiet)

nvalores = {}
newXitems = []

st.header('Encuesta del Pastorado ASIGLEH 2023')
st.subheader('Iglesia de Los Hermanos - Venezuela')
st.caption('Ficha de Registro - Estudios Académicos')

encuasigleh, photos, photosys = abrerecursosdeta()

nombreu = st.session_state['nombreu']
cedulau = st.session_state['cedulau']
rol = st.session_state['rol']
clave = st.session_state['clave']

st.caption(nombreu)
st.write('***')
st.subheader(':orange[$\large \\bold{Estudios\, académicos}$]')
st.info('ℹ️ 🙂En esta sección se requiere proveer información de todos los estudios académicos formales realizados en los niveles básico(prescolar y primaria), media(secundaria y técnico medio), superior/universitario(técnico, pre-grado y post-grado) y post-doctorado. Los denominados transversales hacen referencia a todos aquellos con una menor carga académica y/o reconocimiento, por ejemplo, especializaciones y diplomados')
NroEstAca = 0

nivele = st.radio(':orange[$\Large Nivel$]', ['-', 'Básico', 'Media', 'Superior/Universitario', 'Post-Doctorado', 'Estudios Transversales'], horizontal=True, index=0)
if nivele!='-':
    NroEstAca+=1
    if nivele=='Básico':
        cualea = st.radio(':orange[$\large SubNivel$]',['-', 'Infantil - Kinder', 'Primaria'], horizontal=True, index=0)
        if cualea!='-':
            if cualea=='Infantil - Kinder':
                st.write('***')
                st.write(':blue[$ \\bold{Estudios\, Basicos:\, Infantil-Kinder} $]')
                showestudios('Infantil')
                valnewestudio = estudioBaseA('Nombre del kinder/prescolar', 'Último nivel alcanzado y/o certificado-diploma-título obtenido', 10)
            elif cualea=='Primaria':
                st.write('***')
                st.write(':blue[$ \\bold{Estudios\, Basicos:\, Primaria} $]')
                showestudios('Primaria')
                valnewestudio = estudioBaseA('Nombre del colegio/escuela primaria', 'Último nivel alcanzado y/o certificado-diploma-título obtenido', 100)
    elif nivele=='Media':
        cualea = st.radio(':orange[$\large SubNivel$]',['-', 'Secundaria', 'Técnica(Media)'], horizontal=True, index=0)
        if cualea!='-':
            if cualea=='Secundaria':
                st.write('***')
                st.write(':blue[$ \\bold{Estudios\, Medios:\, Secundaria} $]')
                showestudios('Secundaria')
                valnewestudio = estudioBaseA('Nombre del colegio/escuela/instituto donde realizó estudios de secundaria', 'Último nivel alcanzado y/o certificado-diploma-título obtenido', 200)
            elif cualea=='Técnica(Media)':
                st.write('***')
                st.write(':blue[$ \\bold{Estudios\, Medios:\, Técnica(Media)} $]')
                showestudios('Técnica(Media)')
                valnewestudio = estudioBaseA('Nombre del instituto/escuela donde realizó estudios de Técnico Medio', 'Último nivel alcanzado y/o certificado-diploma-título obtenido', 300)
    elif nivele=='Superior/Universitario':
        cualea = st.radio(':orange[$\large SubNivel$]',['-', 'Técnico Universitario', 'Pregrado Universitario / Licenciatura', 'Maestría', 'Doctorado'], horizontal=True, index=0)
        if cualea!='-':
            if cualea=='Técnico Universitario':
                st.write('***')
                st.write(':blue[$ \\bold{Estudios\, Superior/Universitario:\, } $]')
                st.write(':orange[$ \\bold{Técnico Universitario} $]')
                showestudios('Técnico Universitario')
                valnewestudio = estudioBaseA('Nombre de la institución ó universidad donde estudia ó realizó estudios de Técnico Universitario', 'Último nivel alcanzado y/o certificado-diploma-título obtenido', 400)
            elif cualea=='Pregrado Universitario / Licenciatura':
                st.write('***')
                st.write(':blue[$ \\bold{Estudios\, Superior/Universitario:\, } $]')
                st.write(':orange[$ \\bold{Pregrado Universitario / Licenciatura} $]')
                showestudios('Pregrado Universitario / Licenciatura')
                valnewestudio = estudioBaseA('Nombre de la institución ó universidad donde estudia ó realizó estudios de Pregrado Universitario / Licenciatura', 'Último nivel alcanzado y/o certificado-diploma-título obtenido', 500)
            elif cualea=='Maestría':
                st.write('***')
                st.write(':blue[$ \\bold{Estudios\, Superior/Universitario:\, } $]')
                st.write(':orange[$ \\bold{Maestría} $]')
                showestudios('Maestría')
                valnewestudio = estudioBaseA('Nombre de la institución ó universidad donde estudia ó realizó estudios de Maestría', 'Último nivel alcanzado y/o certificado-diploma-título obtenido', 600)
            elif cualea=='Doctorado':
                st.write('***')
                st.write(':blue[$ \\bold{Estudios\, Superior/Universitario: } $]')
                st.write(':orange[$ \\bold{Doctorado} $]')
                showestudios('Doctorado')
                valnewestudio = estudioBaseA('Nombre de la institución ó universidad donde estudia ó  realizó estudios de Doctorado', 'Último nivel alcanzado y/o certificado-diploma-título obtenido', 700)
    elif nivele=='Post-Doctorado':
        st.write('***')
        st.write(':blue[$ \\bold{Estudios\, de\, Post-Doctorado} $]')
        showestudios('Post-Doctorado')
        valnewestudio = estudioBaseA('Nombre de la institución ó universidad donde estudia ó realizó estudios de Post-Doctorado', 'Último nivel alcanzado y/o certificado-diploma-título obtenido', 800)

    elif nivele=='Estudios Transversales':
        st.write('***')
        st.write(':blue[$ \\bold{Estudios\, Transversales} $]')
        showestudios('Estudios Transversales')
        nameETransField = 'nameETrans#'
        clavenameETrans = 'knameETrans1'
        etinameETrans = 'Curso/Estudio'
        valnewnameETransField = newtexto([nameETransField, 'texto', etinameETrans, clavenameETrans, '-'], 1)

        tipoETransField = 'tipoETrans#'
        opcionestipoETrans = ['-', 'Especialización', 'Curso', 'Diplomado', 'Certificación', 'Otra']
        Etiqueta1 = 'Tipo de estudio (ejem: Especialización, Curso, Diplomado, etc)'
        Etiqueta2 = 'Especifique el tipo de estudio'
        valnewtipoETrans = newtexto([tipoETransField, 'radio', Etiqueta1, opcionestipoETrans, Etiqueta2], 1)

        namemodoETransField = 'modoETrans#'
        opcionesmodoETrans = ['presencial', 'en línea /a distancia', 'híbrido']
        etiquetamodoETrans = 'Modalidad de estudio'
        valnewmodoETrans = newtexto([namemodoETransField, 'select slider', etiquetamodoETrans, opcionesmodoETrans], 1)

        institutolugarETransField = 'institutolugarETrans#'
        claveinstitutolugarETrans = 'kinstitutolugarETrans1'
        eticertificadonivelETrans = 'Instituto / Lugar'
        valnewinstitutolugarETransField = newtexto([institutolugarETransField, 'texto', eticertificadonivelETrans, claveinstitutolugarETrans, '-'], 1)

        tiempoETransField = 'tiempoETrans#'
        etiquetaTiempoETrans = 'Tiempo de estudio (Desde...Hasta)'
        minimo = 1980
        maximo = 2023
        desde = 1990
        hasta = 2000
        valnewtiempoEB = newtexto([tiempoETransField, 'range slider', etiquetaTiempoETrans, minimo, maximo, (desde, hasta)], 1)

        certificadonivelETransField = 'certificadonivelETrans#'
        clavecerETrans = 'certETrans1'
        eticertificadonivelETrans = 'Certificado y/o último nivel alcanzado'
        valnewcertificadonivelETransField = newtexto([certificadonivelETransField, 'texto', eticertificadonivelETrans, clavecerETrans, '-'], 1)


        btfoto = st.checkbox(label='tomar foto')
        if btfoto:
            nombreFoto = 'fotoETrans'+'##'+'-clave-ima01-seq01.png'
            st.write('nameFoto = ', nombreFoto)
        
        describeETransField = 'describeETrans#'
        etidescribeETrans = 'Breve descripción de lo aprendido'
        valor = '-'
        valnewdescribeETransField = newtexto([describeETransField, 'textarea', etidescribeETrans, valor], 1)

        # btn = st.button(label='Guardar', key='btnfinal1')
        # if btn:
        #     st.write('se guarda como:', valnewcertificadonivelETransField)
        # st.write('***')

#btn = st.button(label='Guardar / Actualizar')
btn = st.button(':orange[$ \Large \\bold{Guardar / Actualizar} $]', key='btnEstAca', use_container_width=True)
if btn:
    #st.write('se guarda como:', valnewestudio)
    newregistro = {'nombreu': nombreu, 'cedulau': cedulau}
    EstAca=[]

    newregistro_2 = {}
    newregistro_2['EstAca'+str(NroEstAca)]=[]
    for elemento in valnewestudio:
        for k, v in elemento.items():
            if 'Ac#' in k: 
                if 'tiempo' not in k: newregistro_2['EstAca'+str(NroEstAca)].append(k+':'+v)
                else: newregistro_2['EstAca'+str(NroEstAca)].append('Tiempo : ('+str(v[0])+','+str(v[1])+')')
    # 'newr2 = ', newregistro_2['EstAca'+str(NroEstAca)]
    # st.write('***')
    st.write('newregistro = ', newregistro)
    #st.stop()
    encuasigleh.update(newregistro_2, clave)
    st.stop()
st.write('***')

