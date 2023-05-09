import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")


upload_img = st.file_uploader("Upload Image")


with st.expander("Start Camera"):
    # Creates an expandable box 
    cam_image = st.camera_input("Camera")

if cam_image:
    # Fixes the error caused by the browser asking for permission to access camera while the scrips runs anyways. 

    img = Image.open(cam_image)
    # Creates a "pillow" image

    grey_img = img.convert("L")
    # "L" is notation that converts the pillow image to greyscale

    st.image(grey_img)
    # Renders the greyscale image on the webpage

if upload_img:
    img = Image.open(upload_img)
    grey_img = img.convert("L")
    st.image(grey_img)