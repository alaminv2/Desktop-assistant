import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
# import pyaudio


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishing():
    hour = int(datetime.datetime.now().hour)

    if hour >= 5 and hour < 11:
        speak("Good Morning")

    elif hour > 11 and hour < 16:
        speak("Good Afternoon")

    elif hour > 16 and hour < 20:
        speak("Good Evening")

    else:
        speak("Good Night")

    speak("I am jervis. sir, how may i help you?")


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listning...')
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-US')

    except Exception as e:
        print('''I could not recognize what you are said.
        please say it again...''')
        return 'None'
    return query


if __name__ == '__main__':
    wishing()
    while True:
        query = command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            # query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open codeforces' in query:
            webbrowser.open('codeforces.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'open drive' in query:
            webbrowser.open('drive.google.com/drive/my-drive')

        elif 'open hacker rank' in query:
            webbrowser.open('hackerrank.com')

        elif 'open atcoder' in query:
            webbrowser.open('atcoder.com')

        elif 'open videos' in query:
            video_dir = "D:\\My Phone\\Videos"
            videos = os.listdir(video_dir)
            os.startfile(os.path.join(video_dir,videos[random.randint(0, len(videos)-1)]))

        elif 'open sublime text' in query:
            sublimePath = "C:\\Program Files (x86)\\Sublime Text 3\\sublime_text.exe"
            os.startfile(sublimePath)

        elif 'open codeforces' in query:
            pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.1\\bin\\pycharm64.exe"
            os.startfile(pycharmPath)

        elif 'open photoshop' in query:
            photoshopPath = "C:\\Program Files (x86)\\Adobe Photoshop CS6\\Photoshop.exe"
            os.startfile(photoshopPath)

        elif 'open chrome' in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif 'open android studio' in query:
            androidPath = "C:\\Program Files\\Android\\Android Studio1\\bin\\studio64.exe"
            os.startfile(androidPath)

        elif 'the time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'sir, now the time is {time}')

        elif 'exit' in query:
            exit()