#coding:utf-8
import pytesseract
from PIL import Image

im = Image.open('test.jpg')

data = pytesseract.image_to_string(im)
print (data)