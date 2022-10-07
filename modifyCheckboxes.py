import streamlit as st

'''
Convert svg to inline css:
- https://www.svgbackgrounds.com/tools/svg-to-css/

SVG sources: 
- https://www.svgrepo.com/svg/17481/lock
- https://www.svgrepo.com/svg/47268/locked
'''

locked_svg = "data:image/svg+xml,%3C%3Fxml version='1.0' encoding='iso-8859-1'%3F%3E%3C!-- Generator: Adobe Illustrator 19.0.0  SVG Export Plug-In . SVG Version: 6.00 Build 0) --%3E%3Csvg version='1.1' id='Layer_1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='0 0 457.952 457.952' style='enable-background:new 0 0 457.952 457.952%3B' xml:space='preserve'%3E%3Cg%3E%3Cg%3E%3Cpath d='M374.006 143.699h-22.645v-21.313C351.361 54.902 296.46 0 228.976 0S106.591 54.902 106.591 122.385v21.313H83.945c-18.121 0-32.864 14.743-32.864 32.865v248.524c0 18.122 14.743 32.865 32.864 32.865h290.06c18.122 0 32.865-14.743 32.865-32.865V176.563C406.871 158.442 392.128 143.699 374.006 143.699z M271.362 143.698h-84.771v-21.313c0-23.371 19.014-42.385 42.386-42.385c23.371 0 42.385 19.014 42.385 42.385V143.698z'/%3E%3C/g%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3C/svg%3E"
unlocked_svg = "data:image/svg+xml,%3C%3Fxml version='1.0' encoding='iso-8859-1'%3F%3E%3C!-- Generator: Adobe Illustrator 19.0.0  SVG Export Plug-In . SVG Version: 6.00 Build 0) --%3E%3Csvg version='1.1' id='Layer_1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' x='0px' y='0px' viewBox='0 0 330 330' style='enable-background:new 0 0 330 330%3B' xml:space='preserve'%3E%3Cg id='XMLID_516_'%3E%3Cpath id='XMLID_517_' d='M15 160c8.284 0 15-6.716 15-15V85c0-30.327 24.673-55 55-55c30.327 0 55 24.673 55 55v45h-25c-8.284 0-15 6.716-15 15v170c0 8.284 6.716 15 15 15h200c8.284 0 15-6.716 15-15V145c0-8.284-6.716-15-15-15H170V85c0-46.869-38.131-85-85-85S0 38.131 0 85v60C0 153.284 6.716 160 15 160z'/%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3Cg%3E%3C/g%3E%3C/svg%3E"

st.markdown(
    fr""" 
    <style>
    /* When checkbox is checked*/
    .st-cp{{
        background-image: url("{locked_svg}");
        background-size: cover;
    }}

    /* When checkbox is not checked*/
    .st-c3 {{
        background-image: url("{unlocked_svg}");
        background-color: #a9dda9;
    }}

    /* When checkbox is not checked but hovered*/
    .st-cr {{
        background-image: url("{unlocked_svg}");
    }}
    </style>
    """, unsafe_allow_html=True)

st.checkbox("One", False)
st.checkbox("Two", True)

'''
Those CSS selectors are not unique to checkboxes.
They will break other elements. 
'''

st.multiselect("Multiselect", [i for i in "ABCD"])
