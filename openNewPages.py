import streamlit as st
import webbrowser

def openTab():
    webbrowser.open_new_tab("https://duckduckgo.com")

if st.button("Open new tab"):
    openTab()