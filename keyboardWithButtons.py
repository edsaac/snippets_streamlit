import streamlit as st

def keyboard():
    st.write(""" ## Keyboard""")
    kb_line1 = st.empty()
    q, w, e, r, t, y, u, i, o, p, dummy_0,  = st.columns(11)
    user_input_dialog = st.empty()

    q_btn, w_btn, e_btn, r_btn, t_btn = q.button("Q"), w.button("W"), e.button("E"), r.button("R"), t.button("T")
    y_btn, u_btn, i_btn, o_btn, p_btn = y.button("Y"), u.button("U"), i.button("I"), o.button("O"), p.button("P")

    user_input=""

    if q_btn:
        user_input = "Q"
    if w_btn:
        user_input = "W"
    if e_btn:
        user_input = "E"
    if r_btn:
        user_input = "R"
    if t_btn:
        user_input = "T"
    if y_btn:
        user_input = "Y"
    if u_btn:
        user_input = "U"
    if i_btn:
        user_input = "I"
    if o_btn:
        user_input = "O"
    if p_btn:
        user_input = "P"

    if user_input != "" :
        user_input_dialog.write(""" ## You selected: """+user_input)

if __name__ == "__main__" :
    keyboard()