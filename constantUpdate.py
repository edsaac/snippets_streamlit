import streamlit as st
import numpy as np
import pandas as pd
from time import sleep

df = pd.DataFrame({'x':np.arange(15),'y':np.random.normal(size=15)})
df.set_index('x',inplace=True)

placeholder = st.empty()
constant_update = st.checkbox("Keep updating")

while constant_update:
    df['y'] = np.random.normal(size=15)
    sleep(0.1)
    placeholder.line_chart(df)
else:
    placeholder.line_chart(df)