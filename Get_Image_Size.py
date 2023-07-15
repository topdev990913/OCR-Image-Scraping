from PIL import Image
# Open the image file
# image = Image.open("./images/LatestCropped_Image_mpv-shot008.jpg")
image = Image.open("./50_images/LatestCropped_Image_mpv-shot0037.jpg")

# Get the size of the image
width, height = image.size

# Print the size
print(f"Width: {width} pixels")
print(f"Height: {height} pixels")