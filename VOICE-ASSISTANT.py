import pyttsx3 as p  #text to speech conversion
import speech_recognition as sr#speech to text conversion
import webbrowser# websearches
import pywhatkit# provide functionality playing on youtube
from assistantfunctions import tell_time #built in file
from assistantfunctions import time


engine = p.init("sapi5") # defaultly available on windows 
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
engine.setProperty('rate',180)
engine.setProperty('volume',1.0)
def speakaudio(audio):#
    engine.say(audio)
    engine.runAndWait()
def takecommand(): 
    r = sr.Recognizer() 
    with sr.Microphone() as source:  
        print("Listening...")
        r.adjust_for_ambient_noise(source , duration=0.5)  #
        r.pause_threshold = 0.5
        r.energy_threshold = 500
        try:
            audio = r.listen(source,0,4)  #start listening
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected within the time frame.")
            return "None"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #convert to text
        print(f"User said: {query}\n")
    except Exception as e:
        speakaudio("Say that again...")
      
        return "None" 
    return query
if __name__ == "__main__":
    
      while True: # listening in infinity
          query = takecommand().lower()
          if "wake up" in query or "utha ja bhai" in query:
            speakaudio("hello sir i am yor voice assistant")
            time()        
          elif "close the program" in query or "stop" in query:#
            speakaudio("Closing the program Bye sir have a good day sir")
            break
          elif "hello" in query:
            speakaudio("Hello sir  how are you ")
          elif "fine" in query:
            speakaudio("That's great sir ")
          elif " how are you " in query:
             speakaudio("i m good how can i assist you sir")
          elif "thanks" in query or "thankyou" in query or "very much" in query:
             speakaudio(" you are welcome sir")
          elif "time now" in query:
           tell_time()   
          elif "play" in query:
           song = query.replace("play","")
           speakaudio("playing" + song)#using pywhatkit for playing 
           pywhatkit.playonyt(song)
          elif "google" in query:
           search_term = query.replace("google", "").strip()
           search_url = f"https://www.google.com/search?q={search_term}"
          elif "wikipedia" in query:
           search_term = query.replace("wikipedia", "").strip()
           search_url = f"https://www.wikipedia.com/search?q={search_term}"
           print(search_url)
           webbrowser.open(search_url)
          elif "open" in query:
           s1= query.replace("open", "").strip()
           speakaudio("opening" + s1)
           s2 = f"https://www.google.com/search?q={s1}"#
           webbrowser.open(s2)
          else:
             pass