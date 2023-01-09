import os
import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "officeguyyt@gmail.com"
    password = os.getenv("EMAIL_NEWS_API_KEY")

    reciever = username
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)


if __name__ == "__main__":
    test_msg = """\
Subject: TEST

Message: TEST"""

    send_email(test_msg)
