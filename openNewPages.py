import streamlit as st
from streamlit.util import open_browser

st.button("Open Google!", 
        key="openWebsite", 
        on_click=open_browser,
        args=[r"https://www.google.com"])