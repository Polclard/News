from email import message
from http import client
import tweepy
import requests
import os
from dotenv import load_dotenv
import keep_alive
import time
import urllib.request, json
import re

load_dotenv()


# region FUNCTIONS
def get_whole_link(message):
    try:
        tweet_link = re.search("(?P<url>https?://[^\s]+)",str(message)).group("url")
        tweet_link = requests.get(tweet_link).url
    except AttributeError:
        tweet_link = ""
    return tweet_link


def send_message(TELEGRAM_TOKEN, CHAT_ID, CONTEXT):
    SEND_MESSAGE = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={chat_id}&text={CONTEXT}"
    requests.get((SEND_MESSAGE))


send_once = True
gta1_ID = os.getenv("API_MY_USER")
TELEGRAM_TOKEN = os.getenv("API_TELEGRAM_TOKEN")
bearer_token = os.getenv("API_BEARER_TOKEN")
second_user_token = os.getenv("API_SECOND_USER")


def get_message_id(data):
    data_from_msg['result'][-1]['message']['message_id']


def get_message_from_user(data):
    data_from_msg['result'][-1]['message']['text']


client = tweepy.Client(bearer_token)
tweets = client.get_users_tweets(id=gta1_ID,
                                 exclude="retweets,replies",
                                 max_results=5)

secondsTweets = client.get_users_tweets(id=second_user_token,
                                        exclude="retweets,replies",
                                        max_results=5)

chat_id = os.getenv("CHAT_ID")
messages = tweets.data
second_messages = secondsTweets.data

headers = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'
}

while True:
    for message in messages:

        the_whole_link = get_whole_link(message)
        send_message(TELEGRAM_TOKEN, chat_id, the_whole_link)

        incoming_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
        with urllib.request.urlopen(incoming_url) as incoming_url1:
            data_from_msg = json.load(incoming_url1)

    for message2 in second_messages:
        the_whole_link = get_whole_link(message2)
        send_message(TELEGRAM_TOKEN, chat_id, the_whole_link)
    time.sleep(3600)

keep_alive.keep_alive()
