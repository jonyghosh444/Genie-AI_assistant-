# Hare Krishna
import sys
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import json


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 < hour < 12:
        speak("Good morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hello Boss. I am Genie. Please tell me how may I help you.")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    with open('docs.json', 'r') as c:
        params = json.load(c)["params"]
    print(params["email"])
    server.login(params["email"], params["pass"])
    server.sendmail(params["email"], to, content)
    server.close()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening............")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language="en-US")
        print(f"User said {query}")

    except Exception as e:
        print(e)
        print("Speak again please...")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play hori naam' in query:
            songno = random.randint(0, 1)
            music_dir = 'G:\\krishna nam'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[songno]))
            print(songno)

        elif 'play music' in query:
            songno = random.randint(0, 14)
            music_dir = 'G:\\Audio song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[songno]))
            print(songno)
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Boss, the time is {strTime}")

        elif 'open pycharm' in query:
            path = "C:\\Users\\User\\PyCharm Community Edition 2021.3.2\\bin\\pycharm64.exe"
            os.startfile(path)

        elif 'open code' in query:
            path = "D:\\Installed file\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "target@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry boss. I am not able to send this email at the moment.")

        elif 'destroy' in query:
            sys.exit()

        elif 'exit' in query:
            sys.exit()

        elif 'leave me alone' in query:
            sys.exit()

        elif 'leave now' in query:
            sys.exit()



