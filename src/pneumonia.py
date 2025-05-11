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
        return "Model not loaded — check logs for why (weights file missing or load error)"

    input_tensor = tf.expand_dims(img_array, axis=0)
    output = model.predict(input_tensor)
    class_names = ["Normal", "Pneumonia"]
    return class_names[np.argmax(output)]

def load_model():
    IMG_SHAPE = (224, 224, 3)
    path = os.path.dirname(os.path.realpath(__file__))
    weights_path = os.path.join(path, 'checkpoints', 'pneumonia_model_weights.weights.h5')
    st.write(f"Looking for weights at: {weights_path}")

    conv_layer = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE, include_top=False, weights="imagenet")
    conv_layer.trainable = False

    model = tf.keras.Sequential([
        conv_layer,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(32, activation="relu"),
        tf.keras.layers.Dense(2, activation="softmax")
    ])

    if not os.path.exists(weights_path):
        st.error(f"Model weights not found at: {weights_path}")
        return None

    try:
        model.load_weights(weights_path)
        st.success("✅ Model weights loaded successfully.")
    except Exception as e:
        st.error(f"❌ Error loading weights: {str(e)}")
        return None

    return model

if __name__ == "__main__":
    main()
