import cv2
import os

directory = "images"
files = os.listdir(directory) #I know

file_list = []

for file in files:
    file_path = os.path.join(directory, file)
    file_list.append(file_path)

file_list_str = ', '.join(file_list)
file_list_split = file_list_str.split(", ")

for file_path in file_list_split:
    image = cv2.imread(file_path)
    if image is not None:
        x = 0 # x of top-left cooperate
        y = 3 # y of top-left cooperate
        height = 30 # height to crop
        width = 311 # width to crop
        img1 = image[y: y + height, x: x + width] # cropped image
        cv2.imwrite("cropped/cropped_" + os.path.basename(file_path), img1) # saving the cropped image.