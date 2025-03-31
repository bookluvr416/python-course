import streamlit as st
from PIL import Image

st.header("Convert Image from Camera")
with st.expander("Start Camera"):
    # get image photo from webcam
    camera_image = st.camera_input("Camera")

# uses screenshot to convert image to greyscale and display on screen
if camera_image:
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.image(gray_img)

st.header("Convert Image from File")
uploaded_image = st.file_uploader("Upload Image")

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)