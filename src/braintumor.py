import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import tempfile

def main():
    st.title("🧠 Brain Tumor Detection")
    st.write("Upload an MRI scan and a trained model file to detect Brain Tumor type.")

    # Upload model
    model_file = st.file_uploader("Upload your trained model (.keras or .h5)", type=["keras", "h5"])

    # Upload image
    uploaded_file = st.file_uploader("Upload a brain MRI scan...", type=["jpg", "jpeg", "png"])

    model = None
    if model_file is not None:
        model = load_model_from_uploaded_file(model_file)
        if model:
            st.success("✅ Model loaded successfully.")
            input_shape = model.input_shape
            st.write(f"Model input shape: {input_shape}")  # Display input shape for debugging

    if uploaded_file is not None:
        try:
            # Open and preprocess the image
            image = Image.open(uploaded_file).convert("RGB")
            image = image.resize((80, 80))  # Resize to match model input size (80x80)
            img_array = np.array(image).astype(np.float32) / 255.0  # Normalize the image

            st.image(image, caption="Uploaded MRI", use_container_width=True)
            st.write(f"Image shape after resize: {img_array.shape}")  # Debug info

            # Check if the model expects a flattened input
            if len(img_array.shape) == 3:
                img_array = img_array.flatten()  # Flatten the image if the model expects a 1D input

            # Add batch dimension
            input_tensor = np.expand_dims(img_array, axis=0)  # Shape: (1, 6400) or whatever model expects

            if input_tensor.shape == (1, 6400):  # Ensure image shape matches expected
                if st.button("Predict"):
                    if model is not None:
                        prediction = predict(model, input_tensor)
                        st.success(f"Prediction: **{prediction}**")
                    else:
                        st.error("Model not loaded. Please upload the model file.")
            else:
                st.error(f"Image shape is incorrect. Expected shape: {input_shape}, but got: {input_tensor.shape}")
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")

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
        class_names = ["Meningioma", "Glioma", "Pituitary", "Normal"]
        predicted_class = class_names[np.argmax(output)]  # Get the class with the highest probability
        return predicted_class
    except Exception as e:
        st.error(f"Prediction error: {str(e)}")
        return None

if __name__ == "__main__":
    main()
