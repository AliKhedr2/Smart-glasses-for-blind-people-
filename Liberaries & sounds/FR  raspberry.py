import face_recognition
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import pygame
pygame.init()
import os



# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

### Load a sample picture and learn how to recognize it.

nada_image = face_recognition.load_image_file("nada.jpg")
nada_face_encoding = face_recognition.face_encodings(nada_image)[0]

doctor_image = face_recognition.load_image_file("doctor.jpg")
doctor_face_encoding = face_recognition.face_encodings(doctor_image)[0]

mayada_image = face_recognition.load_image_file("mayada.jpg")
mayada_face_encoding = face_recognition.face_encodings(mayada_image)[0]

lamia_image = face_recognition.load_image_file("lamia.jpg")
lamia_face_encoding = face_recognition.face_encodings(lamia_image)[0]

rawda_image = face_recognition.load_image_file("rawda.jpg")
rawda_face_encoding = face_recognition.face_encodings(rawda_image)[0]

feter_image = face_recognition.load_image_file("feter.jpg")
feter_face_encoding = face_recognition.face_encodings(feter_image)[0]

samlak_image = face_recognition.load_image_file("samlak.jpg")
samlak_face_encoding = face_recognition.face_encodings(samlak_image)[0]

ziad_image = face_recognition.load_image_file("ziad.jpg")
ziad_face_encoding = face_recognition.face_encodings(ziad_image)[0]

saeed_image = face_recognition.load_image_file("saeed.jpg")
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

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx= 0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)
            mytext = name
            language = 'en'


    process_this_frame = not process_this_frame


##    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)


        
    # Display the resulting image
        
        cv2.imshow('Video', frame)

        if mytext == "Nada":
            pygame.mixer.sound('nada.wav')
            
        elif mytext == "doctor mahmoud":
            pygame.mixer.sound('doctor.wav')
            
        elif mytext == "mayada":
            pygame.mixer.sound('mayada.wav')
            
        elif mytext == "lamia":
            pygame.mixer.sound('lamia.wav')
            
        elif mytext == "rawda":
            pygame.mixer.sound('rawda.wav')
            
        elif mytext == "feter":
            pygame.mixer.sound('feter.wav')

        elif mytext == "samlak":
            pygame.mixer.sound('samlak.wav')
        elif mytext == "ziad":
            pygame.mixer.sound('ziad.wav')
        elif mytext == "saeed":
            pygame.mixer.sound('saeed.wav')

        else:
            pygame.mixer.sound('unknown.wav')
    
        # Hit 'q' on the keyboard to quit!
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
