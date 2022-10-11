import sys
import FILETOIMAGE.pdftoimage as ftoimage
import OCR.ocr as ocr
import os
import PLOTBOX.plotbox as plot

images = ftoimage.filetoimage('resume.pdf')
for i in images:
    input = ocr.ImageToText(i)
    plot.plotSkills(i , input , ['MYSQL' , 'JAVA' , 'FLASK'])