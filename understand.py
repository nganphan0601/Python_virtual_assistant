you = "hello"

if you == "":
    robot_brain = "I can't hear you, try again"
elif you == "hello":
    robot_brain = "Hello Ngan"
elif you == "today":
    robot_brain = "Sunday"
else:
    robot_brain = "Sorry I don't understand"

print("Robot: " + robot_brain)
    