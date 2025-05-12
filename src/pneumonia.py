import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import tempfile

def main():
    st.title("🔬 Pneumonia Detection")
    st.write("Upload a chest X-ray image and a trained model file to detect Pneumonia.")

    # Upload model
    model_file = st.file_uploader("Upload your trained model (.keras or .h5)", type=["keras", "h5"])

    # Upload image
    uploaded_file = st.file_uploader("Upload a chest X-ray image...", type=["jpg", "jpeg", "png"])

    model = None
    if model_file is not None:
        model = load_model_from_uploaded_file(model_file)
        if model:
            st.success("✅ Model loaded successfully.")
            # Log model input shape
            st.write(f"Model input shape: {model.input_shape}")  # Display model input shape
    if uploaded_file is not None:
    # Open image, convert, and resize to match model input
    image = Image.open(uploaded_file).convert("RGB").resize((256, 256))  # Resize image to 256x256
    img_array = np.array(image).astype(np.float32) / 255.0  # Normalize the image

    # Flatten the image if required
    img_array_flattened = img_array.flatten()  # Flatten the image to 1D
    img_array_flattened = np.expand_dims(img_array_flattened, axis=0)  # Add batch dimension (1, 256*256*3)

    # Ensure that the image shape is correct
    st.write(f"Image shape after flattening: {img_array_flattened.shape}")  # Debugging line

    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Predict"):
        if model is not None:
            prediction = predict(model, img_array_flattened)
            st.success(f"Prediction: **{prediction}**")
        else:
            st.error("Model not loaded. Please upload the model file.")

def load_model_from_uploaded_file(uploaded_file):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".keras") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name
        model = tf.keras.models.load_model(tmp_path)
        return model
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        return None

def predict(model, input_tensor):
    try:
        output = model.predict(input_tensor)
        class_names = ["Normal", "Pneumonia"]
        return class_names[np.argmax(output)]
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")
        return None

if __name__ == "__main__":
    main()
