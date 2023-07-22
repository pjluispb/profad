
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



df = pd.DataFrame(
    [
       {"command": "Estudio Secundaria: Liceo Tulio Febres Cordero en Colon, estado Tachira, Liceo Fray Juan Ramos de Lora en Merida, estado Merida", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)

edited_df = st.data_editor(df, 
    column_config={
        "command": st.column_config.TextColumn(
            "command",
            help="Streamlit **widget** commands 🎈",
            default="st.",
            width=5000,
            max_chars=200,
            validate="^st\.[a-z_]+$",
        )
    },
    hide_index=True,)
#edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")