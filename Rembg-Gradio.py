import gradio as gr
from gradio.components import File, Image
from PIL import Image as PILImage
from rembg import remove

def remove_background(input_file):
    # Open input file and convert to RGBA format
    with PILImage.open(input_file.name) as im:
        im = im.convert("RGBA")
        # Remove background and return processed image data
        return remove(im)

# Define interface
input_file = File(label="Input Image")
output_image = Image(label="Output Image")

# Create Gradio interface
gr.Interface(remove_background, inputs=input_file, outputs=output_image, title="Remove Image Background", allow_flagging="auto").launch()
