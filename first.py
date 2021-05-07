import pyttsx3
import datetime

import speech_recognition as sr

import os

import webbrowser

import pyjokes

import randfacts

import weathercom
import json        #this also needed for weather, its already present in system

import requests    #for news

import wikipedia
from oyt import *

from sel import *


import psutil             #check cpu usage, battery
import pyautogui          #check screenshot

import word2number

from word2number import w2n




#pyttsx3= python text to speech converter x3
engine = pyttsx3.init('sapi5') #this is for windows users || it is the api key used toaccess the voices available on windows
voices = engine.getProperty('voices')
#print(voices[0].id)    #name of voice 1 male
#print(voices[1].id)     #name of voice 2 female
#print(voices)           #to see number of voices, we see there are 2 ids so we know there are two voices
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() #we dont want the speaking thing to run away once they speak. so run and keep waiting hence run and wait

def wish():   #for greeting
    hour = int(datetime.datetime.now().hour) #from datetime lib and datetime package we choose now 
    #hour is in form of 24 hour
    if(hour>0 and hour<12):
        speak("Good Morning")
    elif(hour>=12 and hour<18):
        speak("Good afternoon")
    else:
        speak("Good evening")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8 #this is same as default tho so u dont haave to type it
        #above line i samount of time it waits for after the person stops working before it stops working
        audio =r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language="en-in")    #we are using the language from google and indian english
            print(f"User said :{query}\n ")

        except Exception as e:
            print("I am sorry :[ please repeat yourself")
            return "None"
        return query


#pip install weathercom
def weatherReport(city):
    weatherdetails = weathercom.getCityWeatherDetails(city)
    temp = json.loads(weatherdetails)["vt1observation"]["temperature"]   #vt1observation is the api key of weather.com which is the webist we are refeering to for this data
    humidity = json.loads(weatherdetails)["vt1observation"]["humidity"]
    phrase = json.loads(weatherdetails)["vt1observation"]["phrase"]
    return temp, humidity,phrase 




if __name__ == '__main__':            #name,main are global variables. if u dont use it then u cant use this in other scripts or use this script in other programs
    wish()
    speak("I am Tanya. How are you?")
    while True:
        text = takeCommand().lower()
        if "what" and "about" and "you" in text:
            speak("I am good what can i do for you?")
        elif "date" in text:
            #module.class.function
            curDate = datetime.datetime.now().strftime("%d:%B:%Y")
            curDay = datetime.datetime.now().strftime("%A")
            speak(f"Today's day is {curDate} and the day is {curDay}")

            
        elif "time" in text:  
            #hour=%H is for 24 hour and %I is for 12 hour %p is am/pm
            curTime=datetime.datetime.now().strftime("%I:%M:%S %p")
            speak(f"The time is {curTime}")

#to open applications that are already present
        elif "open" and "code" in text:
            speak("Open Visual Studio Code")
            codePath = "C:\\Users\\Anoushka C\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

        elif "git" and "bash" in text:
            speak("Opening Git Bash")
            codePath = "C:\Program Files\Git\git-bash.exe --cd-to-home"

        elif "word" in text:
            speak("Opening Word")
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
#to open web browsers
        elif "open" and "google" in text:
            speak("Opening Google in your browser")
            webbrowser.open(url="https://google.com")
        
        elif "open youtube" in text:
            speak("Opening Youtube in your browser")
            webbrowser.open(url="https://youtube.com")

        elif "open" and "netflix" in text:
            speak("Opening Netflix in browser")
            webbrowser.open(url="https://www.netflix.com")
#for jokes lol   pip install pyjokes
        elif "joke" in text:
            J = pyjokes.get_joke("en","neutral")  
            print(J)
            speak(J)  

#for facts do pip install randfacts        
        elif "fact" in text:
            F = randfacts.getFact()  
            print(F)
            speak(F)  

#for reading out the first few lines of wikipedia of a certain topic
#pip install wikipedia
        elif "according to wikipedia" in text:
            speak("Searching to wikipedia...")
            word = text.replace("wikipedia","")
            results = wikipedia.summary(word,sentences=2)
            speak("According to wikipedia...")
            print(results)
            speak(results)


        elif "play" and "online" in text:
            speak("What do you want me to play?")

            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 0.8 #this is same as default tho so u dont haave to type it
        #above line i samount of time it waits for after the person stops working before it stops working
                audio =r.listen(source)
                print("Recognizing...")
                title = r.recognize_google(audio,language="en-in")    #we are using the language from google and indian english
            print("Playing {} in youtube".format(title))
            speak("Playing {} in youtube".format(title))
            bot = music()
            bot.play(title)


        elif "information" in text:
            speak("What is the topic you want to search?")

            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 0.8 #this is same as default tho so u dont haave to type it
        #above line i samount of time it waits for after the person stops working before it stops working
                audio =r.listen(source)
                print("Recognizing...")
                topic = r.recognize_google(audio,language="en-in")    #we are using the language from google and indian english
            print("Searching {} in wikipedia".format(topic))
            speak("Searching {} in wikipedia".format(topic))
            assit = info()
            assit.get_info(topic)


        elif "weather" in text:
            print("sure, please tell me the city?")
            speak("sure, please tell me the city?")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 0.8 #this is same as default tho so u dont haave to type it
        #above line i samount of time it waits for after the person stops working before it stops working
                audio =r.listen(source)
                print("Recognizing...")
                city = r.recognize_google(audio,language="en-in")    #we are using the language from google and indian english
            temp, humidity, phrase = weatherReport(city)
            print("currently in:"+ city + " the temperature is "+str(temp)+" degrees celcius, with humidity " +str(humidity)
            + " percent and sky is "+phrase)
            speak("Weather Report: currently in: "+ city + "the temperature is "+str(temp)+" degrees celcius, with humidity " +str(humidity)
            + " percent and sky is "+phrase)

            
        #new pre code in word doc
        elif "news" in text:
            api_address = "https://newsapi.org/v2/top-headlines?country=in&apiKey=c674aa265cd740828e095eb29b4cc279"
            response = requests.get(api_address)
            news_json = json.loads(response.text)
            print("How many articles?")
            speak("How many articles?")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                r.pause_threshold = 0.8 #this is same as default tho so u dont haave to type it
        #above line i samount of time it waits for after the person stops working before it stops working
                audio =r.listen(source)
                print("Recognizing...")
                num = r.recognize_google(audio,language="en-in")
            #print(num)
            count = w2n.word_to_num(num)
            print('Here are todays top headlines:')
            speak('Here are todays top headlines:')

            for news in news_json['articles']:
                if count > 0:
                    T = str(news['title'])
                    #T = str(news['title']+new['description']) if u also want description not just headline
                    print(T)
                    speak(T)
                    count -= 1    #count is less 1




        elif "cpu stats" in text:
            usage = str(psutil.cpu_percent)
            speak('CPU is at '+ usage)
            
            battery = psutil.sensors_battery()
            speak('battery is at')
            speak(battery.percent)

        elif "take screenshot" in text:
            img = pyautogui.screenshot()
            speak("done")
            img.save('C:\\Users\\Anoushka C\\OneDrive\\Pictures\\Screenshots')


        elif "take notes" in text:
            file = open('notes.txt', 'w')
            # w for write
            speak('Should i include date and time?')
            ans = takeCommand()
            speak("What should I write ")
            notes = takeCommand()
            if "yes" or "sure" in ans:

                curDate = datetime.datetime.now().strftime("%d:%B:%Y")
                curTime=datetime.datetime.now().strftime("%I:%M:%S %p")
                file.write(curTime)
                file.write(curDate)
                file.write(':-')
                file.write(notes)
                speak("Done taking notes")
            
            else:
                file.write(notes)
                speak("Done taking notes")


        elif "show notes" in text:
            speak("Opening notes")
            file = open('notes.txt','r')
            print(file.read())

        elif "go offline" in text:
            speak("Going offline")
            quit()