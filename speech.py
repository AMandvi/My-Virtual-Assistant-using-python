import pyttsx3

class Speech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[33].id)
    
    def initialSpeech(self):
        self.engine.say("Hi, I am your siri,your virtual assistant")
        self.engine.say('How can I help you?') 
        self.engine.runAndWait()
        self.engine.stop()

    #talk function will talk/pronounce the string which is passed to it
    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()