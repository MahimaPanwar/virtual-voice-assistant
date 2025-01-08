import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import time
# import openai
# from config import apikey
# import random

try:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()


    def greet():
        hour = int(datetime.datetime.now().hour)
        print(hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning !")
        elif hour >= 12 and hour < 18:
            speak("Good Afternoon !")
        else:
            speak("Good Evening !")
        speak("Welcome , I am your personal google assistant")


    def VoiceCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:

            print("Recognizing...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "None"
        return query


    # def ai(prompt):
    #     openai.api_key = apikey
    #     text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"
    #
    #     response = openai.Completion.create(
    #         model="text-davinci-003",
    #         prompt=prompt,
    #         temperature=0.7,
    #         max_tokens=256,
    #         top_p=1,
    #         frequency_penalty=0,
    #         presence_penalty=0
    #     )
    #
    #     # print(response["choices"][0]["text"])
    #     text += response["choices"][1]["text"]

    def get_current_time():
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        # speak("The current time is " + current_time)
        print("The current time is", current_time)


    def get_current_date():
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        # speak("Today's date is " + current_date)
        print("Today's date is", current_date)


    get_current_time()
    get_current_date()


    if __name__ == '__main__':
        greet()
        while True:
            work = VoiceCommand().lower()
            if 'hello' in work:
                if 'hello' in work:
                    speak('hi , how can i help you')
                    print('hi , how can i help you')

            if "wikipedia" in work:
                speak("Searching wikipedia...")
                webbrowser.open("https://www.wikipedia.com/")
                time.sleep(1)

            elif 'open notepad' in work:
                speak('opening notepad for you.......')
                path = ("c:\\windows\\system32\\notepad.exe")
                os.startfile(path)
            elif 'close notepad' in work:
                speak('closing notepad wait.....')
                os.system('c:\\windows\\system32\\taskkill.exe /F /IM notepad.exe')
                time.sleep(1)

            elif 'open youtube' in work:
                speak("Here you go to Youtube\n")
                webbrowser.open("https://www.youtube.com/")
                time.sleep(1)

            elif 'open google' in work:
                speak("Here you go to Google\n")
                webbrowser.open("https://www.google.co.in/")
                time.sleep(1)

            elif 'play music' in work:
                speak('opening music player....')
                path = ("C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe")
                os.startfile(path)
                time.sleep(1)

            elif 'open mail' in work:
                speak("Here you go to mail\n")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                time.sleep(1)

            elif 'open whatsapp' in work:
                speak("opening whatsapp for you\n")
                webbrowser.open("https://web.whatsapp.com/")
                time.sleep(1)

            # elif 'using ai'.lower() in work.lower():
            #     ai(prompt=work)

            elif 'exit' in work:
                speak("Thanks for giving me your time ..... have a nice day....")
                print("Thanks for giving me your time ..... have a nice day....")
                exit()

except BaseException as ex:
    print(f"error occured = {ex}")

finally:
    print("Thank you .....bye..have a nice day")
