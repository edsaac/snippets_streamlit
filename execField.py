import streamlit as st

x = st.number_input("Number")
code = st.text_input("Code", "y = x**2")
btn_calc = st.button("Calculate!", key="btn_calc")

if btn_calc:
    exec(code)
    st.markdown(rf"## $ x = {{{x}}} \rightarrow y = {{{y}}} $")

