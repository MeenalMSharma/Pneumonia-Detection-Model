import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import os

def main():
    st.title("🔬 Pneumonia Detection")
    st.write("Upload a chest X-ray image to detect Pneumonia.")

    if "cell_model" not in st.session_state:
        st.session_state.cell_model = load_model()

    uploaded_file = st.file_uploader("Choose an X-ray image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB").resize((224, 224))
        img_array = np.array(image) / 255.0

        st.image(image, caption='Uploaded Image', use_column_width=True)

        if st.button("Predict"):
            prediction = predict(img_array)
            st.success(f"Prediction: **{prediction}**")

def predict(img_array):
    model = st.session_state.cell_model
    if model is None:
        return "Model not loaded"

    input_tensor = tf.expand_dims(img_array, axis=0)
    output = model.predict(input_tensor)
    class_names = ["Normal", "Pneumonia"]
    return class_names[np.argmax(output)]

def load_model():
    IMG_SHAPE = (224, 224, 3)
    base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE, include_top=False, weights="imagenet")
    base_model.trainable = False

    model = tf.keras.Sequential([
        base_model,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(32, activation="relu"),
        tf.keras.layers.Dense(2, activation="softmax")
    ])

    path = os.path.dirname(os.path.realpath(__file__))
    weights_path = os.path.join(path, '..', 'checkpoints', 'pneumonia_model_weights.weights.h5')
    weights_path = os.path.abspath(weights_path)

    if os.path.exists(weights_path):
        try:
            model.load_weights(weights_path)
        except Exception as e:
            st.error(f"Failed to load weights: {e}")
            return None
    else:
        st.error(f"Model weights not found at: {weights_path}")
        return None

    return model
