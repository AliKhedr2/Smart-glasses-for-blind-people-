import picamera
from time import sleep


with picamera.PiCamera() as camera :
    camera.start_recording("videoHd.h264")
    sleep(120)
    camera.stop_recording()
