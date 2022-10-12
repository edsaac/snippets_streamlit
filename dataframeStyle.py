import streamlit as st
import pandas as pd
import numpy as np

arrays = [
    ["bar", "bar", "bazzz"],
    ["one", "two", "one"],
]
tuples = list(zip(*arrays))

index = pd.MultiIndex.from_tuples(tuples, names=[None, "Brand"])

df = pd.DataFrame([[1,1,1],[2,3,4]], index=["A", "B"], columns=index)

# "Adding whitespace with python"
# st.dataframe(df.style.format("{:.0f}".center(30)))

"Passing CSS selectors to pandas"
st.dataframe(
    df.style
        .set_table_styles(
            [{'selector': 'td', 
              'props': 'font-weight:bold;'}])
        .format("{:.1f}"),
    height=200, use_container_width=True)

st.table(
    df.style
        .set_table_styles(
            [{'selector': 'td:hover', 'props': 'background-color: grey; '}])
        .format("{:.1f}"))

st.dataframe(
    df.style
        .format("{:.1f}")
        .background_gradient('viridis'),
    height=200, use_container_width=True)

st.markdown(""" 
    <style>
        td {
            background-color: rgba(55,55,55,0.5);
            text-align: center;
            vertical-align: middle;
        }
    </style>
    """, unsafe_allow_html=True)

from streamlit_javascript import st_javascript

if st.button("Center"):
    with open("center_td.js") as js:
        st.code(js.read(), "js")
        st_javascript(js.read())

"***************"
if df not in st.session_state:
    df = pd.DataFrame([[1, 2], [3, 4], [4, 6]], index=["A1", "A2", "Total"])
    total_style = pd.Series("text-align: center;", index=["Total"])
    st.session_state.df = df.style.apply(lambda s: total_style)

st.dataframe(st.session_state.df)
st.table(st.session_state.df)