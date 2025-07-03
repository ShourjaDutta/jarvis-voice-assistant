#import speech_recognition as sr
#import os
from time import strftime

#def say(text):
#    os.system(f"say {text}")

#def takeCommand():
#    r=sr.Recognizer()
#    with sr.Microphone as source:
#        r.pause_threshold = 1
#        audio = r.listen(source)
#        query = r.recognize_google(audio, language = "en-in")
#        print(f"User said : {query}")
#        return query

#if __name__=="__main__":
#    print("PyCharm")
#    say("Hello I am Jarvis A.I")
#    print("Listening... ")
#    text = takeCommand()
#    say(text)

#import win32com.client

#speaker = win32com.client.Dispatch("SAPI.SpVoice")

#while 1:
#    print("Enter the word you want to speak it out by computer")
#    s=input()
#    speaker.Speak(s)

import speech_recognition as sr
import pyttsx3
import webbrowser
import openai
import os
import datetime


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
    except Exception as e:
        print("Sorry, I did not understand that. Please say that again.")
        return None
    return query

if __name__ == "__main__":
    say("Hello, I am Jarvis AI")
    while True:
        text = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in text.lower():
                say(f"Opening {site[0]} Sir...")
                webbrowser.open(site[1])
        if "open music" in text:
            musicPath = "C:/Users/KIIT/Downloads/Jab Tak - M.S. Dhoni - The Untold Story 320 Kbps.mp3"
            os.startfile(musicPath)
        if "the time" in text:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")
        if "open notepad".lower() in text.lower():
            appPath = "C:/Windows/System32/notepad.exe"
            os.startfile(appPath)
        if "exit" in text:
            break
        #if text:
        #    say(text)

