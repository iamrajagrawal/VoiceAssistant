import pyttsx3
import datetime
import speech_recognition as spr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def takeCommand(): #Microphone input to text(String)
    r=spr.Recognizer()
    with spr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recognizing...')
        query=r.recognize_google(audio, language='en-in')
        print('User said :', query)
    except Exception:
        print("Sorry Sir, I didn't get it. Please say it again...")
        return "None"
    return query


def speak(command): #Text to Audio
    engine.say(command)
    engine.runAndWait()


def wishInitiator():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('Good Morning')
    elif hour>12 and hour<=16:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
    speak('I am your personal Voice Assistant Sir, Please tell me how may I help you?')


if __name__=="__main__":
    wishInitiator()
    while(True):
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia...')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play music' in query:
            musicdir = 'C:\\Users\\RAJ AGRAWAL\\Downloads\\Transcend'
            songs=os.listdir(musicdir)
            songnum = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(musicdir, songs[songnum]))

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M")
            print(time)
            speak(f'Sir the time is {time}')

        elif 'my name' in query:
            speak('Sir, Your name is Raj Agrawal')

        elif 'my profession' in query:
            speak('Sir, You are working as a software engineer')
        
        elif 'i live' in query:
            speak('As far as I know you live in Bangalore sir')

        elif 'you are great' in query:
            speak('My pleasure sir')
        
        elif 'write a note' in query:
            notepad = 'C:\\Windows\\system32\\notepad.exe'
            os.startfile(notepad)


        elif 'stop' in query:
            speak('Going in hybernation mode Sir...Have a great day...Good bye')
            break