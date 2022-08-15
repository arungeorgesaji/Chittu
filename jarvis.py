from function import *

if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            wiki(query)

        elif 'time' in query:
           time()

        elif 'repeat my words' in query:
           rep()

        elif 'news' in query:
            latestnews()

        elif 'temperature' in query:
            temp()

        elif 'weather' in query:
            weth()

        elif "open" in query:
            openappweb(query)

        elif "close" in query:
            closeappweb(query)

        elif 'buy jarvis' in query:
            exit()

        elif 'play spaceship war' in query:
            from spaceship_war import *
            spaceship_war()

        elif 'search pokemon' in query:
            pokedex()

        elif query == 'none':
            pass

        elif 'sleep' in query:
            sleep()

        else:
            chat(query)
