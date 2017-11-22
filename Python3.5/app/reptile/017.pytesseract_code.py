# coding:utf-8
import pytesseract
from PIL import Image
import os

base_dir = '017.verification_code'
images = os.listdir(base_dir)
# print(images)
for image in images:
    image = base_dir + os.sep + image
    im = Image.open(image)
    # print(im)
    data = pytesseract.image_to_string(im)
    print(data)
