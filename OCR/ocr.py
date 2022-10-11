import pytesseract
import shutil
import os
import random
from pytesseract import Output
from PIL import Image
import cv2
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def ImageToText(image):
    image = cv2.resize(image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ans = pytesseract.pytesseract.image_to_data(image ,output_type= Output.DICT)
    return ans