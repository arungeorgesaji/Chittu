import datetime
import pyttsx3
import random
import numpy as np
import pickle
import json
import speech_recognition as sr
import wikipedia
import sys
import webbrowser

import nltk
from nltk.stem import WordNetLemmatizer


import tensorflow as tf
lemmatizer = WordNetLemmatizer
keras = tf.keras
k = keras.backend
km = keras.models
load_model = km.load_model

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

def prepare():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    intents = json.loads(open('intents.json').read())
    words = pickle.load(open('words.pkl', 'rb'))
    classes = pickle.load(open('classes.pkl', 'rb'))
    model = load_model('ai.h5')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


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
        return "None"
    return query

    while query == None:
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
            return "None"
    return query

def chat():
    ints = predict_class(query)
    res = get_response(ints, intents)
    print(res)
    pyttsx3.speak(res)

def wiki():
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
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
    speak(chat())
    sys.exit()

def google():
    webbrowser.open("google.com")

def youtube():
    webbrowser.open("youtube.com")

def gmail():
    webbrowser.open("mail.google.com")




