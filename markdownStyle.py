import streamlit as st

LOGGED_IN = True

"π₯ͺ Desired:"
st.markdown("""___\n
bla bla bla
____""")

"β With `ββββbla bla bla`"
if LOGGED_IN == True:
    st.markdown("""___\n
    bla bla bla
    ____""".replace(" "," "))

"β With `ββββbla bla bla`"
if LOGGED_IN == True:
    st.markdown("""___\n
    bla bla bla
    ____""".replace("    "," "))

"β With `bla bla bla`"
if LOGGED_IN == True:
    st.markdown("""___\n
bla bla bla
____""")
