import pyttsx3
import datetime
import speech_recognition as SR
import wikipedia
import webbrowser
import os

engine_friday = pyttsx3.init('sapi5')
voices = engine_friday.getProperty('voices')
engine_friday.setProperty('voice',voices[1].id)

def speak(audio):
    engine_friday.say(audio)
    engine_friday.runAndWait()
def wishOwner():
    Hour = datetime.datetime.now().hour
    if Hour <= 0 and Hour >12:
        speak("Good Morning Sir !")
    elif Hour >=12 and Hour <18:
        speak("Good After Noon Sir !")
    else:
        speak("good Evening Sir !")
    speak("I am Friday Sir , Please tell me my assignment !")
def takeCommandFromOwner():
    R1 = SR.Recognizer()
    with SR.Microphone() as source:
        print("Listening...")
        R1.pause_threshold = 1.2
        audio = R1.listen(source)
    try:
        print("Recognising...")
        query = R1.recognize_google(audio, language="en-in")
        print(f"User said : {query}")
    except Exception as me:
        print("Please say that Again ")
        return None
    return query


if __name__ == '__main__':
    wishOwner()
    while True:

        query = takeCommandFromOwner().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences = 4)
            speak("According to wikipedia ")
            speak(results)

        if "bye" in query:
            exit()
        if "youtube" in query:
            npath = "https://www.youtube.com/"
            webbrowser.open(npath)
        if "google" in query:
            path = "https://www.google.com/"
            webbrowser.open(path)
        if "Chrome" in query:
            path = "C:\\Program Files\\Google\\Chrome\\Application"

            os.startfile(path)
