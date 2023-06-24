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
    print("Bunu Söyledin: " + data)

    if "youtube" or "linkedin" or "github" or "facebook" or "twitter" or "twitch" or "instagram" in data:
        search_query = data.replace("", "")
        search_url = "https://www.google.com/search?q=" + search_query
        webbrowser.open(search_url)

except sr.UnknownValueError:
    print("Ne dediğini anlamadım, tekrarlar mısın?")
