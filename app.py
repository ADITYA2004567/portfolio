import streamlit as st
from emotion_utils import load_model, preprocess_image, predict_emotion, get_emotion_label

st.set_page_config(page_title="Emotion Detection", layout="centered")
st.title("😊 Emotion Detection from Facial Image")

uploaded_file = st.file_uploader("Upload a face image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    model = load_model("emotion_mobilenetv2.pth")
    input_tensor = preprocess_image(uploaded_file)
    prediction = predict_emotion(model, input_tensor)
    emotion_label = get_emotion_label(prediction)

    st.success(f"Predicted Emotion: **{emotion_label}**")
