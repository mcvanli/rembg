import streamlit as st
from rembg import remove
from PIL import Image
import urllib.request
from io import BytesIO

def main():
    st.title("Background Remover")

    uploaded_files = st.file_uploader("Choose one or more image files", accept_multiple_files=True)

    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            st.image(image, caption=f'Original Image: {uploaded_file.name}', use_column_width=True)

            # Remove the background
            # image_data = remove(image.convert("RGBA"),
            #                     alpha_matting=True,
            #                     alpha_matting_foreground_threshold=240,
            #                     alpha_matting_background_threshold=10)
            image_data = remove(image.convert("RGBA"))

            # Display the processed image
            st.image(image_data, caption=f'Processed Image: {uploaded_file.name}', use_column_width=True)

            # Download the processed image
            st.download_button(f'Download processed image: {uploaded_file.name}', download_image(image_data, uploaded_file.name), f'processed_{uploaded_file.name}')

def download_image(image_data, filename):
    with BytesIO() as buffer:
        image_data.save(buffer, format="PNG")
        return buffer.getvalue()


if __name__ == '__main__':
    main()
