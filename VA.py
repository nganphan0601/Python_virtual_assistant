import speech_recognition as sr
import pyttsx3

# listen: speech to text
robot_ear = sr.Recognizer()
with sr.Microphone() as mic:
    print("Robot: I'm listening")
    audio = robot_ear.listen(mic)

try:
    you = robot_ear.recognize_google(audio)
except:
    you = ""
    
print("You: " + you)


# understand
# pick the appropriate response

if you == "":
    robot_brain = "I can't hear you, try again"
elif you == "hello":
    robot_brain = "Hello Ngan"
elif you == "today":
    robot_brain = "Sunday"
else:
    robot_brain = "Sorry I don't understand"

print("Robot: " + robot_brain)
    

# speak: text to speech
engine = pyttsx3.init()
engine.say(robot_brain)
engine.runAndWait()