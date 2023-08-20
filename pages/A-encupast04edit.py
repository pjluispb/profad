
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from deta import Deta
import pandas as pd
import datetime
import time
#from streamlit_toggle import st_toggle_switch
#from streamlit_extras.stateful_button import button

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
updvalea=[]

def esta_en_lista(lista1, lista2):
    for i in lista1:
        if i not in lista2:
            return False
    return True

def item(ti, v1, v2, v3):
    newcont = st.container()
    with newcont:
        tik = 'inputtext-'+ti
        btk = 'btn-'+ti
        col1, col2 = st.columns(2)
        txtnc = col1.text_input(label='Texto'+tik, key=tik, value = v1)
        otxnc = col2.text_input(label='Otro Texto: ', key='ot-'+tik, value= v2)
        tanc = st.text_area(label='text-area-'+tik, key='tanc-'+ti, value= v3)
        btnc = st.button(label='Actualizar', key=btk)
        if btnc:
            st.write(txtnc, ' - ', otxnc, '---', tanc)
        #st.write('---')

#@st.cache_data
@st.cache_data(experimental_allow_widgets=True)
def newElemnt(datTexto, num, cond):  
    tik = datTexto[0]+str(num)
    if datTexto[1]=='texto':
        param = st.text_input(label=datTexto[2], value=datTexto[4], key='keyt-'+tik+datTexto[3])
        if cond == 'add': 
            if param not in ['', '-', None]:
                newvalea.append({tik:param})
                st.session_state['newvalea'] = newvalea
        else:
            if param not in ['', '-', None]:
                updvalea.append({tik:param})
                st.session_state['upvalea'] = updvalea

    if datTexto[1]=='textarea':
        param = st.text_area(label=datTexto[2], value=datTexto[3], key='keyta-'+tik)
        if cond == 'add':
            if param not in ['', '-', None]:
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
        #st.write('param = ', param)
        #st.stop()
        if param[1] not in ['-','',None]: newvalea.append({tik:param})
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
    
def estudioBaseA(etiescuela,eticertificadonivelAc, contador):
    st.write('****Estudio Base Académico****')
    escuelaField = 'escuelaAc#'
    clavetxtAc = 'escAc1'
    #etiescuela = 'Nombre del colegio/escuela'
    valnewescuelaField = newElemnt([escuelaField, 'texto', etiescuela, clavetxtAc, '-'], contador, 'add')

    namemodoAcField = 'modoAc#'
    opcionesmodoAc = ['presencial', 'en línea /a distancia', 'híbrido']
    etiquetamodoAc = 'Modalidad de estudio'
    valnewmodoAc = newElemnt([namemodoAcField, 'select slider', etiquetamodoAc, opcionesmodoAc], contador, 'add')

    tiempoAcField = 'tiempoAc#'
    etiquetaTiempoAc = 'Tiempo de estudio (Desde...Hasta)'
    minimo = 1960
    maximo = 2023
    desde = 1990
    hasta = 2000
    valnewtiempoAc = newElemnt([tiempoAcField, 'range slider', etiquetaTiempoAc, minimo, maximo, (desde, hasta)], contador, 'add')

    certificadonivelAcField = 'certificadonivelAc#'
    clavecerAc = 'certAc1'
    #eticertificadonivelAc = 'Certificado y/o último nivel alcanzado'
    valnewcertificadonivelAcField = newElemnt([certificadonivelAcField, 'texto', eticertificadonivelAc, clavecerAc, '-'], contador, 'add')


    btfoto = st.checkbox(label='tomar foto', key='keyFotoCertAc'+str)
    if btfoto:
        nombreFoto = 'fotoCertAc'+str(contador)+'-clave-ima01-seq01.png'
        st.write('nameFoto = ', nombreFoto)
    
    describeAcField = 'describeAc#'
    etidescribeAc = 'Breves comentarios sobre la experiencia educativa'
    valor = '-'
    valnewdescribeAcField = newElemnt([describeAcField, 'textarea', etidescribeAc, valor], contador, 'add')
    return(valnewescuelaField)

def estudiosARegistrados(ti, valores):
    newcont = st.container()
    with newcont:
        with st.form('estudio registrado'+ti):
            tik = ti[1:]
            btk = 'btnea'+ti
            lvalores = list(valores.items())
            #'lvalores = ', lvalores
            estudioanc = st.text_area(label=lvalores[0][0], value=lvalores[0][1])
            certificadoanc = st.text_input(label=lvalores[1][0], value=lvalores[1][1])
            #descriptranc = st.text_area(label=lvalores[2][0], value=lvalores[2][1])
            if lvalores[2][1] == '':
                desde='2000'
                hasta='2000'
            else:
                desde = str(lvalores[2][1][0])
                hasta = str(lvalores[2][1][1])
            # desde, hasta
            try:
                tiempoeanc = st.slider(label='Tiempo de estudio academico: desde el año '+desde+' hasta el '+hasta,min_value=int(desde)-4, max_value=int(hasta)+4, value=(int(desde), int(hasta)))
            except:
                tiempoeanc = st.slider(label='Tiempo de estudio academico: desde el año '+desde+' hasta el '+hasta, min_value=int(desde), max_value=int(hasta))
            newvalea.append({lvalores[0][0]:estudioanc, lvalores[1][0]:certificadoanc, lvalores[2][0]:tiempoeanc})
            btnc = st.form_submit_button(label='Actualizar',  use_container_width=True)
            if btnc:
                st.write('clickaste Actualizar')
                st.session_state['clave'] = clave
                st.session_state['newvalea'] = newvalea
                st.session_state['nombreu'] =  nombreu
                st.session_state['cedulau'] = cedulau

                switch_page('testnewitem_edit_ea')
        fotoCerT = clave+'_certea'+tik+'_ima01_si00.png'
        #'fotoCerT = ', fotoCerT
        try:
            imagenCer = photos.get(fotoCerT)
            content = imagenCer.read()
            st.image(content)
            btcer1 = st.button('Actualizar foto del Certificado/Título de estudio académico', key='foto-'+btk, use_container_width=True)
        except:
            btcer1 = st.button('Tomar foto del Certificado del trabajo', key='foto-'+btk, use_container_width=True)
        if btcer1:
            st.session_state['nameima'] = fotoCerT
            st.session_state['clave'] = clave
            st.session_state['nombreu'] = nombreu
            st.session_state['cedulau'] = cedulau 
            switch_page('A-surtphoto05a')
        st.write('***')
        st.write('***')
        


st.header('Encuesta del Pastorado ASIGLEH 2023')
st.subheader('Iglesia de Los Hermanos - Venezuela')
st.text('Ficha de Registro')

encuasigleh, photos, photosys = abrerecursosdeta()

# nombreu = "dinozzo"                    # nombreu = st.session_state['nombreu']
# cedulau = "11111"                     # cedulau = st.session_state['cedulau']
# rol = "Pastor"                         # rol = st.session_state['rol']
# clave = "asigleh-11111-dinozzo"        # clave = st.session_state['clave']

nombreu = st.session_state['nombreu']
cedulau = st.session_state['cedulau']
rol = st.session_state['rol']
clave = st.session_state['clave']

clavei = nombreu+'_'+cedulau
st.write(':red[Bienvenido $\\tiny '+clavei+'    -    '+clave+'  <->  '+rol+'$]')
# st.toast('$$ \large Bienvenido $$'+' 	:smiley:  $\large  \\textcolor{red}{'+nombreu+'}$', icon="🆔")

registro = encuasigleh.get(key=clave)
# registro
cra = list(registro.keys())
# 'camposregactual : ', cra
# cra[100], registro[cra[100]]
camposreg = ["nombreu", "cedulau", "Nombres", "Apellidos", "Nacionalidad", "Telefono", "Celular", "email", "Whatsapp", "Facebook", "Instagram", "Twitter", "Direccion", "Edo_Civil", "Edad", "Iglesia", "DireccionIglesia", "Pastor",	"nivestudios","estudio1","certifi1","estudio2","certifi2","estudio3","certifi3","estudio4","certifi4","estudio5","certifi5","otrosEstudiosAcademicos", "cargoIgle", "min_damas", "min_caba", "min_diaco", "min_jov", "min_ados", "min_ninos", "min_aa", "min_fami", "min_misio", "min_celu", "min_ense", "min_prof", "otrosMin",  "cargo_tra_1", "empresa_1",  "cargo_tra_2", "empresa_2",  "cargo_tra_3", "empresa_3",  "cargo_tra_4", "empresa_4",  "cargo_tra_5", "empresa_5",  "otrosc", "fec_conversion", "fec_bautismo_agua", "fec_bautismo_Espiritu", "testimonio", "llamado", "estudiob1", "nivCertBib1", "estudiob2", "nivCertBib2", "estudiob3", "nivCertBib3", "estudiob4", "nivCertBib4", "otrosEstudiosBiblicos", "categomin", "minist_1", "orgigle_1", "tiempominist_1", "descripmin_1", "minist_2", "orgigle_2", "tiempominist_2", "descripmin_2", "minist_3", "orgigle_3", "tiempominist_3", "descripmin_3", "minist_4", "orgigle_4", "tiempominist_4", "descripmin_4", "minist_5", "orgigle_5", "tiempominist_5", "descripmin_5", "otrostrabmin", "tabaq", "cigarrosSlide", "exfumador", "fumadorPasivo", "consumoExposicion", "alcohol", "cantidadXsem", "tiempoDeConsumo", "exalcoholico", "AlcoholicOcasional", "alergias", "queAlergias", "tipoSangre", "farmacodependencia",  "farmacoTiempo", "observaciones", "enfermedadesInfancia", "secuelas", "padeinfa", "parasin", "neurologico", "fiebrereuma", "tuberculosis", "diabemelitus", "fiebreuptiva", "parodiepi", "enfermavene",  "tifoidea", "mentales", "inmunalergi", "vasculares",  "malforcon", "diarreas", "difteria", "artropatias",  "hipertension", "exporadia", "paludismo", "sifilisov", "meningitis",  "polio", "otrospad", "traumaciru", "Inmualertrans"]
camposregfinal = list(set(cra + camposreg))
# 'camposregfinal', camposregfinal
st.write(esta_en_lista(camposreg, camposregfinal), len(camposreg), len(camposregfinal), len(cra))

valores={}
for t in camposregfinal:
    #t
    try:
        #registro[t]
        valores[t] = registro[t]
    except:
        valores[t]=''
    if valores[t]==None: valores[t]=''
'valores = ', valores


try:  #normaliza algunos campos para mostrarlos en la app
    if valores['Edad']=='': valores['Edad']=0
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
    if valores['categomin']=='': valores['categomin']='No se'
except:
    st.write('---')
# st.write( 'valores = ', valores)
with st.expander(':orange[$\Large Datos\, Personales$]'):
    st.info('ℹ️ 🙂 Aquí solicitamos información básica sobre tu persona, los medios a través de los cuáles nos podemos comunicar contigo, tus redes sociales e información acerca de tu familia más cercana ')
    nombre = st.text_input('Nombres ---- Obligatorio', value=valores['Nombres'])
    apellido = st.text_input('Apellidos    ----   Obligatorio', value=valores['Apellidos'])
    nacionalidad = st.text_input('Nacionalidad', value=valores['Nacionalidad'])
    indEdo_Civil = ['', 'Soltero','Casado','Viudo','Otro'].index(valores['Edo_Civil'])
    Edo_Civil = st.selectbox('Estado Civil',['', 'Soltero','Casado','Viudo','Otro'], index=indEdo_Civil)
    #fecnac = st.date_input('Fecha de nacimiento',min_value=datetime.date(1940,1,1))
    edad = st.slider('Edad', value=valores['Edad'])
    direccion = st.text_input('Dirección', value=valores['Direccion'])

    st.subheader(':green[$\small Comunicaciones$]')
    # muestra telefonos
    conttel = 0
    for string in cra:
        if string.startswith('tel'):
            conttel+=1
            clavetele = 'tele-'+str(conttel)
            # st.write(string, valores[string], conttel)
            valtel = newElemnt([str(conttel), 'texto', 'Teléfono-'+str(conttel), clavetele, valores[string]], conttel, 'show') 

    conttel+=1
    clavetel = 'tel1'
    valnewtexto = newElemnt(['telefono#', 'texto', 'Teléfono', clavetel, '-'], conttel, 'add') 
    st.write('***') 
    # muestra email
    contmail = 0 
    for string in cra:
        if string.startswith('email#'):
            contmail+=1
            clavemail = 'email-'+str(contmail)
            # st.write(string, valores[string], conttel)
            valtel = newElemnt([str(contmail), 'texto', 'Email-'+str(contmail), clavemail, valores[string]], contmail, 'show') 

    contmail+=1 
    clavemail = 'email1'
    valnewemail = newElemnt(['email#', 'texto', 'Email', clavemail, '-'], contmail, 'add')

    
    st.subheader(':green[$\small Redes\, Sociales$]')

    conredso = 0
    for string in cra:
        if string.startswith('redsocial'):
            conredso+=1
            claveredso = 'redso-'+str(conredso)
            valredso = newElemnt([str(conredso), 'texto', valores[string][0], claveredso, valores[string][1]], conredso, 'show') 
    
    conredso+=1
    claveredso = 'redsocial1'

    nameField = 'redsocial#'
    opcionesradio = ['-', 'Facebook', 'Whatsapp', 'Telegram', 'Otra']
    Etiqueta1_radio = 'Red Social'
    Etiqueta2_radio = 'Cual red? '
    Etiqueta3_texto = 'Ingresa tu ID(nombre, teléfono, etc) en la red social'
    # nameField, opcionesradio
    
    valnewtexto = newElemnt([nameField, 'radio + texto', Etiqueta1_radio, opcionesradio, Etiqueta2_radio,Etiqueta3_texto], conredso, 'add')
#-----------------------------------------------------------------------------------------------------
    st.subheader(':green[$\small Datos\, Familiares$]')

    # muestra email
    contrelfam = 0 
    for string in cra:
        if string.startswith('relfam'):
            contrelfam+=1
            claverelfam = 'relfam-'+str(contrelfam)
            valrelfamNom = newElemnt([str(contrelfam)+'-nombre', 'texto', 'nombre', claverelfam, valores[string][0]], contrelfam, 'show')
            valrelfamRel = newElemnt([str(contrelfam)+'rel', 'texto', 'relación', claverelfam, valores[string][1]], contrelfam, 'show')
            valrelfamDesc = newElemnt([str(contrelfam)+'coment', 'texto', 'Comentario', claverelfam, valores[string][2]], contrelfam, 'show')
            st.write('***')
    contrelfam+=1

    nombrefamField = 'relfamnombre#'
    clavenomfam = 'nf1'
    etinomfam = 'Nombre del familiar'
    valnewnombrefamField = newElemnt([nombrefamField, 'texto', etinomfam, clavenomfam, '-'], contrelfam, 'add')

    #st.write('Tipo de Relación')
    tiporelp = st.radio(label='Tipo de relación', options=['cosanguinea', 'política', 'de adopción', 'de crianza', 'ninguna'], index=4, horizontal=True)
    if tiporelp == 'cosanguinea':
        tiporels = st.radio(label='cosanguinea', options=['Padres', 'Abuelos', 'Hermanos', 'Tíos', 'Primos', '-'], index=4, horizontal=True)
    elif tiporelp == 'política':
        tiporels = st.radio(label='políticos', options=['Cónyuge','Suegros','Yerno','Nuera','Cuñados'], horizontal=True)
    elif tiporelp == 'de adopción':
        tiporels = st.radio(label='adoptivos', options=['Padres','Hermanos','Hijos'], horizontal=True)
    elif tiporelp == 'de crianza':
        tiporels = st.radio(label='de crianza', options=['Padres','Hermanos','Hijos'], horizontal=True)
    else:
        tiporels = '-'
        #st.write('***')
    relfamtipo = tiporelp+' - '+tiporels
    describeFamField = 'relfamdescripcion#'
    etidescribefam = 'Breve comentario sobre la relación ...'
    valor = '-'
    valnewdescribeFamField = newElemnt([describeFamField, 'textarea', etidescribefam, valor], contrelfam, 'add')

    #valrelfamcomb = [valnewnombrefamField, tiporelp, tiporels, valnewdescribeFamField]

    # btn = st.button(label='Guardar')
    btn = st.button(':orange[$ \large \\bold{Guardar / Actualizar} $]', key='btndatper', use_container_width=True)
    if btn:
        try:
            st.write('se guarda como:',st.session_state['newvalea'])
        except:
            st.write('error')
            st.stop()
        #'valrelfamcomb = ',valrelfamcomb 
        newregistro = {'Nombres': nombre, 'Apellidos':apellido, 'Nacionalidad': nacionalidad, 'nombreu': nombreu, 'cedulau': cedulau, 'Direccion': direccion, 'Edo_Civil': Edo_Civil,'Edad': edad}
        #newregistro
        for elemento in valnewtexto:
            newregistro.update(elemento)
        st.write('***')
        st.write(newregistro)
        st.write(relfamtipo)
        newregistro_2 = {}
        for key, value in newregistro.items():
            if key.startswith('relfamnom'):
                crf = key.split('#')[1]
                newregistro_2['relfam'+str(crf)]=[]
                newregistro_2['relfam'+str(crf)].append(value)
                newregistro_2['relfam'+str(crf)].append(relfamtipo)
                newregistro_2['relfam'+str(crf)].append(newregistro['relfamdescripcion'+'#'+str(crf)])
            elif key.startswith('relfamdes'):
                relfamdes = '---'
            else:
                newregistro_2[key]=value
        'newregistro_2 : ', newregistro_2

        # st.stop()
        # st.write(clave)
        encuasigleh.update(newregistro_2, clave)
        
        switch_page('A-depaso1')

    
    st.write('***')
        
with st.expander(':orange[$ \large Ministerios/iglesia\, que\, preside\, ó\\newline participa\, actualmente $]'):
    st.info('ℹ️ 🙂 Datos acerca de la iglesia y/o ministerios que presides. Por ejemplo eres el pastor Asociado de la iglesia de La Pradera y el tesorero de la confraternidad de pastores de La Montaña. ')
    coniglemin = 0
    listiglemin = []
    igleminval = {}
    for string in cra:
        if string.startswith('iglemin'):
            coniglemin+=1
            #st.write(string, valores[string])
            #st.info(':red[ '+valores[string][0].split(':')[0]+ '] :'+'$ \\newline $'+' :blue['+ valores[string][0].split(':')[1]+']' + '$ \\newline $'+ ':red[ '+valores[string][1].split(':')[0]+ '] :'+'$ \\newline $'+' :blue['+ valores[string][1].split(':')[1]+']'  + '$ \\newline $'+ ':red[ '+valores[string][2].split(':')[0]+ '] :'+'$ \\newline $'+' :blue['+ valores[string][2].split(':')[1]+']'  + '$ \\newline $'+ ':red[ '+valores[string][3].split(':')[0]+ '] :'+'$ \\newline $'+' :blue['+ valores[string][3].split(':')[1]+']')
            claveiglemin = 'iglemin-'+str(coniglemin)

            valigleminNom = st.text_input(label=':blue[$ \\bold{Nombre}  $]', value=valores[string][0].split(':')[1], key=claveiglemin+'nombre')
            valigleminDir = st.text_input(label=':blue[$ \\bold{Dirección}  $]', value=valores[string][1].split(':')[1], key=claveiglemin+'direccion')
            valigleminNiv =  st.text_input(label=':blue[$ \\bold{Nivel \, Ministerial}  $]', value=valores[string][2].split(':')[1], key=claveiglemin+'nivmin')
            try:
                valigleminDes = st.text_area(label=':blue[$ \\bold{Descripción}  $]', value = valores[string][3].split(':')[1], key=claveiglemin+'desc')
            except:
                valigleminDes = st.text_area(label=':blue[$ \\bold{Descripción}  $]', value = '-', key=claveiglemin+'desc')
            #valores[string]
            igleminval[string] = ['Nombre Iglesia/Ministerio : '+str(valigleminNom),'Dirección : '+str(valigleminDir), 'Nivel(cargo) Ministerial : '+str(valigleminNiv), 'Descripción : '+str(valigleminDes)]
            # string, igleminval[string]
            listiglemin.append((string,igleminval[string]))
            st.write('***')


    coniglemin+=1

    nombreField1 = 'IgleMinactual#'
    etinomfam1 = 'Nombre del Ministerio / Iglesia que preside actualmente'
    clavetxt = 'im1'
    valnewNombreField1 = newElemnt([nombreField1, 'texto', etinomfam1, clavetxt, '-'], coniglemin, 'add')

    direccionField2 = 'direccionIgleMin#'
    etinomfam2 = 'Dirección de la Iglesia / Ministerio'
    clavedir = 'dir1'
    valnewDireccionField2 = newElemnt([direccionField2, 'texto', etinomfam2, clavedir, '-'], coniglemin, 'add')

    nivelLiderField = 'nivelLiderIgleMin#'
    opcionesradio = ['-', 'Pastor principal', 'Líder', 'Asociado', 'Miembro', 'Otro']
    Etiqueta1 = 'Nivel Ministerial ó de Liderazgo (Cargo)'
    Etiqueta2 = 'Label o etiqueta secundaria'
    valnewNivelLider = newElemnt([nivelLiderField, 'radio', Etiqueta1, opcionesradio, Etiqueta2], coniglemin, 'add') 

    describeIgleMinField = 'descripcionIgleMin#'
    etidescribeIgleMin = 'Breve descripción de la Iglesia / Ministerio que preside'
    valor = '-'
    valnewdescribeIgleMinField = newElemnt([describeIgleMinField, 'textarea', etidescribeIgleMin, valor], coniglemin, 'add')

    # btn = st.button(label='Guardar', key='btn-iglemin201')
    btn = st.button(':orange[$ \large \\bold{Guardar / Actualizar} $]', key='btn-iglemin201', use_container_width=True)
    if btn:
        try:
            st.write('se guarda como:',st.session_state['newvalea'])
        except:
            st.write('No hay newvalea')
        #'valrelfamcomb = ',valrelfamcomb 
        newregistro = {'Nombres': nombre, 'Apellidos':apellido, 'Nacionalidad': nacionalidad, 'nombreu': nombreu, 'cedulau': cedulau, 'Direccion': direccion, 'Edo_Civil': Edo_Civil,'Edad': edad}
        #newregistro
        for elemento in valnewtexto:
            newregistro.update(elemento)
        st.write('***')
        st.write(newregistro)
        
        #st.write(relfamtipo)
        newregistro_2 = {}
        lxc1 = [(k,v) for (k,v) in newregistro.items() if 'IgleMin' in k]
        'lxc1 = ', lxc1
        keysinlxc1 = [k for (k,v) in lxc1]
        'keys in lxc1 = ', keysinlxc1
        cim = keysinlxc1[0].split('#')[1]
        newregistro_2['iglemin'+str(cim)]=[]
        for k,v in newregistro.items():
            if k in keysinlxc1:
                if 'actual' in k and v not in ['-', '', None]: newregistro_2['iglemin'+str(cim)].append('Nombre Iglesia/Ministerio : '+v)
                elif 'direccion' in k and v not in ['-', '', None]: newregistro_2['iglemin'+str(cim)].append('Dirección : '+v)
                elif 'nivel' in k and v not in ['-', '', None]: newregistro_2['iglemin'+str(cim)].append('Nivel(cargo) Ministerial : '+v)
                elif 'descripcion' in k and v not in ['-', '', None]: newregistro_2['iglemin'+str(cim)].append('Descripción : '+v)
            else:
                newregistro_2[k]=v
        if newregistro_2['iglemin'+str(cim)]==[]:
            del newregistro_2['iglemin'+str(cim)]
        listiglemin
        for elem in listiglemin:
            newregistro_2[elem[0]] = elem[1]
        'newregistro_2 = ', newregistro_2
        # st.stop()

        # st.write(clave)
        encuasigleh.update(newregistro_2, clave)
        
        switch_page('A-depaso1')

    
    st.write('***')

with st.expander(':orange[$\Large Testimonio $]'):
    st.info('ℹ️ 🙂Por favor comparte tu testimonio de salvación y llamado al ministerio ')
    fec_conversion = st.date_input(label=':blue[$ Fecha \,de \, \\bold{Conversión}  $]',  min_value=datetime.date(1940,1,1), format='DD/MM/YYYY', value=datetime.datetime.strptime(valores['testi_fec_conversion'], '%d/%m/%Y'))
    fec_bautismo_agua = st.date_input(':blue[$ Fecha \, de\, Bautismo \, en\, agua  $]', min_value=datetime.date(1940,1,1), format='DD/MM/YYYY', value=datetime.datetime.strptime(valores['testi_fec_bautismo_agua'], '%d/%m/%Y'))
    fec_bautismo_Espiritu = st.date_input(':blue[$ Fecha\, de\, Bautismo\, en\, \\newline el\, \\bold{Espiritu\, Santo}  $]',  min_value=datetime.date(1940,1,1), format='DD/MM/YYYY', value=datetime.datetime.strptime(valores['testi_fec_bautismo_Espiritu'], '%d/%m/%Y'))
    testimonio = st.text_area(label=':blue[$ Compártenos\, tu\, testimonio\, de\, \\bold{salvación}  $]', value=valores['testi_tesimonioS'])
    llamado = st.text_area(label=':blue[$ Compártenos\, tu\, testimonio\, acerca\, de\, tu\\newline \\bold{llamado\, ministerial.\,} \\newline \\scriptsize  ¿Cómo,\, cuándo\, y\, dónde\,  inició\, su\, ministerio? $]', value=valores['testi_llamado'])
    st.write('---')
    guarda06 = st.button(':orange[$ \large \\bold{Guardar / Actualizar} $]', key='btntestimonio', use_container_width=True)
    if guarda06:
        st.write('---guardando Datos sobre su testimonio---')
        st.write(fec_conversion, fec_bautismo_agua, fec_bautismo_Espiritu, testimonio, llamado)
        newregistro = {'Nombres': nombre, 'Apellidos':apellido, 'nombreu': nombreu, 'cedulau': cedulau, 'Direccion': direccion, 'Edo_Civil': Edo_Civil,'Edad': edad, 'testi_fec_conversion':fec_conversion.strftime('%d/%m/%Y'), 'testi_fec_bautismo_agua':fec_bautismo_agua.strftime('%d/%m/%Y'), 'testi_fec_bautismo_Espiritu':fec_bautismo_Espiritu.strftime('%d/%m/%Y'), 'testi_tesimonioS':testimonio, 'testi_llamado':llamado}
        newregistro
        clave
        #st.stop()

        encuasigleh.update(newregistro, clave)
        
        switch_page('A-depaso1')

        # 
        # update_reg_dattestimonio(fec_conversion, fec_bautismo_agua, fec_bautismo_Espiritu, testimonio, llamado)

with st.expander(':orange[$\Large Trabajo\, ministerial$]'):
    st.info('ℹ️ 🙂En esta sección queremos nos hables sobre las diferentes tareas o trabajos ministeriales que haz realizado o realizas en la iglesia. Tareas cómo pastorear, dirigir un ministerio, etc, que hayas ejecutado en tiempos, lugares y hasta organizaciones diferentes')
    conTraMin = 0
    listTramin = []
    TraMinval = {}
    
    for string in cra:
        if string.startswith('TraMin'):
            conTraMin+=1
            claveTraMin = 'TraMin-'+str(conTraMin)

            valTraMinNom = st.text_input(label=':blue[$ \\bold{Iglesia/Ministerio}  $]', value=valores[string][0].split(':')[1], key=claveTraMin+'nombre')
            valTiempo = valores[string][1].split(':')[1]
            #valTiempo
            valTiempoIni = int(valTiempo.split(',')[0].replace('(',''))
            valTiempoFin = int(valTiempo.split(',')[1].replace(')',''))
            #valTiempoIni, valTiempoFin
            valTraMinTiempo = st.slider(label=':blue[$ \\bold{Tiempo\, en\, el\, ministerio/iglesia}  $]', value=(valTiempoIni, valTiempoFin), min_value=valTiempoIni-10, max_value=valTiempoFin+10)
            valTraMinOrg = st.text_input(label=':blue[$ \\bold {Organización\, /\, Iglesia\, /\, Ministerio}  $]', value=valores[string][2][valores[string][2].index(':') + 1:].strip(), key=claveTraMin+'organizacion')
            valTraMinDes = st.text_area(label=':blue[$ \\bold{Descripción\, del\, \\newline trabajo\, ministerial}  $]', value=valores[string][3][valores[string][3].index(':') + 1:].strip(), key=claveTraMin+'descripcion')
            valTraMinRef =  st.text_input(label=':blue[$ \\bold{Referencias }  $]', value=valores[string][4][valores[string][4].index(':') + 1:].strip(), key=claveTraMin+'referencia')
            if valores[string][5]!='N/A' :
                fotoCerT = valores[string][5].split(':')[1]
                try:
                    imagenCer = photos.get(fotoCerT)
                    content = imagenCer.read()
                    st.image(content)
                    ':blue[$ \\tiny{'+valores[string][5].split(':')[1]+'} $]'
                    btcer1 = st.button('Actualizar foto del Certificado de estudio', key='btn-'+claveTraMin+'fotoTraMin')
                except:
                    btcer1 = st.button('Tomar foto del Certificado de estudio', key='btn-'+claveTraMin+'fotoTraMin')
                if btcer1:
                    st.session_state['nameima'] = fotoCerT
                    st.session_state['clave'] = clave
                    st.session_state['nombreu'] = nombreu
                    st.session_state['cedulau'] = cedulau 
                    st.write(clave, nombreu, cedulau )
                    st.write(fotoCerT)
                    switch_page('A-surtphoto05a')
            #st.session_state['nameima']
            #st.stop()
            TraMinval[string] = ['Iglesia/Ministerio : '+str(valTraMinNom),'Tiempo : '+str(valTraMinTiempo), 'Organización : '+str(valTraMinOrg), 'Descripción : '+str(valTraMinDes), 'Referencia : '+str(valTraMinRef), 'fotoref : '+str(valores[string][5].split(':')[1])]
            # string, igleminval[string]
            listTramin.append((string,TraMinval[string]))
            #TraMinval.update({claveTraMin : [{'nombre':valTraMinNom}, {'tiempo':valTraMinTiempo}, {'org':valTraMinOrg}, {'describe':valTraMinDes}, {'referencia':valTraMinRef}, {'fotoref':valores[string][5]}]})
            # TraMinval
            st.write('***')
    #st.stop()
    conTraMin+=1

    TraMinField1 = 'nombreTraMin#'
    etiTraMin = 'Iglesia / Ministerio'
    claveTraMin = 'TraMin1'
    valnewTraMinField1 = newElemnt([TraMinField1, 'texto', etiTraMin, claveTraMin, '-'], conTraMin, 'add')

    tiempoTraMinField = 'tiempoTraMin#'
    etiquetaTiempoTraMin = 'Tiempo en el ministerio/iglesia (Desde...Hasta)'
    minimo = 1980
    maximo = 2023
    desde = 1990
    hasta = 2000
    valnewtiempoTraMin = newElemnt([tiempoTraMinField, 'range slider', etiquetaTiempoTraMin, minimo, maximo, (desde, hasta)], conTraMin, 'add')

    orgTraMinField1 = 'orgTraMin#'
    etiorgTraMin = 'Organización / Iglesia / Ministerio / Departamento'
    claveorgTraMin= 'orgTraMin1'
    valneworgTraMinField1 = newElemnt([orgTraMinField1, 'texto', etiorgTraMin, claveorgTraMin, '-'], conTraMin, 'add')

    describeTraMinField = 'describeTraMin#'
    etidescribeTraMin = 'Breve descripción del trabajo ministerial'
    valor = '-'
    valnewdescribeTramMnField = newElemnt([describeTraMinField, 'textarea', etidescribeTraMin, valor], conTraMin, 'add')

    referenciaTraMinField = 'referenciaTraMin#'
    claverefTraMin = 'referenciaTraMin1'
    etireferenciaTraMin = 'Referencias sobre el trabajo ministerial'
    valnewreferenciaTraMinField = newElemnt([referenciaTraMinField, 'texto', etireferenciaTraMin, claverefTraMin, '-'], conTraMin, 'add')

    btfoto = st.checkbox(label='tomar foto de la referencia del trabajo ministerial')
    nombreFoto = 'N/A'
    if btfoto:
        nombreFoto = 'fotoRefTraMin'+str(conTraMin)+'-clave-ima01-seq01.png'
        st.write('nameFoto = ', nombreFoto)

    # btn = st.button(label='Guardar', key='btnTraMin')
    btn = st.button(':orange[$ \large \\bold{Guardar / Actualizar} $]', key='btnTraMin', use_container_width=True)
    if btn:
        st.write('se guarda como:', valnewreferenciaTraMinField)

        newregistro = {'Nombres': nombre, 'Apellidos':apellido, 'Nacionalidad': nacionalidad, 'nombreu': nombreu, 'cedulau': cedulau, 'Direccion': direccion, 'Edo_Civil': Edo_Civil,'Edad': edad}
        #newregistro
        for elemento in valnewreferenciaTraMinField:
            if 'TraMin' in str(elemento.keys()):
                newregistro.update(elemento)
        # for elemento in TraMinval.items():
        #     'elemento =' , elemento
        #     elemento[0]
        #     elemento[1]
        #     for t in elemento[1]:
        #         t.keys(), t.values()
        #     neweTriMine = {}
        #     neweTriMine.update({elemento[0] : elemento[1]})
        #     newregistro.update(neweTriMine)
            # else: st.write('Noooo')
                # newregistro.update(elemento)
        st.write('***')
        st.write(newregistro)
        # st.stop()
        newregistro_2 = {}
        
        lxc1 = [(k,v) for (k,v) in newregistro.items() if 'TraMin' in k]
        'lxc1 = ', lxc1
        keysinlxc1 = [k for (k,v) in lxc1]
        'keys in lxc1 = ', keysinlxc1
        cim = keysinlxc1[0].split('#')[1]
        newregistro_2['TraMin'+str(cim)]=[]
        #st.stop()
        for k,v in newregistro.items():
            if k in keysinlxc1:
                if 'nombre' in k : newregistro_2['TraMin'+str(cim)].append('Nombre Iglesia/Ministerio : '+v)
                elif 'tiempo' in k : newregistro_2['TraMin'+str(cim)].append('Tiempo : '+str(v))
                elif 'org' in k : newregistro_2['TraMin'+str(cim)].append('Organización : '+v)
                elif 'describe' in k : newregistro_2['TraMin'+str(cim)].append('Descripción : '+v)
                elif 'referencia' in k : newregistro_2['TraMin'+str(cim)].append('Referencia : '+v)
            else:
                newregistro_2[k]=v
        newregistro_2['TraMin'+str(cim)].append('fotoref : '+nombreFoto)
        newregistro_2['TraMin'+str(cim)], len(newregistro_2['TraMin'+str(cim)])
        
        if newregistro_2['TraMin'+str(cim)]==[] or len(newregistro_2['TraMin'+str(cim)])<4 :
            del newregistro_2['TraMin'+str(cim)]
        listTramin
        for elem in listTramin:
            newregistro_2[elem[0]] = elem[1]

        'newregistro_2 = ', newregistro_2
        # st.stop()
        encuasigleh.update(newregistro_2, clave)
        
        switch_page('A-depaso1')

        #st.stop()
    st.write('***')

with st.expander(':orange[$\large  Participación\, actual\\newline en\, los\, ministerios\, de\, su\, iglesia $]'):
    
    st.info('ℹ️ 🙂En esta sección queremos información de tu nivel de participación actual en los diferentes ministerios ó departamentos de tu iglesia. Por ejemplo, digamos que participas en el grupo o ministerio de alabanza porque tocas el piano, pero no tienes participación alguna en el departamento de damas, pero lideras a los diáconos.')
    st.caption('Por favor, trata de incluir todos los departamentos ó ministerios de tu congregación, aún cuando tu participación en alguno de ellos sea nula')

    conMinA = 0
    listMinA = []
    MinAval = {}
    for string in cra:
        if string.startswith('MinA'):
            conMinA+=1
            #st.write(string, valores[string])
            #st.info(':red[ '+valores[string][0].split(':')[0]+ '] :'+'$ \\newline $'+' :blue['+ valores[string][0].split(':')[1]+']' + '$ \\newline $'+ ':red[ '+valores[string][1].split(':')[0]+ '] :'+'$ \\newline $'+' :blue['+ valores[string][1].split(':')[1]+']'  + '$ \\newline $'+ ':red[ '+valores[string][2].split(':')[0]+ '] :'+'$ \\newline $'+' :blue['+ valores[string][2].split(':')[1]+']'  + '$ \\newline $'+ ':red[ '+valores[string][3].split(':')[0]+ '] :'+'$ \\newline $'+' :blue['+ valores[string][3].split(':')[1]+']')
            claveMinA = 'MinA-'+str(conMinA)

            valMinANom = st.text_input(label=':blue[$ \\bold{Ministerio/Departamento}  $]', value=valores[string][0].split(':')[1], key=claveMinA+'nombre')
            valores[string][1].split(':')[1]
            # ['ninguno', 'asisto', 'participo', 'líder', 'asesoro/superviso']
            # " ".join(valores[string][1].split(':')[1].split()) in ['ninguno', 'asisto', 'participo', 'líder', 'asesoro/superviso']
            valMinANiv = st.select_slider(label= ':blue[$ \\bold{Nivel\, de\, participación}  $]', options= ['ninguno', 'asisto', 'participo', 'líder', 'asesoro/superviso'], value= " ".join(valores[string][1].split(':')[1].split()), key=claveMinA+'nivmin')
            try:
                valMinADes = st.text_area(label=':blue[$ \\bold{Descripción}  $]', value = valores[string][2].split(':')[1], key=claveMinA+'desc')
            except:
                valMinADes = st.text_area(label=':blue[$ \\bold{Descripción}  $]', value = '-', key=claveMinA+'desc')
            #valores[string]
            MinAval[string] = ['Ministerio/Departamento : '+str(valMinANom), 'Nivel de participación : '+str(valMinANiv), 'Descripción : '+str(valMinADes)]
            # string, igleminval[string]
            listMinA.append((string,MinAval[string]))
            st.write('***')


    conMinA+=1

    nombreMinAField = 'nombreMinA#'
    etinomMinA = 'Nombre del ministerio/departamento de su iglesia'
    claveMinA = 'MinA1'
    valnewnombreMinAField = newElemnt([nombreMinAField, 'texto', etinomMinA, claveMinA, '-'], conMinA, 'add')

    namepMinAField = 'nivelpMinA#'
    opcionesparticipacionMinA = ['ninguno', 'asisto', 'participo', 'líder', 'asesoro/superviso']
    etiquetapMinA = 'Nivel de participación/relación en el ministerio/departamento'
    valnewpMinA = newElemnt([namepMinAField, 'select slider', etiquetapMinA, opcionesparticipacionMinA], conMinA, 'add')

    describeparMinAField = 'describeparMinA#'
    etidescribeparMinA = 'Breve descripción de su participación en el ministerio/departamento de su iglesia'
    valor = '-'
    valnewdescribeparMinAField = newElemnt([describeparMinAField, 'textarea', etidescribeparMinA, valor], conMinA, 'add')

    #btn = st.button(label='Guardar', key='btnpartMinA')
    btn = st.button(':orange[$ \large \\bold{Guardar / Actualizar} $]', key='btnpartMinA', use_container_width=True)
    if btn:
        st.write('se guarda como:', valnewdescribeparMinAField)

        newregistro = {'Nombres': nombre, 'Apellidos':apellido, 'Nacionalidad': nacionalidad, 'nombreu': nombreu, 'cedulau': cedulau, 'Direccion': direccion, 'Edo_Civil': Edo_Civil,'Edad': edad}
        #newregistro
        for elemento in valnewdescribeparMinAField:
            # 'elemento = ', elemento, str(elemento.keys())
            if 'MinA' in str(elemento.keys()):
                newregistro.update(elemento)
        st.write('***')
        st.write(newregistro)
        # st.stop()
        # st.write(relfamtipo)
        newregistro_2 = {}
        lxc1 = [(k,v) for (k,v) in newregistro.items() if 'MinA' in k]
        'lxc1 = ', lxc1
        keysinlxc1 = [k for (k,v) in lxc1]
        'keys in lxc1 = ', keysinlxc1
        cim = keysinlxc1[0].split('#')[1]
        newregistro_2['MinA'+str(cim)]=[]
        for k,v in newregistro.items():
            if k in keysinlxc1:
                if 'nombre' in k and v not in ['-', '', None]: newregistro_2['MinA'+str(cim)].append('Ministerio/Departamento : '+v)
                elif 'nivelp' in k : newregistro_2['MinA'+str(cim)].append('Nivel de participación : '+v)
                elif 'describe' in k : newregistro_2['MinA'+str(cim)].append('Descripción : '+v)

            else:
                newregistro_2[k]=v
        if newregistro_2['MinA'+str(cim)][0].split(':')[1] in ['-','',None] or len(newregistro_2['MinA'+str(cim)])<=1:
            del newregistro_2['MinA'+str(cim)]
        listMinA
        for elem in listMinA:
            newregistro_2[elem[0]] = elem[1]
        'newregistro_2 = ', newregistro_2
        # st.stop()

        # st.write(clave)
        encuasigleh.update(newregistro_2, clave)
        
        switch_page('A-depaso1')

    
    
    st.write('***')

with st.expander(':orange[$\large Datos\, sobre\, su\, trabajo\\newline NO\, eclesiástico\, NI\, ministerial $]'):
    #st.write('***')
    st.info('ℹ️ 🙂Los Datos de trabajo NO eclesiásticos NI ministerial consisten en todos aquellos trabajos ó cargos desempeñados o en ejercicio que no tienen relación directa con el ministerio y/o trabajo en la obra del Señor.')

    conTraNoE = 0
    listTraNoE = []
    TraNoEval = {}

    for string in cra:
        if string.startswith('TraNoE'):
            conTraNoE+=1
            claveTraNoE = 'TraNoE-'+str(conTraNoE)

            valTraNoEcargo = st.text_input(label=':blue[$ \\bold{Cargo / puesto}  $]', value=valores[string][0].split(':')[1], key=claveTraNoE+'cargo')
            valTiempo = valores[string][1].split(':')[1]
            #valTiempo
            valTiempoIni = int(valTiempo.split(',')[0].replace('(',''))
            valTiempoFin = int(valTiempo.split(',')[1].replace(')',''))
            #valTiempoIni, valTiempoFin
            valTraNoETiempo = st.slider(label=':blue[$ \\bold{Tiempo en el cargo ó puesto de trabajo}  $]', value=(valTiempoIni, valTiempoFin), min_value=valTiempoIni-5, max_value=valTiempoFin+5)
            valTraNoEOrg = st.text_input(label=':blue[$ \\bold {Empresa / Organización}  $]', value=valores[string][2][valores[string][2].index(':') + 1:].strip(), key=claveTraNoE+'organizacion')
            valTraNoEDes = st.text_area(label=':blue[$ \\bold{Descripción del trabajo / puesto / cargo}  $]', value=valores[string][3][valores[string][3].index(':') + 1:].strip(), key=claveTraNoE+'descripcion')
            valTraNoERef =  st.text_input(label=':blue[$ \\bold{Referencias }  $]', value=valores[string][4][valores[string][4].index(':') + 1:].strip(), key=claveTraNoE+'referencia')
            if valores[string][5]!='N/A' :
                fotoCerT = valores[string][5].split(':')[1]
                try:
                    imagenCer = photos.get(fotoCerT)
                    content = imagenCer.read()
                    st.image(content)
                    ':blue[$ \\tiny{'+valores[string][5].split(':')[1]+'} $]'
                    btcer1 = st.button('Actualizar foto del Certificado de estudio', key='btn-'+claveTraNoE+'fotoTraNoE')
                except:
                    btcer1 = st.button('Tomar foto del Certificado de estudio', key='btn-'+claveTraNoE+'fotoTraNoE')
                if btcer1:
                    st.session_state['nameima'] = fotoCerT
                    st.session_state['clave'] = clave
                    st.session_state['nombreu'] = nombreu
                    st.session_state['cedulau'] = cedulau 
                    st.write(clave, nombreu, cedulau )
                    st.write(fotoCerT)
                    switch_page('A-surtphoto05a')
            #st.session_state['nameima']
            #st.stop()
            TraNoEval[string] = ['Cargo / puesto : '+str(valTraNoEcargo),'Tiempo : '+str(valTraNoETiempo), 'Organización : '+str(valTraNoEOrg), 'Descripción : '+str(valTraNoEDes), 'Referencia : '+str(valTraNoERef), 'fotoref : '+str(valores[string][5].split(':')[1])]
            listTraNoE.append((string,TraNoEval[string]))

            # TraNoEval
            st.write('***')
    #st.stop()
    conTraNoE+=1


    cargoField1 = 'CargoTraNoE#'
    eticargo = 'Cargo / puesto'
    clavetxt = 'cargo1'
    valnewcargoField1 = newElemnt([cargoField1, 'texto', eticargo, clavetxt, '-'], conTraNoE, 'add')

    tiempocargoField = 'tiempoTraNoE#'
    etiquetaTiempoCargo = 'Tiempo en el cargo ó puesto de trabajo (Desde...Hasta)'
    minimo = 1980
    maximo = 2023
    desde = 1990
    hasta = 2000
    valnewtiempoCargo = newElemnt([tiempocargoField, 'range slider', etiquetaTiempoCargo, minimo, maximo, (desde, hasta)], conTraNoE, 'add')        

    empresaField1 = 'empresaTraNoE#'
    etiempresa = 'Empresa / Organización'
    clavetxt = 'empresa1'
    valneworgminField1 = newElemnt([empresaField1, 'texto', etiempresa, clavetxt, '-'], conTraNoE, 'add')

    describetraNOeField = 'describeTraNoE#'
    etidescribetraNOe = 'Breve descripción del trabajo / puesto / cargo'
    valor = '-'
    valnewdescribetraminField = newElemnt([describetraNOeField, 'textarea', etidescribetraNOe, valor], conTraNoE, 'add')

    referenciatraNOeField = 'referenciaTraNoE#'
    clavereftraNOe = 'referenciatraNOe1'
    etireferenciatraNOe = 'Referencias sobre el trabajo / puesto / cargo'
    valnewreferenciatraNOeField = newElemnt([referenciatraNOeField, 'texto', etireferenciatraNOe, clavereftraNOe, '-'], conTraNoE, 'add')

    btfoto = st.checkbox(label='tomar foto de la referencia del trabajo / puesto / cargo')
    nombreFoto = 'N/A'
    if btfoto:
        nombreFoto = 'fotoRefTraNoE'+str(conTraNoE)+'-clave-ima01-seq01.png'
        st.write('nameFoto = ', nombreFoto)

    #btn = st.button(label='Guardar', key='btnTraNoE')
    btn = st.button(':orange[$ \large \\bold{Guardar / Actualizar} $]', key='btnTraNoE', use_container_width=True)
    if btn:
        st.write('se guarda como:', valnewreferenciatraNOeField)

        newregistro = {'Nombres': nombre, 'Apellidos':apellido, 'Nacionalidad': nacionalidad, 'nombreu': nombreu, 'cedulau': cedulau, 'Direccion': direccion, 'Edo_Civil': Edo_Civil,'Edad': edad}
        #newregistro
        for elemento in valnewreferenciatraNOeField:
            if 'TraNoE' in str(elemento.keys()):
                newregistro.update(elemento)

        st.write('***')
        st.write(newregistro)
        # st.stop()
        newregistro_2 = {}
        
        lxc1 = [(k,v) for (k,v) in newregistro.items() if 'TraNoE' in k]
        'lxc1 = ', lxc1
        keysinlxc1 = [k for (k,v) in lxc1]
        'keys in lxc1 = ', keysinlxc1
        cim = keysinlxc1[0].split('#')[1]
        newregistro_2['TraNoE'+str(cim)]=[]
        # st.stop()
        for k,v in newregistro.items():
            if k in keysinlxc1:
                k, v
                if 'Cargo' in k : newregistro_2['TraNoE'+str(cim)].append('Cargo / puesto : '+v)
                elif 'tiempo' in k : newregistro_2['TraNoE'+str(cim)].append('Tiempo : ('+str(v[0])+','+str(v[1])+')')
                elif 'empresa' in k : newregistro_2['TraNoE'+str(cim)].append('Empresa : '+v)
                elif 'describe' in k : newregistro_2['TraNoE'+str(cim)].append('Descripción : '+v)
                elif 'referencia' in k : newregistro_2['TraNoE'+str(cim)].append('Referencia : '+v)
            else:
                newregistro_2[k]=v
        newregistro_2['TraNoE'+str(cim)].append('fotoref : '+nombreFoto)
        newregistro_2['TraNoE'+str(cim)], len(newregistro_2['TraNoE'+str(cim)])
        
        if newregistro_2['TraNoE'+str(cim)]==[] or len(newregistro_2['TraNoE'+str(cim)])<4 :
            del newregistro_2['TraNoE'+str(cim)]
        listTraNoE
        for elem in listTraNoE:
            newregistro_2[elem[0]] = elem[1]

        'newregistro_2 = ', newregistro_2
        # st.stop()
        encuasigleh.update(newregistro_2, clave)
        
        switch_page('A-depaso1')

        #st.stop()
    st.write('***')

    #st.write('***')

with st.expander(':orange[$\Large Estudios\, eclesiásticos  $]'):
    st.info('ℹ️ 🙂Los estudios eclesiásticos son aquellos tomados en el contexto de la iglesia ó el ministerio. Incluye estudios ó cursos bíblicos, discipulares, sobre liderazgo, teológicos, entre otros.')

    conEstBib = 0
    listEstBib = []
    EstBibval = {}

    for string in cra:
        if string.startswith('EstBib'):
            conEstBib+=1
            claveEstBib = 'EstBib-'+str(conEstBib)
            valEstBibNom = st.text_input(label=':blue[$ \\bold{Nombre del curso eclesiástico/bíblico}  $]', value=valores[string][0].split(':')[1], key=claveEstBib+'nombre')
            valEstBibNiv =  st.text_input(label=':blue[$ \\bold{Tipo de estudio eclesiástico}  $]', value=valores[string][1].split(':')[1], key=claveEstBib+'nivestb')
            valEstBibOrg = st.text_input(label=':blue[$ \\bold{Instituto/ministerio/iglesia proveedor}  $]', value=valores[string][2].split(':')[1], key=claveEstBib+'org')
            valores[string][3].split(':')[1]
            valEstBibmode = st.select_slider(label= ':blue[$ \\bold{Nivel\, de\, participación}  $]', options= ['presencial', 'en línea / a distancia', 'híbrido'], value= " ".join(valores[string][3].split(':')[1].split()), key=claveEstBib+'modestb')

            valTiempo = valores[string][4].split(':')[1]
            valTiempoIni = int(valTiempo.split(',')[0].replace('(',''))
            valTiempoFin = int(valTiempo.split(',')[1].replace(')',''))
            #valTiempoIni, valTiempoFin
            valEstBibTiempo = st.slider(label=':blue[$ \\bold{Tiempo de estudio}  $]', value=(valTiempoIni, valTiempoFin), min_value=valTiempoIni-5, max_value=valTiempoFin+5)

            valEstBibRef =  st.text_input(label=':blue[$ \\bold{Referencias }  $]', value=valores[string][5][valores[string][5].index(':') + 1:].strip(), key=claveEstBib+'referencia')
            if valores[string][6]!='N/A' :
                fotoCerT = valores[string][6].split(':')[1]
                try:
                    imagenCer = photos.get(fotoCerT)
                    content = imagenCer.read()
                    st.image(content)
                    ':blue[$ \\tiny{'+valores[string][6].split(':')[1]+'} $]'
                    btcer1 = st.button('Actualizar foto del Certificado de estudio', key='btn-'+claveEstBib+'fotoEstBib')
                except:
                    btcer1 = st.button('Tomar foto del Certificado de estudio', key='btn-'+claveEstBib+'fotoEstBib')
                if btcer1:
                    st.session_state['nameima'] = fotoCerT
                    st.session_state['clave'] = clave
                    st.session_state['nombreu'] = nombreu
                    st.session_state['cedulau'] = cedulau 
                    st.write(clave, nombreu, cedulau )
                    st.write(fotoCerT)
                    switch_page('A-surtphoto05a')
            #st.session_state['nameima']
            #st.stop()
            valEstBibDes = st.text_area(label=':blue[$ \\bold{Descripción del curso realizado}  $]', value=valores[string][6][valores[string][6].index(':') + 1:].strip(), key=claveEstBib+'descripcion')

            EstBibval[string] = ['Nombre del curso eclesiástico/bíblico : '+str(valEstBibNom), 'Tipo de estudio eclesiástico : '+str(valEstBibNiv), 'Instituto/ministerio/iglesia proveedor : '+str(valEstBibNiv), 'Nivel de participación : '+str(valEstBibmode), 'Tiempo de estudio : '+str(valEstBibTiempo), 'Referencias :'+str(valEstBibRef), 'fotoref : '+str(valores[string][6].split(':')[1]), 'Descripción del curso :'+str(valEstBibDes)]
            listEstBib.append((string,EstBibval[string]))

            # TraNoEval
            st.write('***')

    conEstBib+=1

    nombreEBField = 'nombreEB#'
    etinomEB = 'Nombre del curso eclesiástico/bíblico'
    clavetxt = 'nomEB1'
    valnewnombreEBField = newElemnt([nombreEBField, 'texto', etinomEB, clavetxt, '-'], conEstBib, 'add')

    tipoEBField = 'tipoEB#'
    opcionestipoEB = ['-', 'Bíblico', 'Discipular', 'Liderazgo', 'Teológico', 'Otra']
    Etiqueta1 = 'Tipo de estudio eclesiástico (ejem: bíblico, liderazgo ó de liderazgo, etc)'
    Etiqueta2 = 'Especifique el tipo de estudio'
    valnewtipoEB = newElemnt([tipoEBField, 'radio', Etiqueta1, opcionestipoEB, Etiqueta2], conEstBib, 'add')

    institutoEBField = 'institucionEB#'
    clavetxtiEB = 'iEB1'
    etiinstitutoEB = 'Nombre del instituto/ministerio/iglesia proveedor del estudio y el lugar o sede de dicha organización'
    valnewinstitutoEBField = newElemnt([institutoEBField, 'texto', etiinstitutoEB, clavetxtiEB, '-'], conEstBib, 'add')

    namemodoEBField = 'modoEB#'
    opcionesmodoEB = ['presencial', 'en línea /a distancia', 'híbrido']
    etiquetamodoEB = 'Modalidad de estudio'
    valnewmodoEB = newElemnt([namemodoEBField, 'select slider', etiquetamodoEB, opcionesmodoEB], conEstBib, 'add')

    tiempoEBField = 'tiempoEB#'
    etiquetaTiempoEB = 'Tiempo de estudio (Desde...Hasta)'
    minimo = 1980
    maximo = 2023
    desde = 1990
    hasta = 2000
    valnewtiempoEB = newElemnt([tiempoEBField, 'range slider', etiquetaTiempoEB, minimo, maximo, (desde, hasta)], conEstBib, 'add')

    certificadonivelEBField = 'certificadonivelEB#'
    clavecerEB = 'certEB1'
    eticertificadonivelEB = 'Certificado y/o último nivel alcanzado'
    valnewcertificadonivelEBField = newElemnt([certificadonivelEBField, 'texto', eticertificadonivelEB, clavecerEB, '-'], conEstBib, 'add')


    btfoto = st.checkbox(label='tomar foto')
    if btfoto:
        nombreFoto = 'fotoRefmin'+str(conEstBib)+'-clave-ima01-seq01.png'
        st.write('nameFoto = ', nombreFoto)
    
    describeEBField = 'describeEB#'
    etidescribeEB = 'Breve descripción del estudio realizado'
    valor = '-'
    valnewdescribeEBField = newElemnt([describeEBField, 'textarea', etidescribeEB, valor], conEstBib, 'add')

    # btn = st.button(label='Guardar')
    btn = st.button(':orange[$ \large \\bold{Guardar / Actualizar} $]', key='btnEstBib', use_container_width=True)
    if btn:
        st.write('se guarda como:', valnewinstitutoEBField)

        newregistro = {'Nombres': nombre, 'Apellidos':apellido, 'Nacionalidad': nacionalidad, 'nombreu': nombreu, 'cedulau': cedulau, 'Direccion': direccion, 'Edo_Civil': Edo_Civil,'Edad': edad}
        #newregistro
        for elemento in valnewreferenciatraNOeField:
            if 'EB' in str(elemento.keys()):
                newregistro.update(elemento)

        st.write('***')
        st.write('newregistro = ', newregistro)
        # st.stop()

        newregistro_2 = {}
        
        lxc1 = [(k,v) for (k,v) in newregistro.items() if 'EB' in k]
        'lxc1 = ', lxc1
        keysinlxc1 = [k for (k,v) in lxc1]
        'keys in lxc1 = ', keysinlxc1
        cim = keysinlxc1[0].split('#')[1]
        newregistro_2['EstBib'+str(cim)]=[]
        #st.stop()
        for k,v in newregistro.items():
            if k in keysinlxc1:
                k, v
                if 'nombre' in k : newregistro_2['EstBib'+str(cim)].append('Nombre del curso eclesiástico/bíblico :'+v)
                elif 'tipo' in k : newregistro_2['EstBib'+str(cim)].append('Tipo de curso :'+v)
                elif 'institu' in k : newregistro_2['EstBib'+str(cim)].append('Instituto/ministerio/iglesia proveedor :'+v)
                elif 'modo' in k : newregistro_2['EstBib'+str(cim)].append('Modalidad de estudio : '+v)
                elif 'tiempo' in k : newregistro_2['EstBib'+str(cim)].append('Tiempo : ('+str(v[0])+','+str(v[1])+')')
                elif 'certificadonivel' in k : newregistro_2['EstBib'+str(cim)].append('Certificado y/o último nivel alcanzado : '+v)
                elif 'describe' in k : newregistro_2['EstBib'+str(cim)].append('Descripción : '+v)
                
            else:
                newregistro_2[k]=v
        newregistro_2['EstBib'+str(cim)].append('fotoref : '+nombreFoto)
        newregistro_2['EstBib'+str(cim)], len(newregistro_2['EstBib'+str(cim)])
        
        if newregistro_2['EstBib'+str(cim)][0] in ['','-',None] or len(newregistro_2['EstBib'+str(cim)])<5 :
            del newregistro_2['EstBib'+str(cim)]
        listEstBib
        for elem in listEstBib:
            newregistro_2[elem[0]] = elem[1]

        'newregistro_2 = ', newregistro_2
        # st.stop()
        encuasigleh.update(newregistro_2, clave)
        
        switch_page('A-depaso1')

        #st.stop()
    st.write('***')

    st.write('***')

with st.expander(':orange[$\Large Estudios\, académicos$]'):
    
    st.info('ℹ️ 🙂En esta sección se requiere proveer información de todos los estudios académicos formales realizados en los niveles básico(prescolar y primaria), media(secundaria y técnico medio), superior/universitario(técnico, pre-grado y post-grado) y post-doctorado. Los denominados transversales hacen referencia a todos aquellos con un menor reconocimiento o carga académica, tales como diferentes cursos, especializaciones y diplomados')
    
    AEAbtn = st.button('Agregar/Editar/Actualizar')
    if AEAbtn:
        st.session_state['nombreu'] = nombreu
        st.session_state['cedulau'] = cedulau 
        st.session_state['rol'] = rol 
        st.session_state['clave'] =clave 
        switch_page('A-encupaseaca')

    # progress_text = "Operation in progress. Please wait."
    # my_bar = st.progress(0, text=progress_text)
    # for percent_complete in range(10):
    #     time.sleep(0.1)
    #     my_bar.progress(percent_complete + 1, text=progress_text)
    #     st.session_state['nombreu'] = nombreu
    #     st.session_state['cedulau'] = cedulau 
    #     st.session_state['rol'] = rol 
    #     st.session_state['clave'] =clave 
    #     switch_page('encupaseaca')
    # st.write('***')


imagenCer = photosys.get('lineavert02.png')
content = imagenCer.read()
st.image(content)
with st.expander('Descargo de responsabilidad'):
    st.caption('''Descargo de responsabilidad

La aplicación recopila información de los usuarios de la organización. Esta información solo se utilizará por la organización y por los usuarios. La organización no venderá ni cederá esta información a terceros sin el consentimiento previo de los usuarios.

Los usuarios tienen derecho a acceder, rectificar, cancelar y oponerse al tratamiento de sus datos personales. Para ejercer estos derechos, los usuarios pueden ponerse en contacto con la organización a través de la siguiente dirección de correo electrónico: [email protected]

La organización se compromete a tratar los datos personales de los usuarios de acuerdo con la legislación vigente en materia de protección de datos.''')