import pyttsx3
import speech_recognition
from datetime import date

robot_ear= speech_recognition.Recognizer()

robot_mouth = pyttsx3.init()
robot_brain="" 

while True:
    with speech_recognition.Microphone() as mic:
        print ("I'm listing ")
        audio = robot_ear.listen(mic)

    print ("robot ..." )    
    try:
        you =robot_ear.recognize_google(audio)
    except:
        you = ""
    print (you)

    if you == "" :
        robot_brain =" I can not hear you , please try again"

    elif "Hello" in you:
        robot_brain = " Hello Steven Tuan"

    elif " today" in you:
        robot_brain =" Friday"
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")

    elif "bye" in you:
        robot_brain= "Bye Steven"
        print ("robot_brain:"  + robot_brain)     

        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break    

    else:

        robot_brain =" Ok see you then"

    print ("robot_brain:"  + robot_brain)     

    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()