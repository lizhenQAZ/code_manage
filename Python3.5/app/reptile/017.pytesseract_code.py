# coding:utf-8
import pytesseract
from PIL import Image
import os

base_dir = '017.verification_code'
images = os.listdir(base_dir)
# print(images)
for image in images[1:]:
    image = base_dir + os.sep + image
    im = Image.open(image)
    im = im.convert('P')
    print(im.histogram())
    data = pytesseract.image_to_string(im)
    print(data)
