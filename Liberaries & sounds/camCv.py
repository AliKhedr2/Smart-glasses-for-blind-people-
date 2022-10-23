# import the necessary packages
from picamera.array import PiRGBArray
import picamera
import time
import cv2


with picamera.PiCamera() as camera :
    
    try:
        
        # initialize the camera and grab a reference to the raw camera capture
        #camera = PiCamera()
        rawCapture = PiRGBArray(camera)

        # allow the camera to warmup
        time.sleep(0.1)

        # grab an image from the camera
        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array

        # display the image on screen and wait for a keypress
        #cv2.imshow("Image", image)
        
        ##cv2.destroyAllWindows()
        
        
        #camera.start_preview()
            #DoCameraRelatedStuff
    finally:
        
        camera.stop_preview()
        camera.close()
