import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import july
from july.utils import date_range

dates = date_range("2020-01-01", "2020-12-31")
data = np.random.randint(0, 100, len(dates))

fig, ax = plt.subplots()
july.month_plot(dates, data, month=2, date_label=True, ax=ax, colorbar=True)

st.title("📊 A `july.month_plot()` in streamlit")
st.pyplot(fig)