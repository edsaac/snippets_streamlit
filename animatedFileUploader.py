import streamlit as st

st.markdown(
    """
    <style>
    [data-testid=stFileUploadDropzone]{
        background-color : rgba(164, 179, 224,0.5);
    }

    .cat{
        position: absolute;
        border-style: solid;
        border-color: red;
        top: 20%;
        right: 20%;
        width: 150px;
        height: 150px;
        background-color: rgba(164, 179, 224,0.5);
        background-origin: content-box;
    }   
    </style>
    """, unsafe_allow_html=True
)

st.markdown(
    """
    <div class="cat">
    </div>    
    """, unsafe_allow_html=True
)

"# Title of the page"
"Some repeating text."*50

def printSomething():
    st.markdown(
    """
    <style>
    .cat{
        animation: crash 5s ease-in forwards;
    }

    @keyframes crash{
        0%{
            translate: 0;
            background-image: url('https://media.tenor.com/pjhiPPbQwGYAAAAi/cat-meow.gif');
        }

        49%{
            translate: -200px;
            background-image: url('https://media.tenor.com/pjhiPPbQwGYAAAAi/cat-meow.gif');
        }
        50%{
            width: 90px;
            height: 126px;
            background-image: url('https://media.tenor.com/j-ixpElDGOYAAAAi/explode-boom.gif');
        }

        99%{
            translate: -200px;
            width: 90px;
            height: 126px;
            background-image: url('https://media.tenor.com/j-ixpElDGOYAAAAi/explode-boom.gif');
        100%{
            translate: -200px;
            width: 90px;
            height: 126px;
        }
    }
    </style>
    """, unsafe_allow_html=True
)

st.file_uploader("Upload a file","JPG",False,"fileup",
    on_change=printSomething)



