import pyttsx3
import speech_recognition

robot_ear= speech_recognition.Recognizer()

robot_mouth = pyttsx3.init()
robot_brain="" 

with speech_recognition.Microphone() as mic:
    print ("I'm listing ")

    audio = robot_ear.listen(mic)

print ("robot ...")    
try:
    you =robot_ear.recognize_google(audio)
except:
    you = ""
print (you)

if you == "" :
    robot_brain =" I can not hear you , please try again"

elif you == "Hello":
    robot_brain = " Hello Steven Tuan"

elif you ==" today":
    robot_brain =" Friday"

else          :

    robot_brain =" Ok see you then"

print (robot_brain)   

robot_mouth.say(robot_brain)
robot_mouth.runAndWait()