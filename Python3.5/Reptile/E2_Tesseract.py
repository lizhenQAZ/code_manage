# coding:utf-8
import pytesseract
from PIL import Image


im = Image.open('E2_Test.jpg')
print(im)
data = pytesseract.image_to_string(im)
print(data)
