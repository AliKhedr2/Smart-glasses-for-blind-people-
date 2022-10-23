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
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (1280, 720)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(1280, 720))

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array

	# show the frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)

while True:
    # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        
        print("Button was pushed!")
        camera.capture('pic1.png')
        break
cv2.destroyAllWindows()

image = cv2.imread('pic1.png',0)
cv2.imshow("Image", image)
filename = "ss.png".format(os.getpid())
#cv2.imshow("Image", filename)
cv2.imwrite(filename, image)
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
mytext = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
# The text that you want to convert to audio 
print(mytext)

# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 

myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a Wav file named 
# welcome2  
myobj.save("welcome2.wav")
# Playing the converted file 

pygame.init()

pygame.mixer.music.load("welcome2.wav")

pygame.mixer.music.play()


