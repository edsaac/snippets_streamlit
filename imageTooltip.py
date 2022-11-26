import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, JsCode, GridOptionsBuilder

df = pd.DataFrame(
        {"Site": "DuckDuckGo Google Bing".split(),
        "URL": "https://duckduckgo.com/ https://www.google.com/ https://www.bing.com/".split()}
    )

gb = GridOptionsBuilder.from_dataframe(df)

jscode = JsCode("""
    function(params) {
        return '<img src=https://placekitten.com/g/100/100>'
        }
    """)

gb.configure_column("URL",
                    headerName="URL",
                    cellRenderer=jscode,
                    tooltipComponent={"value":10})

gb.configure_auto_height(False)
gridOptions = gb.build()

AgGrid(df, gridOptions=gridOptions, allow_unsafe_jscode=True)