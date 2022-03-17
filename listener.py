import speech_recognition as sr

class Listener:
    def __init__(self):
        self.listener_engine = sr.Recognizer()
    
    #This function will take command from Microphone
    def take_command(self):
        try:
            with sr.Microphone() as source:
                print('listening....')
                #listener.pause_threshold = 1
                #audio = listener.listen(source)
                self.listener_engine.adjust_for_ambient_noise(source, duration=0.5)
                voice = self.listener_engine.listen(source)
                command = self.listener_engine.recognize_google(voice,language='en-US')
                command = command.lower()
                return command
        except sr.RequestError:
            # API was unreachable or unresponsive
            print("api unavaialble")
        except sr.UnknownValueError:
            print("unable to recognize speech")