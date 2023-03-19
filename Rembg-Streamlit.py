import streamlit as st
import rembg
from rembg import remove
from PIL import Image
import urllib.request
from io import BytesIO

def main():
    col1, col2,col3 = st.columns(3)
    st.title("Arka Plan Kaldırma")
    st.write("Resmi yükle ve arka plan kalksın. Tek yapman gerelen indirme düğmesine basman :cat:")
    col1.write("## Yükle, Düzelt ve İndir :gear:")
    
    uploaded_files = col1.file_uploader("Arka planını kaldırmak istediğin resimleri seç", accept_multiple_files=True)

    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file)
            col2.image(image, caption=f'Original Image: {uploaded_file.name}', use_column_width=True)

            # Remove the background
            # image_data = remove(image.convert("RGBA"),
            #                     alpha_matting=True,
            #                     alpha_matting_foreground_threshold=240,
            #                     alpha_matting_background_threshold=10)
            image_data = remove(image.convert("RGBA"))

            # Display the processed image
            col3.image(image_data, caption=f'Processed Image: {uploaded_file.name}', use_column_width=True)

            # Download the processed image
            col1.download_button(f'Düzeltilmiş Resmi İndir: {uploaded_file.name}', download_image(image_data, uploaded_file.name), f'processed_{uploaded_file.name}')

def download_image(image_data, filename):
    with BytesIO() as buffer:
        image_data.save(buffer, format="PNG")
        return buffer.getvalue()


if __name__ == '__main__':
    main()
