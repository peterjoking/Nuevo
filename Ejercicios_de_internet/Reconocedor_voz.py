import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print('Decí algo')
    audio = r.listen(source)
    try:
        text= r.recognize_google(audio, language='es-Es')
        print("lo que dijiste es: {}".format(text))
    except:
        print("no escuché, repita por favor")

#Problemas para funcinar, me pide Pyaudio que a su vez no consigue instalar el pycharm.