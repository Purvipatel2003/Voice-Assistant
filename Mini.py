import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import requests
from bs4 import BeautifulSoup


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=0 and hour<12:
        speak("Good AfterNoon!") 
    else:
        speak("Good Evening!")

    speak("I am lolo. Please tell me how can I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)    
        print("Say that again please...") 
        return "None" 
    return query

    def sendEmail(to, content):
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.login('youremail@gmail.com', 'your-password')
     server.sendmail('youremail@gmail.com', to, content)
     server.close()

if __name__=="__main__" :
   speak("Hey purvi")
   wishMe()
while True:
    
        query = takeCommand().lower() 
       
        if 'wikipedia' in query: 
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open chrome' in query:
            webbrowser.open("chrome.com")

        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        
        elif 'play music' in query:
            PURVI= 'C:\\Users\\patel\\OneDrive\\PURVI\\Music\\Favourite'
            songs = os.listdir(PURVI )
            print(songs)    
            os.startfile(os.path.join(PURVI, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f" the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\patel\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        # elif 'email to purvi' in query:
        #     try:
        #         speak("What should I say?")
        #         content = takeCommand()
        #         to = "patelpurvi2003@gmail.com"    
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend. I am not able to send this email") 

        elif 'joke' in query:
             speak(pyjokes.get_joke())

        elif 'temperature' in query:
            search = "temperature in gujarat"
            url=f"https://www.google.com/search?q={search}"
            r= requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")


 