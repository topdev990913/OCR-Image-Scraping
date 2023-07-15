import cv2

# Read the image
image = cv2.imread("./50_images/LatestCropped_Image_mpv-shot0037.jpg")

# Set the new dimensions
new_width = 311
new_height = 19

# Resize the image
resized_image = cv2.resize(image, (new_width, new_height))

# Save the resized image
cv2.imwrite('resized_image.jpg', resized_image)
cv2.imshow("1", resized_image)
while True:
    pass