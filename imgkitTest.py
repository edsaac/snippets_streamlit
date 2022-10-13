import streamlit as st
import imgkit

st.markdown("""
    <style>
    img {
        border-radius: 10px;
        border: solid 1px #dadee8;
    }

    a[href] {
        text-decoration: none;
        color: #ff4b4b;
    }

    h1 {
        font-size: 5rem;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

urls = {
    "Search engines": [
        'duckduckgo.com',
        'bing.com',
        'google.com'],
    "Tools": [
        'streamlit.io',
        'wkhtmltopdf.org',
        'www.python.org'],
    "Linux distros": [
        'www.debian.org',
        'linuxmint.com',
        'archlinux.org'
    ],
    "Repositories": [
        'github.com',
        'gitlab.com'
    ]}

options = {
    '--crop-h':'500', 
    '--format':'png',
    '--enable-javascript': None,
    }

st.title("🖼️ Gallery of websites")

cols = st.columns([1,2])
with cols[0]: 
    category = st.radio("Categories", urls.keys())

for url in urls[category]:
    screenshot = imgkit.from_url(url, False, options=options)

    with cols[1]: 
        st.markdown(f"#### [{url}](https://{url})")
        st.image(screenshot, use_column_width=True)
        st.caption("Some additional description")
        "*****"
