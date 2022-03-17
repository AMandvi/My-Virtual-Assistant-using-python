import smtplib
from decouple import config
from speech import Speech

class EmailService:
    def __init__(self):
        self.speech = Speech()

    def sendEmail(self, to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        EMAIL = config('LOGIN_EMAIL')
        PASS = config('LOGIN_PASSWORD')
        server.ehlo()
        server.starttls()
        server.login(EMAIL, PASS)
        self.speech.talk('Sending email now')
        server.sendmail("mandvialreja93@gmail.com", to, content)
        server.close()