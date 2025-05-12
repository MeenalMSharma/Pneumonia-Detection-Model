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

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB").resize((224, 224))
        img_array = np.array(image).astype(np.float32) / 255.0

        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Predict"):
            if model is not None:
                input_tensor = np.expand_dims(img_array, axis=0)  # Shape: (1, 224, 224, 3)
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
    output = model.predict(input_tensor)
    class_names = ["Normal", "Pneumonia"]
    return class_names[np.argmax(output)]

if __name__ == "__main__":
    main()
