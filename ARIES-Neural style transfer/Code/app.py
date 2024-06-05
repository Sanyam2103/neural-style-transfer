import streamlit as st
from PIL import Image
import os
from NST import NST

st.title("Neural Style Transfer")
st.markdown("""
Welcome to the **Neural Style Transfer**! Transform your images into works of art by blending the content of one image with the style of another using deep learning.
Upload your **content image** and **style image** below, then click the 'Style' button to create your own masterpiece!
""")

def save_uploaded_file(uploaded_file, filename):
    try:
        with open(filename, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return True
    except Exception as e:
        print(e)
        return False

content_img = st.file_uploader("Upload Content Image", type=["png", "jpg", "jpeg"])
if content_img is not None:
    if save_uploaded_file(content_img, "content_img.png"):
        st.image(content_img, caption="Content Image", use_column_width=True)

style_img = st.file_uploader("Upload Style Image", type=["png", "jpg", "jpeg"])
if style_img is not None:
    if save_uploaded_file(style_img, "style_img.png"):
        st.image(style_img, caption="Style Image", use_column_width=True)

if st.button("Style"):
    st.write("Styling in progress...wait for 5-10 minutes")
    NST('content_img.png','style_img.png')
    

    if os.path.exists("stylised_image.png"):
        styled_image = Image.open("stylised_image.png")
        st.image(styled_image, caption="Styled Image", use_column_width=True)
        
        with open("stylised_image.png", "rb") as file:
            btn = st.download_button(
                label="Download Styled Image",
                data=file,
                file_name="stylised_image.png",
                mime="image/png"
               
                
            )

