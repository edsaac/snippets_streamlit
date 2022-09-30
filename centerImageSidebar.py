import streamlit as st

st.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
            transform: translateX(-50%);
            transition: all 0.4s;
        }

        [data-testid=stSidebar] [data-testid=stImage]:hover {
            opacity: 0.5;
            transform: translateX(0%)
        }
    </style>
    """, unsafe_allow_html=True
)

with st.sidebar:
    "# Center an image in the sidebar"
    "This image is centered in the sidebar"
    st.image("https://placekitten.com/g/200/200")

"Behavior of other images stays unaltered"
st.image("https://placekitten.com/g/500/400")