import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

def main():
    st.title("🔬 Pneumonia Detection")
    st.write("Upload a chest X-ray image and model file to detect Pneumonia.")

    # File uploader for the model
    model_file = st.file_uploader("Upload the trained model (.h5 or .keras)", type=["h5", "keras"])

    # File uploader for the X-ray image
    uploaded_file = st.file_uploader("Choose an X-ray image...", type=["jpg", "jpeg", "png"])

    if model_file is not None:
        model = load_model(model_file)
        if model is not None:
            st.success("Model loaded successfully.")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB").resize((224, 224))
        img_array = np.array(image) / 255.0
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Predict"):
            if model is not None:
                prediction = predict(model, img_array)
                st.success(f"Prediction: **{prediction}**")
            else:
                st.error("Model not loaded. Please upload the model file.")

def load_model(model_file):
    """Load the model from the uploaded file."""
    try:
        # Load the model file into TensorFlow
        model = tf.keras.models.load_model(model_file)
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def predict(model, img_array):
    """Make a prediction with the loaded model."""
    input_tensor = tf.expand_dims(img_array, axis=0)
    output = model.predict(input_tensor)
    class_names = ["Normal", "Pneumonia"]
    return class_names[np.argmax(output)]

if __name__ == "__main__":
    main()
