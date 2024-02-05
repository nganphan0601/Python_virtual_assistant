import speech_recognition as sr

robot_ear = sr.Recognizer()
with sr.Microphone() as mic:
    print("Robot: I'm listening")
    audio = robot_ear.listen(mic)

try:
    you = robot_ear.recognize_google(audio)
except:
    you = ""
    
print("You: " + you)