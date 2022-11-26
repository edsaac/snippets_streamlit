import streamlit as st

st.markdown(
    """
    <style>
        button[title^=Exit]+div [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
        }
    </style>
    """, unsafe_allow_html=True
)

"# Center an image when in fullscreen"
"Images (and most elements in general) are always aligned to the left"
st.image("https://placekitten.com/g/200/200", caption="Hello!")

#st.image("https://placekitten.com/g/500/500")
