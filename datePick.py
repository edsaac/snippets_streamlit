import streamlit as st
import locale 
from contextlib import contextmanager

@contextmanager
def change_locale(locale_str:str):
    locale.setlocale(locale.LC_ALL, locale_str)
    yield
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')

def create_summary(d):
    f"""
|Format|Code | Output|
|---|---|---:|
|Default|`d`| {d}|
|Custom long|`d.strftime(r'%A, %B %d, %Y')`|{d.strftime(r'%A, %B %d, %Y')}|
|Custom short|`d.strftime(r'🗓️ %y⚬%m⚬%d🗓️')`|{d.strftime(r'🗓️ %y⚬%m⚬%d🗓️')}|

-----
"""

st.markdown("""
    <style>
    .stDateInput input{
        placeholder:"MM/DD/YYYY"
    }
    </style>
""", unsafe_allow_html=True)


with st.echo(): 
    d = st.date_input("Date input", value = None)

"----"

"#### 🇺🇸 `d` will be formated according to my default locale:"
create_summary(d)

"#### 🇫🇷 `d` could be formated using another locale:"
with st.echo():
    with change_locale('fr_FR.utf8'):
        create_summary(d)

"#### 🇪🇸 otro ejemplo:"
with st.echo():
    with change_locale('es_ES.utf8'):
        create_summary(d)

"#### 🇩🇪 but this one will fail because German is not installed:"
with st.echo():
    with change_locale('de_DE.utf8'):
        create_summary(d)

# """### 🇩🇪 But the locale must be installed in your system, for example, 
# this one will fail because of that:"""
# with st.echo():
#     locale.setlocale(locale.LC_ALL, 'de_DE.utf8')

# create_summary(d)