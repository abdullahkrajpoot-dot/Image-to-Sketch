import streamlit as st
import cv2
import numpy as np
from PIL import Image

# 1. Front-end ki Settings
st.set_page_config(page_title="AI Sketcher Pro", layout="centered")
st.title("🎨 AI Image-to-Sketch Converter")
st.subheader("Upload any photo and let AI do the sketching!")

# 2. File Upload ka Dashboard
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Image ko process karna (Backend Logic)
    image = Image.open(uploaded_file)
    img_array = np.array(image)
    
    # Processing Message
    with st.spinner('AI is sketching...'):
        # OpenCV logic
        grey_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        inverted_img = cv2.bitwise_not(grey_img)
        blurred = cv2.GaussianBlur(inverted_img, (21, 21), 0)
        inverted_blurred = cv2.bitwise_not(blurred)
        sketch = cv2.divide(grey_img, inverted_blurred, scale=256.0)
        
        # Front-end par result dikhana
        col1, col2 = st.columns(2)
        with col1:
            st.image(image, caption="Original Photo", use_container_width=True)
        with col2:
            st.image(sketch, caption="AI Sketch Result", use_container_width=True)
            
        # Download Button
        # Sketch ko wapis image format mein badalna taake user save kar sakay
        _, buffer = cv2.imencode('.jpg', sketch)
        st.download_button(label="Download Sketch", data=buffer.tobytes(), file_name="sketch.jpg", mime="image/jpeg")

st.info("Built with Python & OpenCV - No external APIs used.")