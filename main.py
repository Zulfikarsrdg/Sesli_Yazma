import os
import speech_recognition as sr
import webbrowser

dinle = sr.Recognizer()

with sr.Microphone() as source:
    print("Lütfen Konuşun")
    audio = dinle.listen(source)

data = ""
try:
    data = dinle.recognize_google(audio, language='tr-tr')
    data = data.lower()
    if "youtube" in data or "linkedin" in data or "github" in data or "facebook" in data or "twitter" in data or "twitch" in data or "instagram" in data:
        search_url = "https://www.google.com/search?q="+data+".com"
        webbrowser.open(search_url)
    else:
        print("Bunu Söyledin: " + data)
except sr.UnknownValueError:
    print("Ne dediğini anlamadım, tekrarlar mısın?")

