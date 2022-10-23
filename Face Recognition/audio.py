from gtts import gTTS
import os
from playsound import playsound


mytext = 'abdulrahman samlak'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("samlak.mp3") 
#os.system("mpg321 welcome.mp3") 
#playsound('welcome.mp3')

