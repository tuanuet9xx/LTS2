import pyttsx3
robot_brain= "Hello Mina"
robot_mouth = pyttsx3.init('dummy')
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()