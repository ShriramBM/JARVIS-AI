import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
#engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        helo =  speak("good Morning")
    elif hour >=13 and hour <= 18:
        helo = speak("good Afternoon")
    else:
        helo = speak("have a good night ")
    speak(f"{helo}I am jarvis. How are you Stark")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("litening,..,.,.,.,")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("I recognized")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        speak(f"You said: {query}")
    
    except Exception as e:
        return "none"
    
    return query


if __name__ =="__main__":
    wishme()
    while True:
        string = takecommand().lower()

        #Logic Start
         
        if 'wikipedia' in string:
            speak("Searching Wikipedia")
            string = string.replace("wikipedia","")
            results = wikipedia.summary(string, sentences=2)
            speak("According to wikipedia")
            print(results)        
            speak(results)
        
        elif 'open youtube' in string:
            webbrowser.open("youtube.com")

        elif 'open facebook' in string:
            webbrowser.open("facebook.com")
        
        elif'open google' in string:
            webbrowser.open("google.com")

        elif'hey jarvis' in string:
            speak("How you doing man")
        
        elif 'my name' in string:
            speak("your name is John cena")

        elif 'exit'in string:
            speak("Have a nice Day")
            exit()
