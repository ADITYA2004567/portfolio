import streamlit as st
from PIL import Image
from utils import load_model, preprocess_image, predict_emotion, get_emotion_label

st.set_page_config(page_title="Emotion Detection", layout="centered")

st.title("😊 Emotion Detection from Face")
st.write("Upload a face image to detect the emotion.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("L")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    model = load_model()
    tensor = preprocess_image(image)
    label_idx = predict_emotion(model, tensor)
    emotion = get_emotion_label(label_idx)

    st.success(f"Detected Emotion: **{emotion}**")
