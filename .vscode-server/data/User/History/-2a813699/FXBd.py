

you = "today"

if you == "" :
    robot_brain =" I can not hear you , please try again"

elif you == "Hello":
    robot_brain = " Hello Steven Tuan"

elif you ==" today":
    robot_brain =" Friday"

else          :

    robot_brain =" Ok see you then"

print (robot_brain)    

 

robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()