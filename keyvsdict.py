import streamlit as st

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0), key="myvalues")

st.write(values)
st.write(st.session_state["myvalues"])
st.write(st.session_state.myvalues)