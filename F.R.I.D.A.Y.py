import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import subprocess as sp
friday = pyttsx3.init()
voice = friday.getProperty("voices")
friday.setProperty("voice", voice[1].id )        #set giọng nam hoặc nữ, voice[0].id là giọng nam, còn voice[1].id là giọng nữ
def speak(audio):
    print("F.R.I.D.A.Y" + audio)
    friday.say(audio)
    friday.runAndWait()
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)
def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour < 24:
        speak("Good night sir!")
    speak("What can I help for you?")
def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold = 2        #dừng bao nhiêu giây trước khi nghe lệnh mới
        audio = c.listen(source)                #nghe
    try:
        query = c.recognize_google(audio,language="en")          #nhan dien query voi nhan dien cua google
        print("Bao Dep Trai: " + query)
    except sr.UnknownValueError:
        print("Please repeat or typing the command")
        #khi mà nói nó không nhận lệnh thì gõ vào luôn
        query = str(input("Your order is: "))
    return query
if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()     #chuyển mệnh lệnh thành dạng không viết hoa để máy nó dễ nhận diện
        if "google" in query:
            speak("What should I search sir?")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on google")
        elif "youtube" in query:
            speak("What should I search sir?")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on youtube")
        elif "Facebook" in query:
            search = command().lower()
            url = f"https://www.facebook.com/"
            wb.get().open(url)
            speak(f"Here is your Facebook account")
        elif "wikipedia" in query:
            speak("What should I search sir?")
            search = command().lower()
            url = f"https://www.wikipedia.org/wiki/{search}"
            wb.get().open(url)
            speak(f"Here is your {search} on wikipedia")
        elif "open camera" in query:
            sp.run('start microsoft.windows.camera:', shell=True)
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("FRIDAY is quitting sir" + " " + "Goodbye boss!")
            quit()