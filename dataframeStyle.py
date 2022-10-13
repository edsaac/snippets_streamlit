import streamlit as st
import pandas as pd
import numpy as np

# arrays = [
#     ["bar", "bar", "bazzz"],
#     ["one", "two", "one"],
# ]
# tuples = list(zip(*arrays))

# index = pd.MultiIndex.from_tuples(tuples, names=[None, "Brand"])

# df = pd.DataFrame([[1,1,1],[2,3,4]], index=["A", "B"], columns=index)

# # "Adding whitespace with python"
# # st.dataframe(df.style.format("{:.0f}".center(30)))

# "Passing CSS selectors to pandas"
# st.dataframe(
#     df.style
#         .set_table_styles(
#             [{'selector': 'td', 
#               'props': 'font-weight:bold;'}])
#         .format("{:.1f}"),
#     height=200, use_container_width=True)

# st.table(
#     df.style
#         .set_table_styles(
#             [{'selector': 'td:hover', 'props': 'background-color: grey; '}])
#         .format("{:.1f}"))

# st.dataframe(
#     df.style
#         .format("{:.1f}")
#         .background_gradient('viridis'),
#     height=200, use_container_width=True)

# st.markdown(""" 
#     <style>
#         td {
#             background-color: rgba(55,55,55,0.5);
#             text-align: center;
#             vertical-align: middle;
#         }
#     </style>
#     """, unsafe_allow_html=True)

# from streamlit_javascript import st_javascript

# if st.button("Center"):
#     with open("center_td.js") as js:
#         st.code(js.read(), "js")
#         st_javascript(js.read())

# "***************"
# if df not in st.session_state:
#     df = pd.DataFrame([[1, 2], [3, 4], [4, 6]], index=["A1", "A2", "Total"])
#     total_style = pd.Series("text-align: center;", index=["Total"])
#     st.session_state.df = df.style.apply(lambda s: total_style)

# st.dataframe(st.session_state.df)
# st.table(st.session_state.df)

th_props = [
  ('font-size', '14px'),
  ('text-align', 'left'),
  ('font-weight', 'bold'),
  ('color', '#6d6d6d'),
  ('background-color', '#eeeeef'),
  ('border','1px solid #eeeeef'),
  #('padding','12px 35px')
]

td_props = [
  ('font-size', '14px'),
  ('text-align', 'center'),
  ]

cell_hover_props = [  # for row hover use <tr> instead of <td>
    ('background-color', '#eeeeef')
]

styles = [
    dict(selector="th", props=th_props),
    dict(selector="td", props=td_props),
    dict(selector="td:hover",props=cell_hover_props),

]
arrays = [
    ["bar"*5, "bar"*5, "baz"*8, "baz"*8],
    ["one", "two", "one", "two"],
]
tuples = list(zip(*arrays))
index = pd.MultiIndex.from_tuples(tuples, names=[None, "Brand"])
df = pd.DataFrame(np.random.randn(2, 4), index=["A", "B"], columns=index)

with st.echo():
    df_asnumbers = df.style.format("{:.2f}") ## Right-align
    df_asstrings = df.applymap(lambda x:f"{x:.2f}")  ## Left-align

with st.echo():
    "### As numbers:"
    df_styled = df_asnumbers.set_table_styles(styles,overwrite=False).set_properties(**{'text-align':'center'})
    st.table(df_styled)

with st.echo():
    "### As strings:"
    df_styled = df_asstrings.style.set_table_styles(styles,overwrite=False).set_properties(**{'text-align':'center'})
    st.table(df_styled)

with st.echo():
    "### As html:"
    df_html = df_styled.to_html()
    st.components.v1.html(df_html, width=500, height=400)

# ## This does not work
# st.markdown(""" 
#     <style>
#         td {
#             text-align: center;
#         }
#         th {
#             text-align: center;
#             background-color: red;
#         }
#     </style>
#     """, unsafe_allow_html=True)
