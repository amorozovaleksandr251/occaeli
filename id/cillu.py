from PIL import Image

# Assuming 'pix' is the PyMuPDF Pixmap object
mode = "RGBA" if pix.alpha else "RGB"
img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
