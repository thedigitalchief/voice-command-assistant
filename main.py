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
ssl._create_default_https_context = ssl._create_unverified_context


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



run_computer()    


# cd <project>/
# virtualenv venv

#virtualenv venv --system-site-packages
# source venv/bin/activate
# deacticate

# Python 3.10: universal2 for Mac M1 devies
