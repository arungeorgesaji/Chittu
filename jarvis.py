from functions import *
from spaceship_war import *

prepare()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            wiki()

        elif 'open youtube' in query:
            youtube()

        elif 'open google' in query:
            google()

        elif 'open gmail' in query:
            gmail()

        elif 'the time' in query:
            time()

        elif 'repeat my words' in query:
            rep()

        elif 'buy jarvis' in query:
            exit()

        elif 'play spaceship war' in query:
            spaceship_war()
        else:
            chat()
