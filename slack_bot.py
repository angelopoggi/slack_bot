import slack
from config import SLACK_TOKEN
import datetime
import time
import random
import dad_jokes


def bill_bot():
    currentTime = datetime.datetime.now()
    client = slack.WebClient(token=SLACK_TOKEN)
    if currentTime.hour == 9:
        client.chat_postMessage(channel='#provisioninginternal', text="Morning Everyone!")
    if currentTime.hour == 16:
        client.chat_postMessage(channel='#provisioninginternal', text="Night Everyone!")
    randomTime = random.randrange(9,15,1)
    if currentTime.hour == datetime:
        currentJoke = dad_jokes()
        client.chat_postMessage(channel='#provisioninginternal', text=currentJoke['body'][0]['setup'])
        time.sleep(2)
        client.chat_postMessage(channel='#provisioninginternal', text=print(currentJoke['body'][0]['punchline']))

if __name__== '__main__':
    bill_bot()





