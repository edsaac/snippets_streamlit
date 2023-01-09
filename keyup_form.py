import streamlit as st
from st_keyup import st_keyup

if not "name" in st.session_state:
    st.session_state.name = ""

name = st_keyup("Enter user name", value=st.session_state.name)
st.session_state.name = name.lower()
st.write(f"The username is {st.session_state.name}")
