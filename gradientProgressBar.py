import streamlit as st
# from streamlit_js_eval import streamlit_js_eval
# from stqdm import stqdm
# from time import sleep

# st.markdown("""
#     <style>
#     .stProgress > div > div > div > div {
#         background: rgb(253,29,29);
#         background: linear-gradient(90deg, rgba(253,29,29,1) 0%, rgba(219,253,29,1) 50%, rgba(98,252,69,1) 100%); 
#     }
#     </style>
#     """,unsafe_allow_html=True)

"## `st.progress()` "
cols = st.columns(3)
with cols[1]:
    "Progress 20%"
    st.progress(20)
    "Progress 50%"
    st.progress(50)
    "Progress 90%"
    st.progress(90)

# "## `stqdm()`"
# for _ in stqdm(range(50),colour='red'):
#     sleep(0.02)

# # stqdm([10,20,50,90], position=10, colour="00ff00")

# expression = '''
# const element = document.querySelector('.stProgress > div > div > div > div');
# element.style.backgroundColor = 'red';
# '''
# streamlit_js_eval(js_expressions=expression)