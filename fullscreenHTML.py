import streamlit as st
from streamlit.util import open_browser

st.image("https://placekitten.com/g/800/600")

"*****"

with open("someHTML.html") as f:
    st.components.v1.html(f.read(), height=400)

st.button("Open Google", key="Open", on_click=open_browser, args=[r"https://www.google.com"])