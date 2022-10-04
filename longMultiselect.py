import streamlit as st

st.markdown("""
    <style>
        .stMultiSelect [data-baseweb=select] span{
            max-width: 400px;
            font-size: 0.6rem;
        }
    </style>
    """, unsafe_allow_html=True)

st.multiselect("pick a long string", 
    [i*25 for i in "ABCDEWXYZ🍿"])
