import streamlit as st
import numpy as np
import pickle
from PIL import Image, ImageOps
from tensorflow.keras.models import load_model

# Load the trained model
with open("model_cnn.pkl", "rb") as f:
    model= pickle.load(f)


st.title("MNIST Digit Classifier")

# Upload image
uploaded_file = st.file_uploader("Upload a digit image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("L")   # grayscale

    # User chooses whether to invert
    invert_option = st.checkbox("Invert colors (for white background images)", value=False)
    if invert_option:
        img = ImageOps.invert(img)

    img = img.resize((28, 28))                     # resize to MNIST shape
    img_array = np.array(img) / 255.0              # normalize
    img_array = img_array.reshape(1, 28, 28, 1)    # reshape for CNN

    st.image(img, caption="Processed Image", width=150)

    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)
    st.write("Predicted Digit:", predicted_class)
