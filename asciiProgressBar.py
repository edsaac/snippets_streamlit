import streamlit as st
import pandas as pd 

def ascii_progress(x: float, solid: bool = False) -> str:
    '''
    Returns an ascii bar from a number between 0 and 1. 
    The bar has lenght 10
    '''
    nbars = int(min(max(x, 0.0), min(x, 1.0), x) * 10)
    bar = ((("\u2593","\u2588")[solid])*nbars).ljust(10,"\u2591")
    return(bar)

def markdown_progress(x: float) -> str:
    '''
    Returns a bar from a number between 0 and 100. 
    '''
    return(f"""![](https://geps.dev/progress/{x})""")

"### Using unicode blocks"
df = pd.DataFrame({"thing":["Python", "C++", "JS"], "x": [0.2, 0.6, 0.9]})
df["bar"] = df["x"].map(ascii_progress)
st.dataframe(df)

"### With a markdown badge"
df = pd.DataFrame({"thing":["Python", "C++", "JS"], "x": [20, 50, 200]})
df["bar"] = df["x"].map(markdown_progress)
st.markdown(df.to_markdown())

"------"
"$0.0 <= x <= 1.0$"
df = pd.DataFrame({"thing":["Python", "C++", "JS"], "x": [0.1, 0.5, 1.0]})
df["bar"] = df["x"].map(ascii_progress)
st.dataframe(df)

"$0.0 < x < 1.0$"
df = pd.DataFrame({"thing":["Python", "C++", "JS"], "x": [10.1, -10.6, -0.5]})
df["bar"] = df["x"].map(ascii_progress)
st.dataframe(df)