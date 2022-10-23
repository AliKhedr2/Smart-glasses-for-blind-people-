import picamera

with picamera.PiCamera() as camera :
    camera.resolution=(1280,720)
    camera.capture("saaa.jpg" )

print("Pic taken ")
