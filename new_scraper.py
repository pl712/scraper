from interface import Message
from dotenv import load_dotenv
import csv 
import os
import tweepy
import collections

class Scraper:
    def __init__(self, interfaceObject, listOfAccounts):
        self.program = interfaceObject
        self.listOfAccounts = listOfAccounts
        load_dotenv()
        # Set your API keys and tokens
        consumer_key = os.environ.get("CONSUMER_KEY")
        consumer_secret = os.environ.get("CONSUMER_SECRET")
        access_token = os.environ.get("ACCESS_TOKEN")
        access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
        print(consumer_key, consumer_secret, access_token, access_token_secret)
        # Authenticate with the Twitter API
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        # Create a Tweepy API object
        self.api = tweepy.API(auth, timeout=120)
        # Store the tweets in a dictionary - user : [tweets]
        self.user_tweets = collections.defaultdict(list)

    def run(self):
        print("Scraper running")
        for account in self.listOfAccounts:
            user_timeline = self.api.user_timeline(screen_name=account, count=20, tweet_mode='extended')
            for tweet in user_timeline:
                if hasattr(tweet, 'retweeted_status'):
                    # If it's a retweet, store the retweeted_status object instead
                    self.user_tweets[account].append(tweet.retweeted_status)
                else:
                    self.user_tweets[account].append(tweet)
    
    def save_tweets_to_csv(self):
        with open(f'tweets/tweets_web3_big_figures.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['user','tweet_content'])
            for account in self.user_tweets:
                for tweet in self.user_tweets[account]:
                    writer.writerow([account, tweet.full_text])


