import requests
from send_email import send_email
from datetime import date

api_key = "8625d6b7d7e449b6a2bdf6a7875e8bdb"
url = "https://newsapi.org/v2/everything?domains=wsj.com&apiKey=8625d6b7d7e449b6a2bdf6a7875e8bdb"

request = requests.get(url)
content = request.json()

date = date.today()

message = f"""\
Subject: News from WSJ for {date}
"""

for article in content["articles"]:
    tempmsg = "\n\n" + str(article["title"]) + "\n" + \
               str(article["description"]) + "\n" + str(article["url"])

    # API content has chinese in it. convetrtoascii func does not like it
    if tempmsg.isascii():
        message = message + tempmsg

print(message)
send_email(message)
