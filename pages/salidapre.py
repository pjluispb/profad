import streamlit as st
import time
from streamlit_extras.switch_page_button import switch_page

datper = st.session_state['datper']


st.write(datper)
with st.empty():
    for seconds in range(2):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ 2 seconds over!")
switch_page('tdf1')