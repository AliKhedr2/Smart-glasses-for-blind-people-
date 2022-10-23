import cv2
import numpy as np
import imutils
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
pygame.init()

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

cnts=[0]
x=y=0
color=''

lower = {'red':(166, 84, 141), 'green':(66, 122, 129),'black':(0,0,0),'white':(0,0,240) ,
         'blue':(97, 100, 117), 'yellow':(23, 59, 119), 'orange':(0, 50, 80),'brown':(10, 100, 20)}

upper = {'red':(186,255,255), 'green':(86,255,255),'black':(50,50,100),'white':(255,15,255),
         'blue':(117,255,255), 'yellow':(54,255,255), 'orange':(20,255,255),'brown':(20, 255, 200)}

colors = {'red':(0,0,255), 'green':(0,255,0), 'blue':(255,0,0), 'yellow':(0, 255, 217),
          'orange':(0,140,255),'black':(0, 0, 0) ,'white':(255, 255, 255),'brown':(42,42,165)}

kernel = np.ones((9,9),np.uint8)
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(1920, 1080))

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array

    # show the frame
    image = imutils.resize(image, width=600)
    blurred = cv2.GaussianBlur(image, (11, 11), 0)  
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        camera.capture('pic2.png')
        
        

# When everything done, release the capture


        
        im= cv2.imread('pic2.png',0)
        for key, value in upper.items():
            
                
                mask = cv2.inRange(hsv, lower[key], upper[key])
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
                contour = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE)[-2]
                center = None
                
                if len(contour) > 0:
                    areas = max(contour, key=cv2.contourArea)
                    max_index = np.argmax(areas)
                    ((a, b), radius) = cv2.minEnclosingCircle(areas)
                    cnts.append(radius)
                    
                    if cnts[0]>cnts[1]:
                        x,y,color=x,y,color
                    else :
                        x,y,color=a,b,key
                    cnts.remove(min(cnts))
                    radius=cnts[0]
                    
        if cnts[0] > 0.5:
            cv2.circle(image, (int(x), int(y)), int(radius), colors[color], 2)
            cv2.putText(image,color , (int(x-radius),int(y-radius)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6,colors[color],2)
        mytext= color
        print(mytext)
        if mytext == "red":
            
            pygame.mixer.music.load('/home/pi/Desktop/GraduationProject/Records/Colors/Red.mp3')
            pygame.mixer.music.play()

        elif mytext == "yellow":
            
            pygame.mixer.music.load('/home/pi/Desktop/GraduationProject/Records/Colors/yellow.mp3')
            pygame.mixer.music.play()
                
        elif mytext == "black":
            pygame.mixer.music.load('/home/pi/Desktop/GraduationProject/Records/Colors/black.mp3')
            pygame.mixer.music.play()
                
        elif mytext == "brown":
            
            pygame.mixer.music.load('/home/pi/Desktop/GraduationProject/Records/Colors/brown.mp3')
            pygame.mixer.music.play()
                
        elif mytext == "green":
            
            pygame.mixer.music.load('/home/pi/Desktop/GraduationProject/Records/Colors/green.mp3')
            pygame.mixer.music.play()
                
        

        else:
            
            pygame.mixer.music.load('/home/pi/Desktop/GraduationProject/Records/Names/unknown.wav')
            pygame.mixer.music.play()   
            
# Press 'q' to quit
    elif cv2.waitKey(2) == ord('y'):
        
        print("closing camera")
        
        rawCapture.truncate(0)

        camera.close()

        cv2.destroyAllWindows()


##pygame.mixer.music.load("color.mp3")
##
##pygame.mixer.music.play()
##
##             
##cv2.imshow("Frame", image)       
##cv2.waitKey(0) 
##cv2.destroyAllWindows()
##        
##        
