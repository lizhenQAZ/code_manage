# coding:utf-8
import pytesseract
from PIL import Image


im = Image.open('017_pytesseract_code_data.jpg')
# print(im)
data = pytesseract.image_to_string(im)
print(data)
