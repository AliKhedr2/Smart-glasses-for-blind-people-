# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
#To read all images format
from PIL import Image
#OCR Library
import pytesseract
import argparse
# This module is imported so that we can  
# play the converted audio 
import os
# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
import numpy as np
import pygame



image = cv2.imread('/home/pi/Desktop/img1.png',0)
#cv2.imshow("Image", image)
filename = "ss.png".format(os.getpid())
#cv2.imshow("Image", filename)
cv2.imwrite(filename, image)
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
mytext = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
# The text that you want to convert to audio 
print(mytext)
