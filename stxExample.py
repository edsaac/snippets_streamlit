import streamlit as st
import extra_streamlit_components as stx

tab = stx.tab_bar(data=[
    stx.TabBarItemData(id="add", title="➕ Addition", description="Add two numbers"),
    stx.TabBarItemData(id="mult", title="✖ Multiplication", description="Multiply two numbers")])

if tab == "add":
    x = st.number_input('first number', 0, key='first_tab_first_number')
    y = st.number_input('second number', 0, key='first_tab_second_number')
    result = x + y

elif tab == "mult":
    x = st.number_input('first number', 0, key='second_tab_first_number')
    y = st.number_input('second number', 0, key='second_tab_second_number')
    result = x * y

else: 
    result = None

st.write(f"# Result: {result}")

st.warning("""`pip install extra_streamlit_components`""")