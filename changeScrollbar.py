import streamlit as st
import plotly.express as px

st.markdown("""
    <style>
    
    body {
        scrollbar-width: auto;          /* "auto" or "thin" */
        scrollbar-color: blue orange;   /* scroll thumb and track */ 
    }

    </style>
    """, unsafe_allow_html=True)

fig = px.bar(x=list(range(10)), y=list(range(10)))

fig.update_layout(
    autosize=False,
    width=2000,
    height=500,
)

st.plotly_chart(fig,use_container_width=False)