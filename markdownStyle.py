import streamlit as st

LOGGED_IN = True

"🥪 Desired:"
st.markdown("""___\n
bla bla bla
____""")

"❌ With `    bla bla bla`"
if LOGGED_IN == True:
    st.markdown("""___\n
    bla bla bla
    ____""".replace(" "," "))

"❌ With `    bla bla bla`"
if LOGGED_IN == True:
    st.markdown("""___\n
    bla bla bla
    ____""".replace("    "," "))

"✅ With `bla bla bla`"
if LOGGED_IN == True:
    st.markdown("""___\n
bla bla bla
____""")
