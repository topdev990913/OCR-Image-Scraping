import cv2
import os
from PIL import Image
directory = "50_images"
files = os.listdir(directory) #I know

file_list = []

for file in files:
    file_path = os.path.join(directory, file)
    file_list.append(file_path)

file_list_str = ', '.join(file_list)
file_list_split = file_list_str.split(", ")

for file_path in file_list_split:
    image = cv2.imread(file_path)
    image1 = Image.open(file_path)
    width, height = image1.size
    # print(f"Width: {width} pixels")
    # print(f"Height: {height} pixels")
    if image is not None:   
        if height>=15:     
            x = 0 # x of top-left cooperate
            y = 3 # y of top-left cooperate
            height = 16 # height to crop
            width = 311 # width to crop
            img1 = image[y: y + height, x: x + width] # cropped image
        else:
            img1 = image
        cv2.imwrite("cropped/cropped_" + os.path.basename(file_path), img1) # saving the cropped image.
        
