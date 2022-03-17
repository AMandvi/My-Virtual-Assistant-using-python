from listener import Listener
from speech import Speech
import speech_recognition as sr
import datetime
import wikipedia
import pyjokes
import webbrowser
import pywhatkit
import smtplib
from decouple import config
from emailService import EmailService

class Interpreter:
    def __init__(self):
        self.listener = Listener()
        self.speech = Speech()
        self.email_service = EmailService()

    def wait_for_siri(self):
        command = ''
        while (command is None or 'siri' not in command):
            command = self.listener.take_command()
            print(command)
        print(command)
        self.interpret_command(command)

    def interpret_command(self, command):
        #logic for excuting tasks as per commands    
        if 'how are you' in command:
                self.speech.talk("I am fine, Thank you")
                self.speech.talk("How are you, Sir")
                pass
        elif 'fine' in command or "good" in command:
                self.speech.talk("It's good to know that your fine") 
                pass
        elif 'play' in command:
            song = command.replace('play', '')
            self.speech.talk('playing ' + song)
            pywhatkit.playonyt(song)      
            pass         
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            self.speech.talk('Current time is ' + time)
            pass
        elif 'wikipedia' in command:
            self.speech.talk('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences = 3)
            self.speech.talk("According to Wikipedia")
            print(results)
            self.speech.talk(results)
            pass
        elif 'open youtube' in command:
            self.speech.talk("Here you go to Youtube\n")
            webbrowser.open("https://www.youtube.com/")
            pass
        elif 'joke' in command:
            self.speech.talk(pyjokes.get_joke()) 
            pass
        

        # elif "open my downloads folder" in command:
        #         talk("Opening your downloads folder.")
        #         os.system("/Users/mandv/Downloads/1-s2.0-S1110016820304063-main.pdf")
        #         pass    
        # elif 'mail to host' in command:
        #     try:
        #         talk("please type the required information")
        #         sendEmail()
            # except:
            #     talk("Try again")  
        elif 'email to' in command:
            try:
                self.speech.talk("what should i send")
                content = self.listener.take_command()
                print(content)
                to = "mandvialreja93@gmail.com"
                self.email_service.sendEmail(to, content)
                self.speech.talk("Email has been sent to mandvi")
            except:
                print("something went wrong")    
        else:
            self.speech.talk('Please say the command again.')
