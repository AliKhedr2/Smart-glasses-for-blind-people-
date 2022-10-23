# Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO
# Import Raspberry Pi Camera library
from picamera.array import PiRGBArray
from picamera import PiCamera
# Import Raspberry Pi Audio library
import pygame
# Import the required module for text  
# to speech conversion 
from gtts import gTTS
import os 
# Import OpenCv Library
import cv2
import time

pygame.init()

pygame.mixer.music.load("/home/pi/Desktop/GraduationProject/Records/Buttons/welcome.mp3")
camera = PiCamera()
camera.close()
pygame.mixer.music.play()
print("played")

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

# Set pins 8,10,12 ,16 ,18 ,22 ,24 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  #On \ Off
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #time
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #face
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Object
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Bill
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Color
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #OCR
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Capture

while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        camera = PiCamera()
        pygame.mixer.music.load("/home/pi/Desktop/GraduationProject/Records/Buttons/time.mp3")
        pygame.mixer.music.play()
        print("played")
        
        import time
        from datetime import datetime
        #rawCapture.truncate(0) 
        camera.close()
        cv2.destroyAllWindows()


        mytext = time.asctime( time.localtime(time.time()) )

        #mytext = date_time.strftime("%c")
        print("Output 1:", mytext)	
          
        # Language in which you want to convert 
        language = 'en'
          
        # Passing the text and language to the engine,  
        # here we have marked slow=False. Which tells  
        # the module that the converted audio should  
        # have a high speed 
        myobj = gTTS(text=mytext, lang=language, slow=False) 
          
        # Saving the converted audio in a mp3 file named 
        # welcome  
        myobj.save("timee.mp3")
        pygame.init()

        pygame.mixer.music.load("timee.mp3")

        pygame.mixer.music.play()
        print("played")
        
        
        
    elif GPIO.input(26) == GPIO.HIGH:
        
        pygame.mixer.music.load("/home/pi/Desktop/GraduationProject/Records/Buttons/face.mp3")
        pygame.mixer.music.play()
        print("played")

        
            
        
        # This is a demo of running face recognition on a Raspberry Pi.
        # This program will print out the names of anyone it recognizes to the console.

        # To run this, you need a Raspberry Pi 2 (or greater) with face_recognition and
        # the picamera[array] module installed.
        # You can follow this installation instructions to get your RPi set up:
        # https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65

        import face_recognition
        import picamera
        import numpy as np
        import pygame
        pygame.init()

        # Get a reference to the Raspberry Pi camera.
        # If this fails, make sure you have a camera connected to the RPi and that you
        # enabled your camera in raspi-config and rebooted first.
        camera = picamera.PiCamera()
        camera.resolution = (320, 240)
        output = np.empty((240, 320, 3), dtype=np.uint8)

        # Load a sample picture and learn how to recognize it.
        nada_image = face_recognition.load_image_file("/home/pi/Desktop/GraduationProject/Images/nada.jpg")
        nada_face_encoding = face_recognition.face_encodings(nada_image)[0]

        doctor_image = face_recognition.load_image_file("/home/pi/Desktop/GraduationProject/Images/doctor.jpg")
        doctor_face_encoding = face_recognition.face_encodings(doctor_image)[0]

        mayada_image = face_recognition.load_image_file("/home/pi/Desktop/GraduationProject/Images/mayada.jpg")
        mayada_face_encoding = face_recognition.face_encodings(mayada_image)[0]

        lamia_image = face_recognition.load_image_file("/home/pi/Desktop/GraduationProject/Images/lamia.jpg")
        lamia_face_encoding = face_recognition.face_encodings(lamia_image)[0]

        rawda_image = face_recognition.load_image_file("/home/pi/Desktop/GraduationProject/Images/rawda.jpg")
        rawda_face_encoding = face_recognition.face_encodings(rawda_image)[0]

        feter_image = face_recognition.load_image_file("/home/pi/Desktop/GraduationProject/Images/feter.jpg")
        feter_face_encoding = face_recognition.face_encodings(feter_image)[0]

        samlak_image = face_recognition.load_image_file("/home/pi/Desktop/GraduationProject/Images/samlak.jpg")
        samlak_face_encoding = face_recognition.face_encodings(samlak_image)[0]

        ziad_image = face_recognition.load_image_file("/home/pi/Desktop/GraduationProject/Images/ziad.jpg")
        ziad_face_encoding = face_recognition.face_encodings(ziad_image)[0]

        saeed_image = face_recognition.load_image_file("/home/pi/Desktop/GraduationProject/Images/saeed.jpg")
        saeed_face_encoding = face_recognition.face_encodings(saeed_image)[0]

        # Create arrays of known face encodings and their names
        known_face_encodings = [
           
            nada_face_encoding,
            doctor_face_encoding,
            mayada_face_encoding,
            lamia_face_encoding,
            rawda_face_encoding,
            feter_face_encoding,
            samlak_face_encoding,
            ziad_face_encoding,
            saeed_face_encoding

        ]
        known_face_names = [
            
            "Nada",
            "doctor mahmoud",
            "mayada",
            "lamia",
            "rawda",
            "feter",
            "samlak",
            "ziad",
            "saeed"
        ]

        # Initialize some variables
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        mytext= 'unknown'

        while True:
            print("Capturing image.")
            # Grab a single frame of video from the RPi camera as a numpy array
            camera.capture(output, format="rgb")

            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(output)
            print("Found {} faces in image.".format(len(face_locations)))
            face_encodings = face_recognition.face_encodings(output, face_locations)

            # Loop over each face found in the frame to see if it's someone we know.
            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "unknown"

                if True in matches:
                        first_match_index = matches.index(True)
                        name = known_face_names[first_match_index]
                        

                face_names.append(name)
                mytext= name
                language = 'en'
                print("I see someone named {}!".format(name))


            #process_this_frame = not process_this_frame

                if mytext == "Nada":
                    pygame.mixer.music.load('/home/pi/Desktop/GraduationProject/Records/Names/nada.wav')
                    pygame.mixer.music.play()

                elif mytext == "doctor mahmoud":
                    pygame.mixer.music.load('/home/pi/Desktop/GraduationProject/Records/Names/doctor.wav')
                    pygame.mixer.music.play()
                        
                elif mytext == "mayada":
                    pygame.mixer.music.load('/home/pi/Desktop/GraduationProject/Records/Names/mayada.wav')
                    pygame.mixer.music.play()
                        
                elif mytext == "lamia":
                    pygame.mixer.music.load('/home/pi/Desktop/GraduationProject/Records/Names/lamia.wav')
                    pygame.mixer.music.play()
                        
                elif mytext == "rawda":
                    pygame.mixer.music.load('/home/pi/Desktop/GraduationProject/Records/Names/rawda.wav')
                    pygame.mixer.music.play()
                        
                elif mytext == "feter":
                    pygame.mixer.music.load('/home/pi/Desktop/GraduationProject/Records/Names/feter.wav')
                    pygame.mixer.music.play()

                elif mytext == "samlak":
                    pygame.mixer.music.load('/home/pi/Desktop/GraduationProject/Records/Names/samlak.wav')
                    pygame.mixer.music.play()
                elif mytext == "ziad":
                    pygame.mixer.music.load('/home/pi/Desktop/GraduationProject/Records/Names/ziad.mp3')
                    pygame.mixer.music.play()
                elif mytext == "saeed":
                    pygame.mixer.music.load('/home/pi/Desktop/GraduationProject/Records/Names/saeed.wav')
                    pygame.mixer.music.play()

                else:
                    pygame.mixer.music.load('/home/pi/Desktop/GraduationProject/Records/Names/unknown.wav')
                    pygame.mixer.music.play()   
                    
            
    elif GPIO.input(16) == GPIO.HIGH:
        import numpy as np
        import imutils
        
        pygame.mixer.music.load("/home/pi/Desktop/GraduationProject/Records/Buttons/color.mp3")
        pygame.mixer.music.play()
        print("played")
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
            image = imutils.resize(image, width=600)
            blurred = cv2.GaussianBlur(image, (11, 11), 0)  
            hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

##            cv2.imshow("Frame", image)
##            key = cv2.waitKey(1) & 0xFF

            # clear the stream in preparation for the next frame
            rawCapture.truncate(0)

            # if button `18` key was pressed, Take a pic
            if GPIO.input(18) == GPIO.HIGH:
                camera.capture('pic2.png')


                
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
                    
            if any ([ GPIO.input(10) == GPIO.HIGH,GPIO.input(12) == GPIO.HIGH,GPIO.input(16) == GPIO.HIGH,GPIO.input(18) == GPIO.HIGH,GPIO.input(24) == GPIO.HIGH]):
                print("closing camera")
                camera.close()
                cv2.destroyAllWindows()      
                break
                
            
    elif GPIO.input(12) == GPIO.HIGH:
        #To read all images format
        from PIL import Image
        #OCR Library
        import pytesseract
        
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
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # show the frame
            cv2.imshow("Frame", gray)
            
            # clear the stream in preparation for the next frame
            rawCapture.truncate(0)

            # if button `18` key was pressed, Take a picture
            if GPIO.input(18) == GPIO.HIGH:
                    camera.capture('pic1.png')

                    image = cv2.imread('pic1.png',0)
                    #cv2.imshow("Image", image)
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


            if any ([ GPIO.input(10) == GPIO.HIGH,GPIO.input(12) == GPIO.HIGH,GPIO.input(16) == GPIO.HIGH,GPIO.input(18) == GPIO.HIGH,GPIO.input(24) == GPIO.HIGH]):
                    print("closing camera")
                    camera.close()
                    cv2.destroyAllWindows()      
                    break
    
