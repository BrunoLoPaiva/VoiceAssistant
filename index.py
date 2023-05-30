import speech_recognition as sr
import re
import pyttsx3 

nome = ""
engine = pyttsx3.init()
engine.setProperty('voice', "com.apple.speech.synthesis.voice.luciana")

def returnMessage(msg):
    print(msg)
    engine.say(msg)
    engine.runAndWait()

while True:
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)

        returnMessage("Olá, estou à sua disposição!")
        audio = mic.listen(source)

        try:
            text = mic.recognize_google(audio, language='pt-BR')
            print(f"Texto reconhecido: {text}")

            if re.search(r'\bajudar\b', text):
                returnMessage('Como posso lhe ajudar?')  

            elif re.search(r'\bmeu nome é\b', text):
                nome = re.search('meu nome é (.*)', text).group(1)
                returnMessage(f'Olá {nome}')            
                   
        except sr.UnknownValueError:
            returnMessage("Desculpe, não consegui lhe entender.")
