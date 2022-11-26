import streamlit as st
import imgkit

@st.cache
def get_screeshot(url):
    # Some options to pass to wkhtmltoimage
    # (More info in the man)
    options = {
        '--crop-h': '500',
        '--format': 'png',
        '--enable-javascript': None,
    }
    return imgkit.from_url(url, False, options=options)

# Add some styling with CSS selectors
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

# Dict of URLS to screenshot
urls = {
    "Search engines": [
        'duckduckgo.com',
        'bing.com',
        'google.com'],
    "Tools": [
        'isocpp.org',
        'wkhtmltopdf.org',
        'www.python.org',
        'placekitten.com',
        'github.com'],
    "Distros": [
        'www.debian.org',
        'linuxmint.com',
        'archlinux.org'],
    "Streamlit apps": [
        'edsaac-adv-processing--cee440-lab1-haq37n.streamlitapp.com',
        'edsaac-adv-processing--cee440-lab1-haq37n.streamlitapp.com?embed=true',
        'discuss.streamlit.io',
        'streamlit.io/gallery']
    }

st.title("🖼️ Gallery of websites")

cols = st.columns([1, 2])
with cols[0]:
    category = st.radio("Categories", urls.keys())

for url in urls[category]:
    screenshot = get_screeshot(url)
    with cols[1]:
        st.markdown(f"#### [{url}](https://{url})")
        st.image(screenshot, use_column_width=True)
        st.caption("Some additional description")
        "*****"

