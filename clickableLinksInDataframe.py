# import streamlit as st
# import pandas as pd
# import plotly.graph_objects as go
# from st_aggrid import AgGrid, JsCode, GridOptionsBuilder

# def create_link(url:str) -> str:
#     return f'''<a href="{url}">🔗</a>'''

# if "df" not in st.session_state:
#     df = pd.DataFrame(
#         {"Site": "DuckDuckGo Google Bing".split(),
#         "URL": "https://duckduckgo.com/ https://www.google.com/ https://www.bing.com/".split()}
#     )
#     df["Link"] = [create_link(url) for url in df["URL"]]
#     st.session_state.df = df

# else: df = st.session_state.df
# ###################################

# option = st.radio("Render as:", ["Plotly", "Ag-Grid", "Markdown"])

# st.header(option)

# if option == "Markdown":
#     st.markdown(df.drop("Link",axis=1).to_html(render_links=True), unsafe_allow_html=True)
#     "****"
#     st.markdown(df.drop("Link",axis=1).style.format({'URL':create_link}).to_html(), unsafe_allow_html=True)

# elif option == "Plotly":
#     fig = go.Figure(
#         data=[
#             go.Table(
#                 columnwidth = [1,1,0.5],
#                 header=dict(
#                     values=[f"<b>{i}</b>" for i in df.columns.to_list()],
#                     fill_color='pink'
#                     ),
#                 cells=dict(
#                     values=df.transpose()
#                     )
#                 )
#             ]
#         )

#     st.plotly_chart(fig, use_container_width=True)

# elif option == "Ag-Grid":

#     #Infer basic colDefs from dataframe types
#     gb = GridOptionsBuilder.from_dataframe(df.drop("Link",axis=1))

#     gb.configure_column("URL",
#                         headerName="URL",
#                         cellRenderer=JsCode(
#                             '''
#                             function(params) {
#                                 return '<a href=' + params.value + '>' + params.value + '</a>'
#                                 }
#                             '''))

#     gridOptions = gb.build()

#     AgGrid(df.drop("Link",axis=1), gridOptions=gridOptions, allow_unsafe_jscode=True)

import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, JsCode, GridOptionsBuilder

df = pd.DataFrame(
        {"Site": "DuckDuckGo Google Bing".split(),
        "URL": "https://duckduckgo.com/ https://www.google.com/ https://www.bing.com/".split()}
    )

gb = GridOptionsBuilder.from_dataframe(df)

gb.configure_column("URL",
                    headerName="URL",
                    cellRenderer=JsCode(
                        """
                        function(params) {
                            return '<a href=' + params.value + '> 🖱️ </a>'
                            }
                        """))

gridOptions = gb.build()

AgGrid(df, gridOptions=gridOptions, allow_unsafe_jscode=True)
