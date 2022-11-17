import logging
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
import requests
import time
import pyautogui
from bs4 import BeautifulSoup
import os
import pypokedex
import keyboard
import wmi
import pywhatkit
import speedtest
import PyPDF2
from pytube import YouTube
from tkinter import *
import screen_brightness_control as bc

print("please wait until we get the system ready")

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

    speak("i am chittu sir how may i help you ")

def wiki(query):
    speak('Searching Wikipedia...')
    query = query.replace('wikipedia', '')
    query = query.replace('feature', '')
    results = wikipedia.summary(query, sentences=1)
    speak("According to Wikipedia")
    print(results)
    speak(results)

def time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")

def rep():

    speak('what do you want me to repeat sir')
    jj = takecommand()
    speak(f'{jj}')

def exit():

    query = 'bye'
    ints = predict_class(query)
    res = get_response(ints, intents)
    print(res)
    pyttsx3.speak(res)
    sys.exit()

def takecommand():

    query = ''

    while query == '':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = r.listen(source)
            print("Recognizing...")

            #query = r.recognize_houndify(audio, 'tta9-FhirHytE2PGtmbk9Q==','mm_LZwma-32RBJ8FDFIvlx2NlOi2FSkbXEIujEfyc1hWZE1Ki1mGwnBKphEVs0B74FDnD3MAJeMx7qaiiWGLkQ==')
            query = r.recognize_houndify(audio, 'QGNyQu2u80ZIo5jc1k20ig==','PS56AFbKi6M9OyUp3srnviGoS6so5XpowQm_L-3DwxHmKlFrf7IZ2SBpYqsi_RZs9Q4Fa2LH-wzk7_7efDyJXw==')

            if query == '':
                print('say that again please')
                speak('say that again please')

            else:
                print(f"User said: {query}\n")
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
    error_catcher = 0
    speak("Launching, sir")

    if "dot com" in query or "dot org" in query or ".com" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("feature", "")

        if "dot com" in query:
            error_catcher += 1
        if "dot org" in query:
            error_catcher += 1
        if ".com" in query:
            error_catcher += 1
        if ".org" in query:
            error_catcher += 1


        if error_catcher == 1:

            if "dot com" in query or ".com" in query:
                query = query.replace("com", "")
                query = query.replace("dot", "")
                query = query.replace(".", "")
                query = query.replace(" ", "")
                webbrowser.open(f"https://www.{query}.com")

            elif "dot org" in query or ".org" in query:
                query = query.replace("org", "")
                query = query.replace("dot", "")
                query = query.replace(".", "")
                query = query.replace(" ", "")
                webbrowser.open(f"https://www.{query}.org")



    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")


def closeappweb(query):

    speak("Closing,sir")

    if 'tab' in query:
        pyautogui.hotkey("ctrl", "w")
        speak("tab has been closed")

    else:
        keys = list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")

def searchyoutube(query):

        speak("This is what I found for your search!")
        query = query.replace("youtube", "")
        query = query.replace("feature", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        speak("Done, Sir")

def searchgoogle(query):

        import wikipedia as googleScrap
        query = query.replace("feature", "")
        query = query.replace("google", "")
        speak("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No speakable output available")

def tired():

    speak("Playing your favourite songs, sir")
    a = (1, 2, 3)
    b = random.choice(a)
    if b == 1:
        webbrowser.open("https://www.youtube.com/watch?v=Mvaosumc4hU&ab_channel=BoyWithUke")
    if b == 2:
        webbrowser.open("https://www.youtube.com/watch?v=omVvuL0lOes&ab_channel=RachelGardner")
    if b == 3:
        webbrowser.open("https://www.youtube.com/watch?v=QFJQHpk7hnU&ab_channel=ShadowMusic")

def internet_speed():

    wifi = speedtest.Speedtest()
    upload_net = wifi.upload() / 1048576  # Megabyte = 1024*1024 Bytes
    download_net = wifi.download() / 1048576
    print("Wifi Upload Speed is", upload_net)
    print("Wifi download speed is ", download_net)
    speak(f"Wifi download speed is {download_net}")
    speak(f"Wifi Upload speed is {upload_net}")


def rock_paper_scissors():

    speak("Lets Play ROCK PAPER SCISSORS !!")
    print("LETS PLAYYYYYYYYYYYYYY")
    i = 0
    me_score = 0
    com_score = 0
    while (i < 5):
        choose = ("rock", "paper", "scissors")  # Tuple
        com_choose = random.choice(choose)
        query = takecommand().lower()
        if (query == "rock"):
            if (com_choose == "rock"):
                speak("ROCK")
                print(f"Score:- ME :- {me_score} : COM :- {com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                com_score += 1
                print(f"Score:- ME :- {me_score} : COM :- {com_score}")
            else:
                speak("Scissors")
                me_score += 1
                print(f"Score:- ME :- {me_score} : COM :- {com_score}")

        elif (query == "paper"):
            if (com_choose == "rock"):
                speak("ROCK")
                me_score += 1
                print(f"Score:- ME :- {me_score + 1} : COM :- {com_score}")

            elif (com_choose == "paper"):
                speak("paper")
                print(f"Score:- ME :- {me_score} : COM :- {com_score}")
            else:
                speak("Scissors")
                com_score += 1
                print(f"Score:- ME :- {me_score} : COM :- {com_score}")

        elif (query == "scissors" or query == "scissor"):
            if (com_choose == "rock"):
                speak("ROCK")
                com_score += 1
                print(f"Score:- ME :- {me_score} : COM :- {com_score}")
            elif (com_choose == "paper"):
                speak("paper")
                me_score += 1
                print(f"Score:- ME :- {me_score} : COM :- {com_score}")
            else:
                speak("Scissors")
                print(f"Score:- ME :- {me_score} : COM :- {com_score}")
        i += 1

    print(f"FINAL SCORE :- ME :- {me_score} : COM :- {com_score}")


logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import tensorflow as tf
keras =tf.keras
k = keras.backend
km = keras.models
load_model = km.load_model
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('ai.h5')

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

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

def chat(query):

    ints = predict_class(query)
    res = get_response(ints, intents)
    print(res)
    pyttsx3.speak(res)

def sleep():

    speak('ok sir')
    keyboard.wait('shift')
    speak('hello again sir')

def cpu_temp():

    w = wmi.WMI(namespace=r'root\wmi')
    temperature = w.MSAcpi_ThermalZoneTemperature()[0]
    temperature = int(temperature.CurrentTemperature / 10.0 - 273.15)
    print('your cpu is at '+str(temperature)+' degree celcius')
    speak('your cpu is at '+str(temperature)+' degree celcius')

def pokedex():

    speak('what pokemon do you want to search on')
    try:

        p = pypokedex.get(name=input(''))

        speak(p.name + ' is ' + str(p.dex) + ' in the pokedex ' + 'it weighs ' + str(p.weight) + ' and measures at ' +
          str(p.height) + ' its a ' + str(p.types) + ' type ' + 'pokemon')

    except Exception as e:

        print('that not a pokemon')
        speak('thats not a pokemon')
        print('going back to the main program')
        speak('going back to the main program')

def password():

    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
             "u", "v", "w", "x", "y", "z"]
    num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbol = ["#", "*", "@", "&"]
    password1 = random.choice(lower)
    password2 = random.choice(lower)
    password3 = random.choice(num)
    password4 = random.choice(lower)
    password5 = random.choice(lower)
    password6 = random.choice(num)
    password7 = random.choice(num)
    password8 = random.choice(lower)
    password9 = random.choice(symbol)
    password10 = random.choice(lower)
    password11 = random.choice(symbol)
    password12 = random.choice(num)
    password13 = random.choice(symbol)
    password14 = random.choice(symbol)
    password15 = random.choice(lower)
    password16 = random.choice(lower)
    password17 = random.choice(num)
    password18 = random.choice(num)
    password19 = random.choice(lower)
    password20 = random.choice(lower)
    upper1 = str(password2.upper())
    upper2 = str(password4.upper())
    upper3 = str(password5.upper())
    upper4 = str(password19.upper())
    upper5: str = str(password20.upper())
    speak('youre generated password is')
    print(password1 + upper1 + password3 + upper2 + upper3 + password6 + password7 +
          password8 + password9 + password10 + password11 + password12 + password13 + password14 + password15 +
          password16 + password17 + password18 + upper4 + upper5)

def num_guess_game():

    global random_number
    global num
    print("which difficulty you want")
    speak("which difficulty you want")
    print("type help if you need to know more")
    speak("type help if you need to know more")
    dif = input('difficulty:')
    dif.islower()
    lb = False
    chance = 0
    lb2 = False

    while not lb:

        if dif == 'help':
            print("there are four dificulties easy,medium,hard,insane easy is random number from 1 to 10 medium is from 1 to 100 hard is from 1 to 1,000 and insane from 1 to 10,000")
            speak("there are four dificulties easy,medium,hard,insane easy is random number from 1 to 10 medium is from 1 to 100 hard is from 1 to 1,000 and insane from 1 to 10,000")
            dif = input('difficulty:')
            dif.islower()

        if dif == 'easy':
            random_number = int(random.randint(1, 10))
            print("you chose easy difficulty")
            speak("you chose easy difficulty")
            lb = True

        elif dif == 'medium':
            random_number = int(random.randint(1, 100))
            print("you chose medium difficulty")
            speak("you chose medium difficulty")
            lb = True

        elif dif == 'hard':
            random_number = int(random.randint(1, 1000))
            print("you chose hard difficulty")
            speak("you chose hard difficulty")
            lb = True

        elif dif == 'insane':
            random_number = int(random.randint(1, 10000))
            print("you chose insane difficulty")
            speak("you chose insane difficulty")
            lb = True

        else:
            print("thats not a difficulty type help to know about the difficulties")
            speak("thats not a difficulty type help to know about the difficulties")
            dif = input('difficulty:')
            dif.islower()

        if dif =='easy':
                print('type  number between 1 to 10 or type stop to stop guessing')
                speak('type  number between 1 to 10 or type stop to stop guessing')
                num = input('number:')


        if dif == 'medium':
                print('type  number between 1 to 100 or type stop to stop guessing')
                speak('type  number between 1 to 100 or type stop to stop guessing')
                num = input('number:')


        if dif == 'hard':
                print('type  number between 1 to 1000 or type stop to stop guessing')
                speak('type  number between 1 to 1000 or type stop to stop guessing')
                num = input('number:')


        if dif == 'insane':
                print('type  number between 1 to 10000 or type stop to stop guessing')
                speak('type  number between 1 to 10000 or type to stop guessing')
                num = input('number:')

        while not lb2:

            if num == random_number:
                chance += 1
                print('thats correct')
                speak('thats correct')
                print('you took' + str(chance) + 'try to figure the number')
                speak('you took' + str(chance) + 'try to figure the number')
                lb2 = True

            elif num == 'stop':
                print('the correct answer was ' + str(random_number))
                speak('the correct answer was ' + str(random_number))
                lb2 = True

            else:
                print(num)
                print('thats wrong try again')
                speak('thats wrong try again')
                chance += 1

                if dif == 'easy':
                    print('type  number between 1 to 10 or type stop to stop guessing')
                    speak('type  number between 1 to 10 or type stop to stop guessing')
                    num = input('number:')

                if dif == 'medium':
                    print('type  number between 1 to 100 or type stop to stop guessing')
                    speak('type  number between 1 to 100 or type stop to stop guessing')
                    num = input('number:')

                if dif == 'hard':
                    print('type  number between 1 to 1000 or type stop to stop guessing')
                    speak('type  number between 1 to 1000 or type stop to stop guessing')
                    num = input('number:')

                if dif == 'insane':
                    print('type  number between 1 to 10000 or type stop to stop guessing')
                    speak('type  number between 1 to 10000 or type to stop guessing')
                    num = input('number:')

def what_mess():

    lb = False
    phone = input('type phone number put +country code and write number without spaces:')
    hour = input('type the hour in which you want to send the message in universal time:')
    minute = input('type the minute in which you want to send the message:')
    print('tip you can type stop to stop this function')
    print('the time you give should be more than 30 seconds away')

    mess = input('message:')

    if mess == 'stop':

        print('okay going back to main program')
        speak('okay going back to main program')

    else:

        try:

            pywhatkit.sendwhatmsg(phone, mess, int(hour), int(minute))

        except Exception as e:

            print('there seems to be a problem with given info')
            speak('there seems to be a problem with given info')
            print('returning to main program')
            speak('returning to main program')

def audiobook():

    excep = False

    print('right click your pdf and click copy as path,ctrl+v here and remove double quotes to read pdf')
    speak('right click your pdf and click copy as path ctrl+v here and remove double quotes to read pdf')

    pdf = input('pdf:')

    try:
        book = open(pdf, 'rb')

    except Exception as e:

        excep = True

        print('sorry that doesnt match with any pdf,returning to main program')
        speak('sorry that doesnt math with any pdf,returning to main program')

    if excep == False:

        reader = PyPDF2.PdfFileReader(book)
        page = reader.pages[0]
        text = page.extract_text()

        speak(text)

def spam():

    print('keep the app which you want to spam in the side and open when i tell')
    speak('keep the app which you want to spam in the side and open when i tell')

    limit = input("number of times to spam:-")
    message = input("message:-")

    i = 0

    print('open the app now open from the app correct person to spam also')
    speak('open the app now open from the app correct person to spam also')

    print('press spacebar when your ready')
    speak('press spacebar when your ready')

    keyboard.wait('spacebar')

    try:

        while i < int(limit):

            pyautogui.typewrite(message)
            pyautogui.press("enter")
            i += 1

    except Exception as e:

            print('there seems to be a problem with given info')
            speak('there seems to be a problem with given info')
            print('returning to main program')
            speak('returning to main program')

def download():

    root = Tk()
    root.resizable(0, 0)
    root.attributes('-fullscreen', True)
    root.title("youtube video downloader")

    Label(root, text='Youtube Video Downloader', font='arial 50 bold').pack()

    link = StringVar()
    Label(root, text='Paste Link Here:', font='arial 35 bold').place(x=500, y=250)
    link_enter = Entry(root, width=100, textvariable=link).place(x=350, y=350)


    def Downloader():

        path = "C:/Users/DELL/Downloads"

        try:

            speak('please wait even if the program tells not responding')
            print('please wait even if the program tells not responding')

            url = YouTube(str(link.get()))
            video = url.streams.first()
            video.download(path)
            root.destroy()

            print('youre video has been downloaded to downloads')
            speak('youre video has been downloaded to downloads')

        except Exception as e:

            root.destroy()
            print('there seems to be a problem')
            speak('there seems to be a problem')
            print('returning to the main program')
            speak('returning to the main program')



    Button(root, text='DOWNLOAD', font='arial 25 bold', bg='pale violet red', padx=2, command=Downloader).place(x=550,
                                                                                                                y=400)
    root.mainloop()

def spaceship_war():

    import pygame

    pygame.font.init()
    pygame.mixer.init()

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

    BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

    BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
    BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))


    HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
    WINNER_FONT = pygame.font.SysFont('comicsans', 100)

    VEL = 5

    yellow_spaceship = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
    yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship, (w, h)), 90)

    red_spaceship = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
    red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship, (w, h)), 270)

    SPACE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

    def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):

        WIN.blit(SPACE, (0, 0))
        pygame.draw.rect(WIN, BLACK, BORDER)

        red_health_text = HEALTH_FONT.render("Health: " + str(red_health), 1, WHITE)
        yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)

        WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
        WIN.blit(yellow_health_text, (10, 10))

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

        if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:
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

            if red.colliderect(bullet):
                pygame.event.post(pygame.event.Event(RED_HIT))
                yellow_bullets.remove(bullet)

            elif bullet.x > WIDTH:
                yellow_bullets.remove(bullet)

        for bullet in red_bullets:

            bullet.x -= BULLET_VEL

            if yellow.colliderect(bullet):
                pygame.event.post(pygame.event.Event(YELLOW_HIT))
                red_bullets.remove(bullet)

            elif bullet.x < 0:
                red_bullets.remove(bullet)

    def draw_winner(text):

        draw_text = WINNER_FONT.render(text, 1, WHITE)
        WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))

        pygame.display.update()
        pygame.time.delay(3000)

    def video_game():

        red = pygame.Rect(700, 300, w, h)
        yellow = pygame.Rect(100, 300, w, h)

        red_bullets = []
        yellow_bullets = []

        red_health = 10
        yellow_health = 10

        clock = pygame.time.Clock()
        run = True

        while run:

            clock.tick(FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    run = False

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height // 2 - 2, 10, 5)
                        yellow_bullets.append(bullet)
                        BULLET_FIRE_SOUND.play()

                    if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                        bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                        red_bullets.append(bullet)
                        BULLET_FIRE_SOUND.play()

                if event.type == RED_HIT:
                    red_health -= 1
                    BULLET_HIT_SOUND.play()

                if event.type == YELLOW_HIT:
                    yellow_health -= 1
                    BULLET_HIT_SOUND.play()

            winner_text = ""
            if red_health <= 0 and yellow_health <= 0:
                speak('both reached 0 health at the same time,giving 5 health each')
                red_health = 5
                yellow_health = 5
            else:
                if red_health <= 0:
                    winner_text = "Yellow Wins!"

                if yellow_health <= 0:
                    winner_text = "Red Wins"

                if winner_text != "":
                    draw_winner(winner_text)
                    break

            keys_pressed = pygame.key.get_pressed()
            yellow_movement(keys_pressed, yellow)
            red_movement(keys_pressed, red)

            handle_bullets(yellow_bullets, red_bullets, yellow, red)

            draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
        pygame.quit()

    speak('you can close the game to continue main program')
    video_game()

def chatbot():

    chat = True

    while chat == True:

        message = input('message:')

        if message == 'assistant':
            chat = False

        else:
            ints = predict_class(message)
            res = get_response(ints, intents)
            print(res)

def brightness():

    bright = input('type a brightness between 1 to 100:')

    try:
        bc.set_brightness(bright)

    except:
        print('thats not a number between 1 to 100,brightness not changed,returning to the main program.')
        speak('thats not a number between 1 to 100,brightness not changed,returning to the main program.')
        pass







