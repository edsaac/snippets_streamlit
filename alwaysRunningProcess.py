from email.mime import image
import streamlit as st
from threading import Thread
from streamlit.runtime.scriptrunner import add_script_run_ctx
import time

def do_stuff(placeholder):
    count = 0
    while count < 25:
        time.sleep(0.1)
        with placeholder:
            st.metric(f"COUNTER", count)
        print(count)
        count += 1

def get_pic():
    with image_placeholder:
        st.image("https://placekitten.com/320/240")

if __name__ == "__main__":

    if "start" not in st.session_state:
        st.session_state.start = False

    if not st.session_state.start:
        cols = st.columns(2)
        with cols[1]:
            placeholder = st.empty()
        with cols[0]:
            image_placeholder = st.empty()
        st.session_state.start = True

    sidebar_counter = Thread(target=do_stuff, args=(placeholder,), daemon=True)
    t = add_script_run_ctx(sidebar_counter)
    t.start()
    #t.join()

    "# Keep process running"
    st.button("Click me", on_click=get_pic)
    t.join()