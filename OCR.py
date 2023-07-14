import cv2, os
import numpy as np
import pytesseract
import easyocr
def with_easyocr(image_path):
    reader = easyocr.Reader(["en"], gpu=False)
    image = cv2.imread(image_path, 0)
    (h, w) = image.shape
    black_image = np.zeros((h * 9, w + 400 ), np.uint8)
    black_image[4 * h: 5 * h, 200: w + 200] = image
    ret, black_image = cv2.threshold(black_image, 200, 255, cv2.THRESH_BINARY)
    if w > 1000:
        kernel = np.ones((5, 5), np.uint8)
        black_image = cv2.erode(black_image, kernel=kernel)
    else:
        kernel = np.ones((2, 2), np.uint8)
        black_image = cv2.erode(black_image, kernel=kernel)
    results = reader.readtext(
        black_image,
        decoder="greedy",
        detail=0,
        paragraph=True,
        y_ths=0.1,
        allowlist="0123456789/:",
        rotation_info=[90],
    )
    # result_text = ""
    # for result in results:
    #     txts = []
    #     for line in result:
    #         result_text += line[1][0]
    # print (results[0])
    cv2.imshow("1", black_image)
    cv2.waitKey(0)
    return  results[0]
def with_tesseract(image_path):
    image = cv2.imread(image_path, 0)
    (h, w) = image.shape
    black_image = np.zeros((h * 5, w + 100 ), np.uint8)
    black_image[2 * h: 3 * h, 50: w + 50] = image
    kernel = np.ones((5, 5), np.uint8)
    black_image = cv2.erode(black_image, kernel=kernel)
    resultText = pytesseract.image_to_string(black_image)
    cv2.imshow("1", black_image)
    cv2.waitKey(0)
    return resultText
def _main():
    root_dir = "cropped"
    image_names = os.listdir(root_dir)
    result_text = " "
    replacement = ":"
    for image_name in image_names:
        image_path = os.path.join(root_dir, image_name)
        # text = with_tesseract(image_path)
        text = with_easyocr(image_path)
        try:
            new_text = text
            if len(str(text).split(" "))!=2:
                index = text.find(" ", text.find(" ") + 1)
                new_text = text[:index] + replacement + text[index+1:]
            else:
                pass
            if len(str(new_text).split(" "))==3:
                index = new_text.find(" ", new_text.find(" ") + 1)
                new_text = new_text[:index] + replacement + new_text[index+1:]
            else:
                pass
            # index1 = new_text.find(" ", new_text.find(" ") + 2)
            # new_text1 = new_text[:index] + replacement + new_text[index+2:]
        except:
            pass
        print(new_text)
        result_text += image_name + " : " + new_text + " \n"
    with open("result.txt", 'w') as f:
        f.write(result_text)
    return
if __name__ == "__main__":
    _main()