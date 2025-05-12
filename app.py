import streamlit as st
from src import about, home, info, mail, pneumonia
import os

def init():
    
    st.session_state.page = 'Homepage'
    st.session_state.project = False
    st.session_state.model = False
    
    st.session_state.pages = {
        'Homepage': home.main,
        'Pneumonia Detection': pneumonia.main,
        'About the Dataset': info.main,
        'About Us': about.main,
        'Message Us': mail.main
    }
def draw_style():
    style = """
    <style>
    .stApp {
    background-image: url('');  /\* Optional: Add your image URL or leave blank \*/
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    }
    header {visibility: visible;}
    footer {visibility: hidden;} </style>
"""
    st.markdown(style, unsafe_allow_html=True)
    
def load_page():
    if st.session_state.page in st.session_state.pages:
        st.session_state.pages[st.session_state.page]()
    else:
        st.warning("The selected page does not exist!")

def set_page(loc=None, reset=False):
    if st.session_state.page != 'Homepage':
        for key in list(st.session_state.keys()):
            if key not in ('page', 'project', 'model', 'pages'):
                st.session_state.pop(key)

st.session_state.page = loc if loc else st.session_state.get('set', 'Homepage')

if reset:
    st.session_state.project = False
elif st.session_state.page in ('Message Us', 'About Us'):
    st.session_state.project = True
    st.session_state.model = False

def change_button():
    set_page('Pneumonia Detection')
    st.session_state.model = True
    st.session_state.project = True

def main():
    st.set_page_config(page_title='Pneumonia Detection')

if 'page' not in st.session_state:
    init()

draw_style()

with st.sidebar:
    project, about_btn, contact = st.columns([0.8, 1, 1.2])
    
    if not st.session_state.project:
        project.button('Models', on_click=change_button)
    else:
        project.button('Home', on_click=set_page, args=('Homepage', True))

if st.session_state.project and st.session_state.model:
    selected_model = st.radio(
        'Models',
        ['Pneumonia Detection', 'Brain Tumor Detection'],  # Add Brain Tumor as an option
        key='set',
        on_change=set_page,
    )

    about_btn.button('About Us', on_click=set_page, args=('About Us',))
    contact.button('Contact Us', on_click=set_page, args=('Message Us',))
    st.button("About the Dataset", on_click=set_page, args=("About the Dataset",))

    # Optional homepage image
    img_path = "test_files/p1.jpeg"
    img2_path = "test_files/bt1.jpeg"
    img3_path = "test_files/p2.jpeg"
    img4_path = "test_files/bt2.jpeg"
    if st.session_state.page in ['Homepage', 'About the Dataset']:
        if os.path.exists(img_path):
            st.image(img_path)
        else:
            st.warning("No image available.")

        if os.path.exists(img2_path):
            st.image(img2_path)
        else:
            st.warning("No image available.")
load_page()

if __name__ == '__main__':
    main()
