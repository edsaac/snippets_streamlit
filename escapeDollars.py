import streamlit as st

text_with_dollars = "💸 I have $1.00 but I want $2.00 "*20

with st.echo():
    st.write(text_with_dollars)

with st.echo():
    st.write(text_with_dollars.replace("$","\$"))
