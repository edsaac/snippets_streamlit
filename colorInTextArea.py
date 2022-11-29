import streamlit as st
import matplotlib 

st.markdown("""
    <style>
    .stTextArea [data-baseweb=base-input] {
        background-image: linear-gradient(140deg, rgb(54, 36, 31) 0%, rgb(121, 56, 100) 50%, rgb(106, 117, 25) 75%);
        -webkit-text-fill-color: white;
    }

    .stTextArea [data-baseweb=base-input] [disabled=""]{
        background-image: linear-gradient(45deg, red, purple, red);
        -webkit-text-fill-color: gray;
    }

    /*
    .st-cq {
        background: rgb(253,29,29);
        background: linear-gradient(90deg, rgba(253,29,29,1) 0%, rgba(219,253,29,1) 50%, rgba(98,252,69,1) 100%); 
    }
    */

    </style>
    """,unsafe_allow_html=True)

disable_textarea = st.checkbox("Disable text area:")

st.text_area(
    label="Text area:",
    value="This is a repeated sentence "*20,
    height=300,
    disabled=disable_textarea)

cmap = matplotlib.cm.get_cmap('winter')

# cols = st.columns(3)
# for i,col in zip([10,50,90],cols):
#     rgba = cmap(i/100.0, bytes=True)
#     with col: st.progress(i)
#     st.markdown(f"""<style> .st-dn {{ background: rgba{rgba}; }}*/</style>""",unsafe_allow_html=True)
#     st.write(rgba)

