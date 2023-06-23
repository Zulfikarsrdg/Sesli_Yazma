import os
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Lütfen Konuşun")
    audio=r.listen(source)

data=""
try:
    data=r.recognize_google(audio,language='tr-tr')
    data=data.lower()
    print("Bunu Söyledin:"+data)
except sr.UnknownValueError:
    print("Ne dediğini anlamadım tekrarlar mısın?")

