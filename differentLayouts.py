import streamlit as st

st.set_page_config(layout="wide")

st.markdown("""
    <style>
    [data-testid=stVerticalBlock] div:nth-of-type(2) [data-testid=stVerticalBlock]:nth-of-type(1) {
        background-color: Lavender;
        }

    </style>
    """, unsafe_allow_html=True)


top_placeholder = st.container()
bottom_placeholder = st.container()

with top_placeholder:
    "## Top placeholder"
    "This is a repeated text"*20

# with center_placeholder:
#     cols = st.columns(2)
#     with cols[0]:
#         "### Col 0"
#         "Text 88" * 12
#     with cols[1]:
#         "### Col 1"
#         "Text 88" * 12

with bottom_placeholder:
    "## Bottom placeholder"
    "This is a repeated text"*20

