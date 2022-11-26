import streamlit as st

slider_values = [1,2,3]
slider_strings = ["First option", "Second option", "Third option"]

def stringify(i:int = 0):
    return slider_strings[i-1]

myslider = st.select_slider(
    "String slider",
    options=slider_values,
    value=1,
    format_func=stringify)

st.write(f"## The value of the widgets is the number, not the string: {myslider}")