import speech_recognition as sr
import pyttsx3
from datetime import date, datetime
from openai import OpenAI

API_key = open("OpenAI_key.txt", "r").readline()
# initialize
robot_ear = sr.Recognizer()
robot_mouth = pyttsx3.init()
openAI = OpenAI(api_key=API_key)

while True:
    # listen: speech to text
    with sr.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)

    print("Robot: ...")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
        
    print("You: " + you)


    # understand
    # pick the appropriate response

    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello Ngan, how can I help you today?"
    elif "today" in you: 
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "bye" in you:
        robot_brain = "Goodbye, have a good day!"
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        response = openAI.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": you,
            }
        ],
        model="gpt-3.5-turbo",
    )
        robot_brain = response.choices[0].message.content

    print("Robot: " + robot_brain)
        

    # speak: text to speech
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()