import pyttsx3
import datetime
import wikipedia
import re
import webbrowser
import googlesearch
import smtplib
import speech_recognition as S_R
bye=['bye','tata','sayonara','over and out']
wiki=['wiki','wikipedia']
biswa=['biswa','biswarup','bitto','biswarup bhattacharjee','vishwa']
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',170)
engine.setProperty('volume',8.0)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("GOOD MORNING")
    elif hour >12 and hour < 18:
        speak("GOOD AFTERNOON")
    else:
        speak("GOOD EVENING")
def takecommand():
    r=S_R.Recognizer()
    with S_R.Microphone() as source:
        print("Listening.....")
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        print("say again please...")
        return "None"
    return query
if __name__ == '__main__':
    wishme()
    #speak('hello boss,I am JARVIS,I am preparing for your help,THANKS FOR CREATING ME')
    while True:
        query=takecommand().lower()
        if any(re.findall('|'.join(wiki),query)):
            speak("Searching in Wiki")
            results=wikipedia.summary(query,sentences=2)
            result=wikipedia.summary(query,sentences=10)
            speak("According to Wikipedia")
            print("final search result : ",result,"For Knowing more: ",wikipedia.page(query).url)
            speak(results)
        elif any(re.findall('|'.join(bye),query)):
            speak("OK BYE SIR")
            print("Good Bye")
            exit()
        elif 'send email'  in query:
                speak("Opening gmail")
                webbrowser.open("https://mail.google.com")
        elif 'open youtube' in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Opening google")
            webbrowser.open("google.com")
        elif 'open bingo' in query:
            webbrowser("https://www.bingo.com/")
        elif any(re.findall('|'.join(biswa),query)):
            speak("Hello Boss, I am your Jarvis,Thanks for creating me ")
        elif query=="vishwaroop":
            speak("You mean Biswaroop,he is my BOSS,THANKS BOSS FOR CREATING ME")
        else:
            if not str(query).strip():
               speak("I DID'NT LISTEN")
            elif len(query)>=5:
                speak("I DID NOT ABLE TO DO YOUR WORK SO I SEARCHING IN WEB")
                for j in googlesearch.search(query,num=12,stop=12,pause=2):
                    print(j)
            else:
                continue
