import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import os

def main():
    st.title("🔬 Pneumonia Detection")
    st.write("Upload a chest X-ray image to detect Pneumonia.")

    # Check if model is loaded in session state
    if "cell_model" not in st.session_state:
        st.session_state.cell_model = load_model()

    # File uploader to upload chest X-ray image
    uploaded_file = st.file_uploader("Choose an X-ray image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Open and preprocess the image
        image = Image.open(uploaded_file).convert("RGB").resize((224, 224))
        img_array = np.array(image) / 255.0  # Normalize the image

        # Display uploaded image
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Predict button
        if st.button("Predict"):
            prediction = predict(img_array)
            st.success(f"Prediction: **{prediction}**")

def predict(img_array):
    model = st.session_state.cell_model
    if model is None:
        return "Model not loaded"

    # Expand dimensions to match model input
    input_tensor = tf.expand_dims(img_array, axis=0)
    
    # Predict the class
    output = model.predict(input_tensor)
    
    # Define class names
    class_names = ["Normal", "Pneumonia"]
    
    # Return prediction
    return class_names[np.argmax(output)]

import tensorflow as tf

def load_model(model_file):
    """Load the model from the uploaded file."""
    try:
        if model_file.name.endswith('.h5'):
            model = tf.keras.models.load_model(model_file)  # For .h5 format
        elif model_file.name.endswith('.keras'):
            model = tf.keras.models.load_model(model_file)  # For .keras format
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

if __name__ == "__main__":
    main()
