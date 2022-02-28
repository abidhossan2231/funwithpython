import pyttsx3
Friend = pyttsx3.init()
while True:
    msg = input("Assistant: ")
    Friend.say(msg)
    Friend.runAndWait()
