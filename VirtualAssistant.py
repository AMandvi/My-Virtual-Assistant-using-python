import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import webbrowser
import pywhatkit
import smtplib
import getpass

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[33].id)
engine.say("Welcome, I am your virtual assistant")
engine.say('How can I help you?')  
engine.runAndWait()
engine.stop()
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

#talk function will talk/pronounce the string which is passed to it
def talk(text):
    engine.say(text)
    engine.runAndWait()
#This function will take command from Microphone
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source)
            command = listener.recognize_google(voice,language='en-US')
            command = command.lower()
            if 'echo' in command:
                print(command)
    except sr.RequestError:
        # API was unreachable or unresponsive
        print("api unavaialble")
    except sr.UnknownValueError:
        print("unable to recognize speech")
    return command   

#main program starting here named as run_echomandvialreja@gmail.com
def run_echo():
    command = take_command()
    print(command)
#logic for excuting tasks as per commands    
    if 'how are you' in command:
            talk("I am fine, Thank you")
            talk("How are you, Sir")
    elif 'fine' in command or "good" in command:
            talk("It's good to know that your fine") 
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)               
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'wikipedia' in command:
        talk('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences = 3)
        talk("According to Wikipedia")
        print(results)
        talk(results)
    elif 'open youtube' in command:
        talk("Here you go to Youtube\n")
        webbrowser.open("https://www.youtube.com/")
    elif 'joke' in command:
        talk(pyjokes.get_joke()) 
    elif 'email to' in command:
        try:
            talk("please type the required information")
            sendEmail()
        except:
            talk("Try again")    

    else:
        talk('Please say the command again.')

def sendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    email = getpass.getpass("Email:")
    password = getpass.getpass('Password please:')
    server.login(email,password)
    from_address = email
    to_address = email
    subject = input("enter the subject line:")
    message = input("enter the body message:")
    msg = "Subject:" +subject+ '\n' +message
    server.sendmail(from_address,to_address,msg)

    server.close()


while True:
    run_echo()            

