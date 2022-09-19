import streamlit as st
import datetime

d = st.date_input(
    "Date input",
    value = None
#     min_value=datetime.date.min,
#     max_value=datetime.date.max
 )

st.write(datetime.date.min)
st.write(datetime.date.max)