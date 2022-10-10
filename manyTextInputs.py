import streamlit as st
import pandas as pd

number_inputs = st.number_input('number of nr fields', step=1, min_value=1)
st.write('number of nr fields ', number_inputs)

data = pd.DataFrame(columns=['nr'])

if 'df' not in st.session_state:
    st.session_state.df = data

input_values = [st.text_input(f'nr {i}', i+1, key=f"text_input_{i}")
          for i in range(number_inputs)]

if st.button("Add to df", key="button_update"):
    # Update dataframe state
    st.session_state.df = pd.concat(
        [st.session_state.df, pd.DataFrame({'nr': input_values})],
        ignore_index=True)
    st.text("Updated dataframe")

"## Dataframe state:"
st.dataframe(st.session_state.df)
