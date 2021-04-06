import smtplib
import config
import time
import os
import webbrowser
def send_email(subject, msg):
    try:
        server = smtplib.SMTP("smtp.gmail.com: 587")
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, recipient, message)
        server.quit()
    except:
        time.sleep(0.01)
named_tuple = time.localtime()
time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
subject = "PC was logged on"
msg = ("Your Computer was accessed at " + time_string)
recipient = ""
send_email(subject, msg)


