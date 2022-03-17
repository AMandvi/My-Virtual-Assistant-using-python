import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import webbrowser
import pywhatkit
import smtplib
import getpass
import os
from decouple import config
from speech import Speech
from listener import Listener
from interpreter import Interpreter

# listener = sr.Recognizer()
# listener = Listener()
# speech = Speech()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[33].id)
# engine.say("Hi, I am your siri,your virtual assistant")
# engine.say('How can I help you?') 
# engine.runAndWait()
# engine.stop()
#this is the code to print index of the female voice used in this program
# index = 0
# for voice in voices:
#     if voice.languages[0] == u'en_US':
#         print(voice, voice.id)
#         print("index is" + str(index))
#         engine.setProperty('voice', voice.id)
#         engine.say("Hello World!")
#         engine.runAndWait()
#         engine.stop()
#     index+=1

# #talk function will talk/pronounce the string which is passed to it
# def talk(text):
#     engine.say(text)
#     engine.runAndWait()

# #This function will take command from Microphone
# def take_command():
#     try:
#         with sr.Microphone() as source:
#             print('listening....')
#             #listener.pause_threshold = 1
#             #audio = listener.listen(source)
#             listener.adjust_for_ambient_noise(source, duration=0.5)
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice,language='en-US')
#             command = command.lower()
#             return command
#     except sr.RequestError:
#         # API was unreachable or unresponsive
#         print("api unavaialble")
#     except sr.UnknownValueError:
#         print("unable to recognize speech")

#main program starting here named as run_echomandvialreja@gmail.com
# def run_siri():
#     command = ''
#     command = listener.take_command()
#     if command and 'siri' in command:
#         print(command)
#         interpret_commands(command)

# def interpret_commands(command):
# #logic for excuting tasks as per commands    
#     if 'how are you' in command:
#             speech.talk("I am fine, Thank you")
#             speech.talk("How are you, Sir")
#             pass
#     elif 'fine' in command or "good" in command:
#             speech.talk("It's good to know that your fine") 
#             pass
#     elif 'play' in command:
#         song = command.replace('play', '')
#         speech.talk('playing ' + song)
#         pywhatkit.playonyt(song)      
#         pass         
#     elif 'time' in command:
#         time = datetime.datetime.now().strftime('%I:%M %p')
#         speech.talk('Current time is ' + time)
#         pass
#     elif 'wikipedia' in command:
#         speech.talk('Searching Wikipedia...')
#         command = command.replace("wikipedia", "")
#         results = wikipedia.summary(command, sentences = 3)
#         speech.talk("According to Wikipedia")
#         print(results)
#         speech.talk(results)
#         pass
#     elif 'open youtube' in command:
#         speech.talk("Here you go to Youtube\n")
#         webbrowser.open("https://www.youtube.com/")
#         pass
#     elif 'joke' in command:
#         speech.talk(pyjokes.get_joke()) 
#         pass
    

#     # elif "open my downloads folder" in command:
#     #         talk("Opening your downloads folder.")
#     #         os.system("/Users/mandv/Downloads/1-s2.0-S1110016820304063-main.pdf")
#     #         pass    
#     # elif 'mail to host' in command:
#     #     try:
#     #         talk("please type the required information")
#     #         sendEmail()
#         # except:
#         #     talk("Try again")  
#     elif 'email to' in command:
#         try:
#             speech.talk("what should i send")
#             content = listener.take_command()
#             print(content)
#             to = "mandvialreja93@gmail.com"
#             sendEmail(to, content)
#             speech.talk("Email has been sent to mandvi")
#         except:
#             print("something went wrong")    


#     else:
#         speech.talk('Please say the command again.')

# #Virtual assistant can send mail to host email using app password
# # def Mailtohost():
# #     server = smtplib.SMTP('smtp.gmail.com', 587)
# #     server.ehlo()
# #     server.starttls()
# #     email = getpass.getpass("Email:")
# #     password = getpass.getpass('Password please:')
# #     server.login(email,password)
# #     from_address = email
# #     to_address = email
# #     subject = input("enter the subject line:")
# #     message = input("enter the body message:")
# #     msg = "Subject:" +subject+ '\n' +message
# #     server.sendmail(from_address,to_address,msg)

#     #server.close()

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     EMAIL = config('LOGIN_EMAIL')
#     PASS = config('LOGIN_PASSWORD')
#     server.ehlo()
#     server.starttls()
#     server.login(EMAIL, PASS)
#     speech.talk('Sending email now')
#     server.sendmail("mandvialreja93@gmail.com", to, content)
#     server.close()


# def sendEmail(to,content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     email = getpass.getpass("Email:")
#     password = getpass.getpass('Password please:')
#     server.login(email,password)
#     server.login(email,password)
#     server.sendmail("mandvialreja93@gmail.com", to, content)
#     server.close()

# speech.initialSpeech()

def main():
    interpreter = Interpreter()
    speech = Speech()
    speech.initialSpeech()
    while True:
        interpreter.wait_for_siri()       

if __name__ == "__main__":
    main()

#ctrl+C to stop listening