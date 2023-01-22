import schedule, time, os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

motivational_quotes = [
                "The scariest moment is always just before you start. - Stephen King, On Writing: A Memoir of the Craft"
                "It starts with a single step. You just have to take it. - Stephen King, The Stand",
                "The best way to be successful is to make the other guy look bad. - Stephen King, The Long Walk",
                "We make up horrors to help us cope with the real ones. - Stephen King, The Stand",
                "Monsters are real, and ghosts are real too. They live inside us, and sometimes, they win. - Stephen King, It",
                        ]


password = os.environ['app_password']
username = os.environ['email']


def mail():
    email = random.choice(motivational_quotes)
    server = "smtp.gmail.com"
    port = 587
    s = smtplib.SMTP(host=server, port=port)
    s.starttls()
    s.login(username, password)

    message = MIMEMultipart()
    message["To"] = os.environ['email']
    message["From"] = "Pasi! Mini Me!"
    message["Subject"] = "Motivational quote"
    message.attach(MIMEText(email, "html"))
    
    s.send_message(message)
    del message



def print_me():
    mail()
    print("Email sent")

schedule.every(60).seconds.do(print_me)

while True:
    schedule.run_pending()
    time.sleep(1)