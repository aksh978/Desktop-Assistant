#!/usr/bin/env python3
import datetime
import getpass
import os
import random
import smtplib
import sys
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia
import gui
import jarvis as jv
print("Initializing Jarvis....")

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

popular_websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.org",
    "amazon": "https://www.amazon.com",
}
search_engines = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "bing": "https://www.bing.com",
}


def open_url(url):
    webbrowser.open(url)
    chrome_path = r"open -a /Applications/Google\ Chrome.app %s"
    webbrowser.get(chrome_path).open(url)


def search(search_query, search_engine):
    try:
        open_url(f"{search_engines[search_engine]}/search?q={search_query}")
    except IndexError:
        open_url(f"https://www.google.com/search?q={search_query}")


def speak(text):
    gui.speak(text)
    engine.say(text)
    engine.runAndWait()


def print_and_speak(text):
    print(text)
    speak(text)


def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning" + master)
    elif hour < 18:
        speak("Good Afternoon" + master)
    else:
        speak("Good Evening" + master)

    # speak("Hey I am Jarvis. How may I help you")


# This is where our programme begins....


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        """The default value as per speech_recognition documentation.
        Increase if application stops responding. and decrease if
        assistant doesn't execute any command and just says next
        command sir."""

        audio = r.listen(source)

    print("Recognizing....")
    query = ""
    try:
        query = r.recognize_google(audio, language="en-in")
        print("User said: " + query)

    except sr.UnknownValueError:
        print("Sorry could you please try again?")

    except Exception as e:
        print(e)
        print("Say that again, please?")

    return query


def execute_the_command_said_by_user():
    query = take_command().lower()

    # logic for executing basic tasks
    if ('wikipedia' in query or 'what is' in query or 'who is' in query or 'when' in query or 'where is' in query):
        speak("searching...")
        query = query.replace("wikipedia", "")
        query = query.replace("search", "")
        query = query.replace("what", "")
        query = query.replace("when", "")
        query = query.replace("where", "")
        query = query.replace("who", "")
        query = query.replace("is", "")
        result = wikipedia.page(query, auto_suggest=False)
        result = wikipedia.summary(query, sentences=2)
        print(result)
        print_and_speak(result)

    elif "what's up" in query or "how are you" in query:
        st_msgs = (
            "Just doing my thing!",
            "I am fine!",
            "Nice!",
            "I am nice and full of energy",
        )
        speak(random.choice(st_msgs))

    elif "date" in query:
        print_and_speak(f"{datetime.datetime.now():%A, %B %d, %Y}")

    elif "time" in query:
        print_and_speak(f"{datetime.datetime.now():%I %M %p}")

    elif "open" in query.lower():
        website = query.replace("open", "").strip().lower()
        try:
            open_url(popular_websites[website])
        except IndexError:  # If the website is unknown
            print(f"Unknown website: {website}")
            speak(f"Sorry, I don't know the website {website}")

    elif "search" in query.lower():
        search_query = query.split("for")[-1]
        search_engine = query.split("for")[0].replace(
            "search", "").strip().lower()
        search(search_query, search_engine)

    elif "email" in query:
        speak("Who is the recipient? ")
        recipient = take_command()

        if "me" in recipient:
            try:
                speak("What should I say? ")
                content = take_command()

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.ehlo()
                server.starttls()
                server.login("malviyaaksh@gmail.com", "TEst123")
                server.sendmail("malviyaaksh@gmail.com", "aksh", content)
                server.close()
                speak("Email sent!")
            except Exception:
                speak("Sorry Sir! I am unable to send your message at this moment!")

    elif "nothing" in query or "abort" in query or "stop" in query:
        speak("okay")
        speak("Bye Sir, have a good day.")
        sys.exit()

    elif "hello" in query:
        speak("Hello Sir")

    elif "bye" in query:
        speak("Bye Sir, have a good day.")
        sys.exit()

    elif "play music" in query:
        music_folder = "Your_music_folder_path(absolute_path)"
        music = ("music1", "music2", "music3", "music4", "music5")
        random_music = music_folder + random.choice(music) + ".mp3"
        os.system(random_music)

        speak("Playing your request")

    elif ("tell me about yourself" in query):
        jv.personal()
    elif ("about you" in query):
        jv.personal()
    elif ("who are you" in query):
        jv.personal()
    elif ("yourself" in query):
        jv.personal()

    elif ("developer" in query or "tell me about your developer" in query or "father" in query or "who developed you" in query or "developer" in query):
        speak(
            "here is the details: I am developed by Group of Students of Vaishnav college")
    elif ("restart" in query):
        os.system("shutdown /r /t 1")
    elif ("shut down" in query):
        os.system("shutdown /r /t 1")

    elif ("create a reminder list" in query or "reminder" in query):
        speak("What is the reminder?")
        data = takeCommand()
        speak("You said to remember that" + data)
        reminder_file = open("data.txt", 'a')
        reminder_file.write('\n')
        reminder_file.write(data)
        reminder_file.close()

    elif ('i am done' in query or 'bye bye jarvis' in query
          or 'go offline jarvis' in query or 'bye' in query
          or 'nothing' in query):
        jv.wishme_end()

    elif ("tell me your powers" in query or "help" in query
          or "features" in query):
        features = ''' i can help to do lot many things like..
            i can tell you the current time and date,
            i can tell you the current weather,
            i can tell you battery and cpu usage,
            i can create the reminder list,
            i can take screenshots,
            i can send email to your boss or family or your friend,
            i can shut down or logout or hibernate your system,
            i can tell you non funny jokes,
            i can open any website,
            i can search the thing on wikipedia,
            i can change my voice from male to female and vice-versa
            And yes one more thing, My boss is working on this system to add more features...,
            tell me what can i do for you??
            '''
        print(features)
        speak(features)

    # screenshot
    elif ("screenshot" in query):
        jv.screenshot()
        speak("Done!")

# cpu and battery usage
    elif ("cpu and battery" in query or "battery" in query
            or "cpu" in query):
        jv.cpu()

# jokes
    elif ("tell me a joke" in query or "joke" in query):
        jv.jokes()

# weather
    elif ("weather" in query or "temperature" in query):
        jv.weather()

    else:
        speak("sorry didn't understand")


speak("Initializing Jarvis....")
jv.wishme()
gui.set_speak_command(execute_the_command_said_by_user)
gui.mainloop()
