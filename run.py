import random
import numpy as np
import pickle
import json
import pyttsx3

import nltk
from nltk.stem import WordNetLemmatizer

import tensorflow as tf
keras = tf.keras
k = keras.backend
km = keras.models
load_model = km.load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('ai.h5')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

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

print('go bot is running')

while True:
    message = input("")
    ints = predict_class(message)
    res = get_response(ints, intents)
    print(res)
    pyttsx3.speak(res)



