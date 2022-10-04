import imp
import streamlit as st
from stqdm import stqdm
from time import sleep

st.markdown("<style>.st-av{height: 200px}</style>", unsafe_allow_html=True)

for _ in stqdm(range(50)):
    sleep(0.5)

for _ in stqdm(range(50)):
    sleep(1)
