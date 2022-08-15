import nltk
import numpy as np
import random
import json
import pickle
import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
import sys
import pypokedex
import requests
import time
import pyautogui
from bs4 import BeautifulSoup
import keyboard
from waiting import wait
import os

from jarvis import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")

def wiki(query):
    speak('Searching Wikipedia...')
    results = wikipedia.summary(query, sentences=1)
    speak("According to Wikipedia")
    print(results)
    speak(results)

def time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")

def rep():
    speak('what do you want me to repeat sir')
    jj = takeCommand()
    speak(f'{jj}')

def exit():
    query = 'bye'
    ints = predict_class(query)
    res = get_response(ints, intents)
    print(res)
    pyttsx3.speak(res)
    sys.exit()

def chat(query):
    ints = predict_class(query)
    res = get_response(ints, intents)
    print(res)
    pyttsx3.speak(res)

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        speak("Say that again please...")
        return "None"
    return query

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=68412fb931c1440eab8524ba2128d068",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=68412fb931c1440eab8524ba2128d068",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=68412fb931c1440eab8524ba2128d068",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=68412fb931c1440eab8524ba2128d068",
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=68412fb931c1440eab8524ba2128d068",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=68412fb931c1440eab8524ba2128d068"
    }

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key, value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        a = input("[press 1 to cont] and [press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break

    speak("thats all")

def temp():
    search = "temperature in kerala"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"current{search} is {temp}")

def weth():
    search = "weather in kerala"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"current{search} is {temp}")

dictapp = {"commandprompt": "cmd", "paint": "paint", "word": "winword", "excel": "excel", "chrome": "chrome",
           "vscode": "code", "powerpoint": "powerpnt"}

def openappweb(query):
    speak("Launching, sir")
    if ".com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("jarvis", "")
        query = query.replace("launch", "")
        query = query.replace(" ", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")


def closeappweb(query):
    speak("Closing,sir")
    if "one tab" in query or "1 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "2 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "3 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    elif "4 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")
    elif "5 tab" in query:
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        sleep(0.5)
        pyautogui.hotkey("ctrl", "w")
        speak("All tabs closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")

import tensorflow as tf
keras =tf.keras
k = keras.backend
km = keras.models
load_model = km.load_model
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('ai.h5')

def clean_up_setence(setence):
    setence_words = nltk.word_tokenize(setence)
    setence_words = [lemmatizer.lemmatize(word) for word in setence_words]
    return setence_words

def bag_of_words(setence):
    setence_words = clean_up_setence(setence)
    bag = [0] * len(words)
    for w in setence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
        return np.array(bag)

def predict_class(setence):
    bow = bag_of_words(setence)
    res = model.predict(np.array([bow]))[0]
    error_threshold = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > error_threshold]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tags'] == tag:
            result = random.choice(i['responses'])
            break
    return result

def sleep():
    speak('ok sir')
    keyboard.wait('shift')
    speak('hello again sir')

def pokedex():
    speak('what pokemon do you want to search on')
    p = pypokedex.get(name=input(''))

    speak(p.name + ' is ' + str(p.dex) + ' in the pokedex ' + 'it weighs ' + str(p.weight) + ' and measures at ' +
          str(p.height) + ' its a ' + str(p.types) + ' type ' + 'pokemon')


from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


