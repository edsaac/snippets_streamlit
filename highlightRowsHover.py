import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

css = """
    <style>

    tr:hover{
        background: yellow;
        font-size: 2rem;
    }

    tr:hover + tr{
        background: blue;
        opacity: 1.0;
    }

    h1:hover ~ tr{
        background: purple;
    }
    </style>
    """

st.markdown(css, unsafe_allow_html=True)

df = pd.DataFrame({'x':np.arange(8),'y':np.geomspace(1, 100, 8)})

st.title("HELLO")
st.table(df)

x_selected = 5
st.title("X:Y = " f"{x_selected} : {df['y'].loc[x_selected]:.3f}")