import streamlit as st

"# Checking form fields"
myForm = st.form(key="myForm", clear_on_submit=False)

def checkRequired():
    if not all([st.session_state.input_1,
                st.session_state.input_2, 
                st.session_state.input_3]):
        st.error("Data missing!", icon="⭕")

with myForm:
    st.text_input("Enter something*", key="input_1")
    st.text_input("Enter something else*", key="input_2")
    st.selectbox("Select a number:", 
        [f"{i}" for i in range(1,4)],
        key="input_3")
    st.form_submit_button(on_click=checkRequired)
