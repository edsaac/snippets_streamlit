import streamlit as st


# title_placeholder = st.container()
# content_placeholder = st.empty()
# errors_placeholder = st.container()

# error = st.checkbox("Error?")

# if error:

#     with errors_placeholder:
#         st.error("Something went wrong")

# with title_placeholder:
#     "# Hello!"

# with content_placeholder.container():
#     st.image("https://placekitten.com/g/400/200",caption=f"Meowhy from here")

if "history_list" not in st.session_state.keys():
    st.session_state.history_list = list()

cols = st.columns(2)
with cols[0]:
    current_placeholder = st.container()
with cols[1]:
    history_placeholder = st.container()

with st.form("my_form"):
    title = st.text_input('Movie title', 'Life of Brian')
    
    if st.form_submit_button("Submit"):
        with current_placeholder:
            st.write(f'The current movie title is **{title}**')
        with history_placeholder:
            st.session_state.history_list.append(title)
            history_placeholder.write(st.session_state.history_list)


