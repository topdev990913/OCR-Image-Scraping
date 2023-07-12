import cv2
import pytesseract

# Load the image
image = cv2.imread('LatestCropped_Image_mpv-shot003.jpg')

# Preprocess the image
resized_image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# Apply image processing techniques
threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
denoised_image = cv2.fastNlMeansDenoising(threshold_image, None, 10, 7, 21)

# Use OCR to extract the text
text = pytesseract.image_to_string(denoised_image)

# Process the extracted text as per your needs

# Print the extracted text
print(text)