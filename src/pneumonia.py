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
            st.write(f"Model input shape: {model.input_shape}")  # Log the input shape

    if uploaded_file is not None:
        # Open image, convert, and resize to match model input
        image = Image.open(uploaded_file).convert("RGB").resize((224, 224))  # Resize image to 224x224
        img_array = np.array(image).astype(np.float32) / 255.0  # Normalize the image

        # Debugging lines
        st.write(f"Image shape after resize: {img_array.shape}")  # Log image shape after resize

        st.image(image, caption="Uploaded Image", use_container_width=True)

        if st.button("Predict"):
            if model is not None:
                # Add batch dimension: (1, 224, 224, 3)
                input_tensor = np.expand_dims(img_array, axis=0)  
                st.write(f"Input shape before prediction: {input_tensor.shape}")  # Log input shape
                prediction = predict(model, input_tensor)
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
        # Ensure model input compatibility
        st.write(f"Model input shape: {model.input_shape}")  # Log model's expected input shape
        output = model.predict(input_tensor)
        class_names = ["Normal", "Pneumonia"]
        return class_names[np.argmax(output)]
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")
        return None

if __name__ == "__main__":
    main()
