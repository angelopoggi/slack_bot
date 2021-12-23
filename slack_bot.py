import slack
from config import SLACK_TOKEN
import datetime
import time
import random
import dad_jokes
import schedule


def bill_bot(random=False):
    currentTime = datetime.datetime.now()
    client = slack.WebClient(token=SLACK_TOKEN)
    if currentTime.hour == 9:
        client.chat_postMessage(channel='#provisioninginternal', text="Morning Everyone!")
    if currentTime.hour == 16:
        client.chat_postMessage(channel='#provisioninginternal', text="Night Everyone!")
        
def random_num_gen():
    randomTime = random.randrange(9, 15, 1)
    return randomTime
if __name__== '__main__':
    #Morning run
    schedule.every().day.at("09:00:00").do(bill_bot)
    #Evening run
    schedule.every().day.at("17:00:00").do(bill_bot)
    while True:
        schedule.run_pending()
        time.sleep(60)

