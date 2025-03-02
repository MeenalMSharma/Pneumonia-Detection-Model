from src import about, mail, home, info
import streamlit as st

def init():
    st.session_state.page = 'Homepage'
    st.session_state.project = False
    st.session_state.model = False

    st.session_state.pages = {
        'Pneumonia Detection': home.main,
        'About the Dataset': about.main
    }

def draw_style():
    style = """
        <style>
        .stApp {
            background-image: url("");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }
        header {visibility: visible;}
        footer {visibility: hidden;} 
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)

def load_page():
    st.session_state.pages[st.session_state.page]()

def set_page(loc=None, reset=False):
    if not st.session_state.page == 'Homepage':
        for key in list(st.session_state.keys()):
            if key not in ('page', 'project', 'model', 'pages', 'set'):
                st.session_state.pop(key)

    if loc:
        st.session_state.page = loc
    else:
        st.session_state.page = st.session_state.set

    if reset:
        st.session_state.project = False
    elif st.session_state.page in ('Message Us', 'About Us'):
        st.session_state.project = True
        st.session_state.model = False

def change_button():
    set_page('Pneumonia Detection')
    st.session_state.model = True
    st.session_state.project = True

def prev():
    st.header("Disease Detection Deep Learning Model")

    models = ["Pneumonia Detection"]
    models_info = ["Info about Pneumonia Detection"]
    press = [False] * len(models)
    with st.sidebar:
        st.title("Browse Models")
        for i, model in enumerate(models):
            press[i] = st.sidebar.button(model)
            with st.expander("See Info"):
                st.write(models_info[i])

def main():
    st.set_page_config(page_title='Pneumonia Detection')

    if 'page' not in st.session_state:
        init()

    draw_style()

    with st.sidebar:
        project, about, contact = st.columns([0.8, 1, 1.2])

        if not st.session_state.project:
            project.button('Models', on_click=change_button)
        else:
            project.button('Home', on_click=set_page, args=('Homepage', True))

        if st.session_state.project and st.session_state.model:
            st.radio(
                'Models',
                ['Pneumonia Detection'],
                key='set',
                on_change=set_page,
            )

        about.button('About Us', on_click=set_page, args=('About Us',))
        contact.button('Contact Us', on_click=set_page, args=('Message Us',))
        st.button("About the Dataset", on_click=set_page, args=("About the Dataset",))

        if st.session_state.page == 'Homepage':
            st.image("images/pneumonia.jpg")  # Make sure this image exists

    load_page()

if __name__ == '__main__':
    main()
