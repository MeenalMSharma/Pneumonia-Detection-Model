from src import about, mail, home, info
import streamlit as st
import os
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained pneumonia detection model
@st.cache_resource()
def load_model():
    return tf.keras.models.load_model("pneumonia_model.h5")

model = load_model()


def init():
    st.session_state.page = 'Homepage'
    st.session_state.project = False
    st.session_state.model = False

    st.session_state.pages = {
        'Homepage': home.main,
        'Pneumonia Detection': home.main,
        'About the Dataset': about.main,
        'About Us': about.main,  # Added this
        'Message Us': mail.main  # Added this
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
    if st.session_state.page in st.session_state.pages:
        st.session_state.pages[st.session_state.page]()
    else:
        st.warning("The selected page does not exist!")

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
    
def preprocess_image(image):
    image = image.convert('L')  # Convert to grayscale if needed
    image = image.resize((224, 224))  # Resize to match model input
    image = np.array(image) / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

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
 st.title("Pneumonia Detection System")
    uploaded_file = st.file_uploader("Upload a Chest X-ray", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded X-ray", use_column_width=True)

        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)

        result = "Pneumonia Detected" if prediction[0][0] > 0.5 else "No Pneumonia"
        st.write(f"Prediction: **{result}**")
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
            img_path = "test_files/IM-0001-0001.jpeg"
            if os.path.exists(img_path):
                st.image(img_path)
            else:
                st.warning(f"Image not found: {img_path}")

    load_page()

if __name__ == '__main__':
    main()
