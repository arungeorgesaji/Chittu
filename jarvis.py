import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import sys

import random
import numpy as np
import pickle
import json

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


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


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

repeat = "True"

if __name__ == "__main__":
    wishMe()
    while repeat == "True":
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'are you a robot' in query:
            speak('Yes  I am a robot  ,   but    I’m a good one    .        Let me prove it.         How can I help you?')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
                webbrowser.open("google.com")

        elif 'open gmail' in query:
            webbrowser.open("mail.google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'repeat my words' in query:
            speak('what do you want me to repeat sir')
            jj = takeCommand()
            speak(f'{jj}')

        elif 'buy jarvis' in query:
            speak('Bai sir, Have a great day')
            sys.exit()

        elif 'play game' in query:

                import pygame
                import os

                WIDTH, HEIGHT = 900, 500
                WIN = pygame.display.set_mode((WIDTH, HEIGHT))
                pygame.display.set_caption("spaceship war")

                WHITE = (255, 255, 255)
                BLACK = (0, 0, 0)
                RED = (255, 0, 0)
                YELLOW = (255, 255, 0)

                FPS = 60

                BULLET_VEL = 7

                MAX_BULLETS = 3

                w, h = 55, 40

                YELLOW_HIT = pygame.USEREVENT + 1
                RED_HIT = pygame.USEREVENT + 2

                BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

                VEL = 5

                yellow_spaceship = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
                yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship, (w, h)), 90)
                red_spaceship = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
                red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship, (w, h)), 270)

                def draw_window(red, yellow, red_bullets, yellow_bullets):
                    WIN.fill(WHITE)
                    pygame.draw.rect(WIN, BLACK, BORDER)
                    WIN.blit(yellow_spaceship, (yellow.x, yellow.y))
                    WIN.blit(red_spaceship, (red.x, red.y))

                    for bullet in red_bullets:
                        pygame.draw.rect(WIN, RED, bullet)

                    for bullet in yellow_bullets:
                        pygame.draw.rect(WIN, YELLOW, bullet)

                    pygame.display.update()

                def yellow_movement(keys_pressed, yellow):
                    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
                        yellow.x -= VEL
                    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
                        yellow.x += VEL
                    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
                        yellow.y -= VEL
                    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:
                        yellow.y += VEL

                def red_movement(keys_pressed, red):
                    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x +BORDER.width:
                        red.x -= VEL
                    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:
                        red.x += VEL
                    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
                        red.y -= VEL
                    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:
                        red.y += VEL

                def handle_bullets(yellow_bullets, red_bullets, yellow, red):
                    for bullet in yellow_bullets:
                        bullet.x += BULLET_VEL
                        if red.collidedict(bullet):
                            pygame.event.post(pygame.event.Event(RED_HIT))
                            yellow_bullets.remove(bullet)

                    for bullet in red_bullets:
                        bullet.x += BULLET_VEL
                        if yellow.collidedict(bullet):
                            pygame.event.post(pygame.event.Event(YELLOW_HIT))
                            red_bullets.remove(bullet)
                def game():
                    red = pygame.Rect(700, 300, w, h)
                    yellow = pygame.Rect(100, 300, w, h)

                    red_bullets = []
                    yellow_bullets = []

                    clock = pygame.time.Clock()
                    run = True
                    while run:
                        clock.tick(FPS)
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                run = False

                            if event.type == pygame.KEYDOWN:

                                if event.key ==pygame.K_LCTRL and len(yellow_bullets) > MAX_BULLETS:
                                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                                    yellow_bullets.append(bullet)

                                if event.key ==pygame.K_RCTRL and len(red_bullets) > MAX_BULLETS:
                                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                                    red_bullets.append(bullet)

                        keys_pressed = pygame.key.get_pressed()
                        yellow_movement(keys_pressed, yellow)
                        red_movement(keys_pressed, red)

                        handle_bullets(yellow_bullets, red_bullets, yellow, red)

                        draw_window(red, yellow, red_bullets, yellow_bullets)
                    pygame.quit()

                if __name__ == "__main__":
                    game()

        else:
            ints = predict_class(query)
            res = get_response(ints, intents)
            print(res)
            pyttsx3.speak(res)
