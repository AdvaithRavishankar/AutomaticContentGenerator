from PIL import Image

def plot_meme(output):
  # Load the image
  image_path = output["file_path"]
  image = Image.open(image_path)
  image.show()