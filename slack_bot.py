import slack
from config import SLACK_TOKEN
import datetime
import time
import random
import dad_jokes
import schedule


def bill_bot(randomTime):
    currentTime = datetime.datetime.now()
    client = slack.WebClient(token=SLACK_TOKEN)
    if currentTime.hour == 9:
        client.chat_postMessage(channel='#bot-testing', text="Morning Everyone!")
    if currentTime.hour == 16:
        client.chat_postMessage(channel='#bot-testing', text="Night Everyone!")
    if currentTime.hour == randomTime:
        currentJoke = dad_jokes.dad_jokes()
        client.chat_postMessage(channel='#bot-testing', text=currentJoke[0])
        time.sleep(2)
        client.chat_postMessage(channel='#bot-testing', text=currentJoke[1])
        
def random_num_gen():
    randomTime = random.randrange(9, 15, 1)
    return randomTime
if __name__== '__main__':
    #Morning run
    schedule.every().day.at("09:00:00").do(bill_bot)
    randomTime = schedule.every().day.at("09:00:00").do(random)
    if randomTime == 9:
        schedule.every().day.at(f"0{randomTime}:00:00")
    elif randomTime in random(10,15):
        schedule.every().day.at(f"{randomTime}:00:00")
    #Evening run
    schedule.every().day.at("17:00:00").do(bill_bot)
    while True:
        schedule.run_pending()
        time.sleep(60)

