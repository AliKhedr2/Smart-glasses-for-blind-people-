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
import cv2

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
            

            # Press 'q' to quit
        if cv2.waitKey(1) == ord('q'):
            break
            


    #rawCapture.truncate(0)

camera.close()

cv2.destroyAllWindows()
