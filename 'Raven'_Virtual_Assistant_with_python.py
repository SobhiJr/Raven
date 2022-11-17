from email.mime import audio
from http import server
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()
#pack voice from the system
Lady_english="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
Male_english="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
Lady_spanish="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0"
#those should be the ones on the system for Windows
engine.setProperty('rate', 150)
engine.setProperty('volume',1)
engine.setProperty('voice',Lady_english)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Today's date is")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning!")
    elif hour>= 12 and hour < 18:
        speak("Good Afternoon!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("Welcome Back!")
    date()
    speak("This is Rayvin I'm happy to help, How can I help you today?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"
    
    return query

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abzc@gmail.com', '123')
    server.sendmail('abzc@gmail.com', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("E:\'Emma'_AI_Assistant_with_python")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time ()
        elif 'date'in query:
            date()
        elif 'Wikipedia' in query:
            speak("Searching...")
            query = query.replace("Wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak('What should I say?')
                content = takeCommand()
                to = 'xyz@gmail.com'
                sendemail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send Email")
        elif 'search in chrome' in query:
            speak("What should I search")
            chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search +'.com')
        elif 'logout' in query:
            os.system('shutdown -1')
        elif 'shutdown' in query:
            os.system('shutdown /s /t -1')
        elif 'restart' in query:
            os.system('shutdown /r /t -1')
        elif 'play song' in query:
            song_dir = 'D:\Movies'
            songs = os.listdir(song_dir)
            os.startfile(os.path.join(song_dir, songs[0]))
        elif 'remembar that' in query:
            speak("What should I remember?")
            data = takeCommand()
            remember = open('Data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'do you know anything' in query:
            remember = open('Data.txt', 'r')
            speak("You told me to remember that" + remember.read())
        elif 'screenshot' in query:
            screenshot()
            speak("Done!")
        elif 'cpu' in query:
            cpu()
        elif 'joke' in query:
            jokes()
        elif 'offfline' in query:
            quit()