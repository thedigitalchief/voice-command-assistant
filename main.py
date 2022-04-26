from click import command
from re import search
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyautogui
import os
import subprocess
import sys
from bs4 import BeautifulSoup
import requests
from keyboard import press
from keyboard import press_and_release
import webbrowser
import ssl
#ssl._create_default_https_context = ssl._create_unverified_context

# initializing variables along with engine and listener
listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
rate = engine.getProperty("rate")
engine.setProperty("rate", 180)


# function that takes input text from the user
def talk(text):
    engine.say(text)
    engine.runAndWait()
    

# outputs voice prompt "Hello sir"
talk('Hello sir')

# takes user input via voice 
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            global command
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'computer' in command:
                command = command.replace('computer', '')
                print(command)
    except:
            pass   

    return command


def run_computer():
    command = take_command()

    if 'play' in command:
       song = command.replace('play', '')
       pywhatkit.playonyt(song)
       if 'pause' in command:
           press('pause')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('the time is ' + time)
        
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'volume up 6' in command:
        (pyautogui.press("volumeup"))*3 

    elif 'volume mute' in command:
        pyautogui.press("volumemute")                  

    elif 'volume up 8' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 10' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 12' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 14' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 16' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 18' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 20' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 30' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume up 40' in command:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")

    elif 'volume down 4' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 6' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 8' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 10' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 12' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 14' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 16' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 18' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif 'volume down 20' in command:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")


    elif 'shut down' in command or 'power off' in command:
        sys.exit()
    
    # weather command
    elif 'temperature' in command or 'weather' in command:
        search = "local temperature"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        talk(f"it is {temp}")
    
    # search google command
    elif 'search' in command:
        search = command.replace('search', '')
        pywhatkit.search(search)
    
    # screenshot command
    elif 'screenshot' in command:
        talk('What shall I name the image sir?')
        path = take_command()
        path1name = path + ".png"
        path1 = "[drivename]:\\[pathname]\\" + path1name
        ss = pyautogui.screenshot()
        ss.save(path1)
        os.startfile("[drivename]:\\[pathname]\\")
     
    # if computer does not recognize command
    else:
        print('please repeat that sir')

    while True:
        run_computer()
run_computer()    


# cd <project>/
# virtualenv venv

#virtualenv venv --system-site-packages
# source venv/bin/activate
# deacticate

# Python 3.10: universal2 for Mac M1 devies

