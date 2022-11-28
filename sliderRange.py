import streamlit as st
list_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

getColor = lambda i: list_colors[i]

all_colors_in_range = st.select_slider(
    'Select a subset of colors of the rainbow',
    options= range(len(list_colors)),
    value=(1,4),
    format_func=getColor)

st.write('My favorite color is', ", ".join(list_colors[all_colors_in_range[0]:all_colors_in_range[1]+1]))

"****"

single_color = st.select_slider(
    'Select a single color of the rainbow',
    options= list_colors,
    value='orange')

st.write('My favorite color is', single_color)

"*****"

two_colors = st.select_slider(
    'Select two colors of the rainbow',
    options= list_colors,
    value=('orange','blue'))

st.write('My favorite color is', two_colors)