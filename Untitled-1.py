# emotion_detection_app.py

import cv2
import numpy as np
import app as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# Load the pre-trained model
@st.cache_resource
def load_emotion_model():
    try:
        model = load_model("emotion_model.h5")
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Emotion labels
EMOTIONS = ["Angry", "Happy", "Neutral", "Sad"]

# Load Haar cascade for face detection
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Anti-spoofing dummy check (can be extended)
def is_real_face(face_img):
    # Basic anti-spoofing by checking variance in pixel values
    if np.var(face_img) < 10:
        return False
    return True

# Predict emotion from face image
def predict_emotion(face_img, model):
    try:
        face_img = cv2.resize(face_img, (224, 224))
        face_img = face_img.astype("float") / 255.0
        face_img = img_to_array(face_img)
        face_img = np.expand_dims(face_img, axis=0)

        preds = model.predict(face_img)[0]
        label = EMOTIONS[np.argmax(preds)]
        return label, max(preds)
    except Exception as e:
        st.warning(f"Prediction failed: {e}")
        return "Unknown", 0.0

# Streamlit UI
def main():
    st.title("Emotion Detection from Webcam")

    model = load_emotion_model()
    if model is None:
        return

    run = st.checkbox("Start Webcam")
    FRAME_WINDOW = st.image([])

    cap = cv2.VideoCapture(0)

    while run:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to access webcam.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]

            if not is_real_face(face):
                label = "Spoof Detected"
                confidence = 0
            else:
                label, confidence = predict_emotion(face, model)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
            cv2.putText(frame, f"{label} ({confidence:.2f})", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    cap.release()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"Unhandled error: {e}")
