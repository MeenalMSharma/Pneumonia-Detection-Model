import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import os
import time

def init():
    st.session_state.cell_model = load_model()
    st.session_state.selected = False

def main():
    st.title("Pneumonia Detector")
    st.write("This is the Pneumonia detection module.")
    if "cell_model" not in st.session_state:
        init()
        
    st.title("Pneumonia Detector")
    st.write("### Upload X-Ray Image")

    uploaded_file = st.file_uploader("", type=["jpeg", "png", "jpg"])
    if uploaded_file is not None:
        img = np.array(Image.open(uploaded_file).convert("RGB").resize((224, 224))) / 255
        get_prediction(img)

    if st.session_state.selected:
        prog_bar = st.progress(0)
        for i in range(0, 101, 10):
            time.sleep(0.05)
            prog_bar.progress(i)
        prog_bar.empty()

        st.subheader(f"Prediction: {st.session_state.prediction}")

        blood_cell_info = {
            "Lymphocyte": "A lymphocyte is a type of white blood cell...",
            "Neutrophil": "Neutrophils are the most abundant type of Granulocytes...",
            "Eosinophil": "Eosinophils combat multicellular parasites...",
            "Monocyte": "Monocytes are a type of white blood cell..."
        }

        if st.session_state.prediction in blood_cell_info:
            st.success(f"The model indicates that the blood cell identified is {st.session_state.prediction}. {blood_cell_info[st.session_state.prediction]}")
            st.markdown(f'##### <a href="https://en.wikipedia.org/wiki/{st.session_state.prediction}" target="_blank">Know more 🔗</a>', unsafe_allow_html=True)
        
        st.image(Image.fromarray((st.session_state.img * 255).astype(np.uint8)))

    with st.expander("Don't have any Blood Cell Images?"):
        path = os.path.dirname(os.path.realpath(__file__))
        test_dir = f"{path}/testfinal"

        if not os.path.exists(test_dir):
            st.error("Error: 'testfinal' directory not found. Please ensure the path is correct.")
            return
        
        ims = np.random.choice(os.listdir(test_dir), 3, replace=False)
        labels = []
        images = [np.array(Image.open(f"{test_dir}/{i}").convert("RGB").resize((224, 224))) / 255 for i in ims]

        imgs = st.columns(3)
        for i, img_col in enumerate(imgs):
            label_map = {
                "eos": "Eosinophil",
                "lym": "Lymphocyte",
                "mon": "Monocyte",
                "neu": "Neutrophil"
            }
            label = label_map.get(ims[i][:3], "Unknown")
            labels.append(label)

            img_col.image(images[i])
            if img_col.button(f" ({i+1}) {label}"):
                get_prediction(images[i])

def get_prediction(img):
    if "cell_model" not in st.session_state or st.session_state.cell_model is None:
        st.error("Error: Model failed to load. Check if the checkpoint path is correct.")
        return

    dec = ["Lymphocyte", "Neutrophil", "Eosinophil", "Monocyte"]
    pred = st.session_state.cell_model.predict(tf.data.Dataset.from_tensor_slices([img]).batch(1))
    prediction = dec[np.argmax(pred)]

    st.session_state.prediction = prediction
    st.session_state.img = img
    st.session_state.selected = True

def load_model():
    IMG_SHAPE = (224, 224, 3)
    conv_layer = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE, include_top=False, weights="imagenet")
    conv_layer.trainable = False

    model = tf.keras.Sequential([
        conv_layer,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(32, activation="relu"),
        tf.keras.layers.Dense(4, activation="softmax")
    ])

    path = os.path.dirname(os.path.realpath(__file__))
    weights_path = "Pneumonia_Detection_Model.ipynb"

    if not os.path.exists(weights_path):
        st.error("Error: Model weights not found. Ensure the file exists.")
        return None

    model.load_weights(weights_path)
    return model

if __name__ == "__main__":
    main()
