import streamlit as st
import matplotlib.pyplot as plt, mpld3

fig, ax = plt.subplots()
ax.plot([3,1,4,1,5], 'rs-', label='My line')
ax.set(xlabel="X axis", ylabel="Y axis")
ax.legend(title="Legend")

htmlfig = mpld3.fig_to_html(fig)

"# 📊 Matplotlib, `mpld3` & streamlit"
st.components.v1.html(htmlfig, height=500)