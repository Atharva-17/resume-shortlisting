from pdf2image import convert_from_path
from pdf2image import *
import cv2
import os

def filetoimage(file):
    poppler_path = r'C:\\Program Files (x86)\\poppler-22.04.0\\Library\\bin'
    images = convert_from_path(file , poppler_path = poppler_path)
    #print(len(images))
    imagesArray= []
    for i in range(len(images)):
        images[i].save('page'+'.png', 'PNG')
        imagesArray.append(cv2.imread('page.png'))
        file_path = os.getcwd()
        os.remove('page.png')
    #print(len(imagesArray))
    return imagesArray , 
    

