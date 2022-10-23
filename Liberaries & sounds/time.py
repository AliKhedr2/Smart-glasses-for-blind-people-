# Import the required module for text  
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can  
# play the converted audio 
import os 
# The text that you want to convert to audio 
import time;
from datetime import datetime
import pygame



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
