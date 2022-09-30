import streamlit as st

def place_order(tea, flavour, sugar):
    st.success(
        f'''*Order placed:* \n\n **Tea:** {tea} \n\n **Flavour:** {flavour} \n\n **Sugar:** {sugar}
        ''')


selected_flavour = None
selected_sugar = None

selected_tea = st.radio("Type of Tea:", ('Black Tea', 'Red Tea', 'Green Tea', 'Oolong Tea'))

if selected_tea == 'Black Tea':
    selected_flavour = st.selectbox( 'Flavour:', ('Grapefruit', 'Honey'))
    selected_sugar = st.selectbox( 'Sugar Level:', ('50%', '100%'))

elif selected_tea == 'Red Tea':
    selected_flavour = st.selectbox( 'Flavour:', ('Lychee', 'Orange'))
    selected_sugar = st.selectbox( 'Sugar Level:', ('50%', '100%'))

elif selected_tea == 'Green Tea':
    selected_flavour = st.selectbox( 'Flavour:', ('Lemon', 'Melon'))
    selected_sugar = st.selectbox( 'Sugar Level:', ('25%', '50%', '100%'))

elif selected_tea == 'Oolong Tea':
    selected_flavour = st.selectbox( 'Flavour:', ('Honey', 'Pineapple'))
    selected_sugar = st.selectbox( 'Sugar Level:', ('0%', '50%', '100%'))

place_order(selected_tea, selected_flavour, selected_sugar)
