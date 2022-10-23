import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import time
import cv2
camera = PiCamera()
camera.close()
#camera.open()
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        print("Button 1 was pushed!")
        #break
                    
        #rawCapture.truncate(0) 
        camera.close()
        cv2.destroyAllWindows()
        

    elif GPIO.input(12) == GPIO.HIGH:
        
        print("Button 2 was pushed!")
        # import the necessary packages
        # import the necessary packages
        from picamera.array import PiRGBArray
        from picamera import PiCamera
        import time
        import cv2

        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 32
        rawCapture = PiRGBArray(camera, size=(640, 480))

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

                # if the `q` key was pressed, break from the loop
                if GPIO.input(10) == GPIO.HIGH:
                    break
                    
                    rawCapture.truncate(0) 
        camera.close()
        cv2.destroyAllWindows()

##        with picamera.PiCamera() as camera :
##            
##            try:
##
##    
##                camera.resolution=(1280,720)
##                camera.capture("saaa.jpg" )
##
##                print("Pic taken ")
##            finally:
##                
##                camera.stop_preview()
##                camera.close()
