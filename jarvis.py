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

        elif 'temperature' == query:
            temp()

        elif 'weather' in query:
            weth()

        elif "open" in query:
            openappweb(query)

        elif "close" in query:
            closeappweb(query)

        elif 'buy jarvis' in query:
            exit()

        elif 'bhai jarvis' in query:
            exit()

        elif "youtube" in query:
            searchYoutube(query)

        elif 'google' in query:
            searchGoogle(query)

        elif 'tired' in query:
            tired()

        elif 'internet speed' in query:
            internet_speed()

        elif 'rock paper scissors' in query:
            rock_paper_scissors()

        elif 'video game' in query:
            spaceship_war()

        elif 'search pokemon' in query:
            pokedex()

        elif 'generate password' in query:
            password()

        elif query == "none":
            pass

        elif 'sleep' in query:
            sleep()

        elif 'cpu temperature' in query:
            cpu_temp()

        elif 'guess number' in query:
            num_guess_game()

        elif 'whatsapp later' in query:
            what_mess()

        elif 'audiobook' in query:
            audiobook()

        elif 'disturb' in query:
            spam()

        elif 'download' in query:
            download()

        elif 'chat' in query:
            chatbot()

        else:
            chat(query)

