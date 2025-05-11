import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import os

def init():
    st.session_state.cell_model = load_model()

def main():
    st.title("Pneumonia Detector")
    st.write("Upload a chest X-ray to detect Pneumonia.")

    if "cell_model" not in st.session_state:
        init()

    uploaded_file = st.file_uploader("Choose an X-ray image", type=["jpeg", "png", "jpg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB").resize((224, 224))
        img_array = np.array(image) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        pred = st.session_state.cell_model.predict(img_array)
        classes = ["Normal", "Pneumonia"]
        prediction = classes[np.argmax(pred)]

        st.image(image, caption="Uploaded X-ray", width=300)
        st.success(f"Prediction: {prediction}")

def load_model():
    IMG_SHAPE = (224, 224, 3)
    conv_layer = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE, include_top=False, weights="imagenet")
    conv_layer.trainable = False

    model = tf.keras.Sequential([
        conv_layer,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(32, activation="relu"),
        tf.keras.layers.Dense(2, activation="softmax")  # ✅ Corrected to match 2-class output
    ])

    path = os.path.dirname(os.path.realpath(__file__))
    weights_path = os.path.join(path, 'checkpoints', 'pneumonia_model_weights.weights.h5')

    if not os.path.exists(weights_path):
        st.error(f"Error: Model weights not found at: {weights_path}")
        return None

    try:
        model.load_weights(weights_path)
    except Exception as e:
        st.error(f"Error loading weights: {str(e)}")
        return None

    return model

if __name__ == "__main__":
    main()
