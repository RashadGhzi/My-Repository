
from win32com.client import Dispatch
import requests
import json


try:

    print("Select one of this option.")
    print("1.Read news."
          "\n2.Listen news.")


    choose_news = int(input())
    num = 1
    voice = Dispatch("SAPI.SpVoice")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=0f29031a6f164c81b3d34876ee20477f"
    news_text = requests.get(url).text
    news_dict = json.loads(news_text)
    news_article = news_dict['articles']


    if choose_news == 1:

        print("Select your option."
                    "\n1.Title."
                        "\n2.Description."
                            "\n3.Content."
                                "\n4.Everything.")

        choose_option = int(input())
        if choose_option == 1:
            for articles in news_article:
                print(f"Today news title no.{num} is : {articles['title']}")
                num += 1

        elif choose_option == 2:
            for articles in news_article:
                print(f"Today news description no.{num} is : {articles['description']}")
                num += 1

        elif choose_option == 3:
            for articles in news_article:
                print(f"Today news content no.{num} is : {articles['content']}")
                num += 1

        elif choose_option == 4:
            for articles in news_article:
                print(f"Today news article is : {articles}")

        else:
            print("Enter a valid keyword.")



    elif choose_news == 2:

        print("Select your option."
                    "\n1.Title."
                        "\n2.Description."
                            "\n3.Content."
                                "\n4.Everything.")

        choose_option = int(input())
        if choose_option == 1:
            for articles in news_article:
                print("For stop listening please enter 'done'.")
                voice.Speak(f"Today news title no.{num} is : {articles['title']}")
                voice.Speak("For next news title please press enter.")
                stop = input()
                if stop == 'done':
                    break
                num += 1

        if choose_option == 2:
            for articles in news_article:
                print("For stop listening please enter 'done'.")
                voice.Speak(f"Today news description no.{num} is : {articles['description']}")
                voice.Speak("For next news description please press enter.")
                stop = input()
                if stop == 'done':
                    break
                num += 1

        if choose_option == 3:
            for articles in news_article:
                print("For stop listening please enter 'done'.")
                voice.Speak(f"Today news content no.{num} is : {articles['content']}")
                voice.Speak("For next news content please press enter.")
                stop = input()
                if stop == 'done':
                    break
                num += 1

        if choose_option == 4:
            for articles in news_article:
                print("For stop listening please enter 'done'.")
                voice.Speak(f"Today news article is : {articles}")
                stop = input()
                if stop == 'done':
                    break

        else:
            print("Enter a valid keyword.")

    else:
        print("Please enter a valid keyword.")

except Exception:
    print("You entered an invlaid keyword.")