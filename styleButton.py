import streamlit as st

st.markdown("""
<style>
    .stButton button {
        background-color: white;
        font-weight: bold;
        width: 50px;
        border: 2px solid green;
    }

    .stButton button:hover {
        background-color:#018749;
        color: black;
    }

</style>
""", unsafe_allow_html=True)

with st.sidebar:
    "## This is the sidebar"
    cols = st.columns(5)
    for i,col in enumerate(cols):
        with col:
            st.button(f"{i}", key=f"btn_{i}")
