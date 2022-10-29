import streamlit as st
from time import sleep

def showSuccess(t:int):
    placeholder.success("Success!")
    sleep(t)
    placeholder.empty()

"# My awesome app"
placeholder = st.empty()
with st.form("My form"):
    f"## My form to wait {(t:=2)} s"
    wait_button = st.form_submit_button(f"Submit wait", on_click= showSuccess, args=[t])

"-----"
"### Some other content"
"Some repeated text 🐏"*50
st.image("https://placekitten.com/g/100/120")