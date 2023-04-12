import requests, json, time
from interface import Message
from requests.structures import CaseInsensitiveDict
from dotenv import load_dotenv
import csv 
import os

class categorizer:
    def __init__(self):
        pass
    
    def setCategory(self, msg):
        return "general-topic"
    
    def setQuality(self, msg):
        return 0


class Scraper:
    def __init__(self, interfaceObject, listOfAccounts):
        self.program = interfaceObject
        self.listOfAccounts = listOfAccounts
        load_dotenv()
        # Add your bearer token in the .env file
        self.bearerToken = os.environ.get("TWITTER_BEARER_TOKEN")
        self.lastTweet = {i: None for i in self.listOfAccounts}
        self.cat = categorizer()

    def bearer_oauth(self, r):

        r.headers["Authorization"] = f"Bearer {self.bearerToken}"
        r.headers["User-Agent"] = "v2RecentSearchPython"
        return r
    
    def getTweet(self, accountName, maxResults=10):
        endpoint_url = "https://api.twitter.com/2/tweets/search/recent"
        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {self.bearerToken}"

        payload = {
            "query": f"from:{accountName}",
            "max_results": str(maxResults),
            "tweet.fields": "created_at,entities,public_metrics,context_annotations",
            "since_id": str(self.lastTweet[accountName]),
        } if self.lastTweet[accountName] is not None else {
            "query": f"from:{accountName}",
            "max_results": str(maxResults),
            "tweet.fields": "created_at,entities,public_metrics,context_annotations",
        }

        # response = requests.get(endpoint_url, auth=self.bearer_oauth, params=payload)
        response = requests.get(endpoint_url, headers=headers, params=payload)
        data = response.json()

        if response.status_code != 200:
            print(f"Error: {data}")
            return []

        if data['meta']['result_count'] == 0:
            print(f'No new tweets since last check for {accountName} at t = {time.time()}, last tweet id: {self.lastTweet[accountName]}')
            return []

        self.lastTweet[accountName] = data['meta']['newest_id']
        print(data['data'])
        return data['data']
        

    def saveTweet(self, tweet):
        import csv

# def saveTweet(self, tweet):
#     with open('tweets.csv', mode='a', newline='', encoding='utf-8') as csvfile:
#         fieldnames = ['id', 'text', 'created_at', 'public_metrics', 'account', 'msg_media', 'msg_hashtags', 'msg_classification_tags', 'msg_quality']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         if csvfile.tell() == 0:
#             writer.writeheader()

#         writer.writerow({
#             'id': tweet['id'],
#             'text': tweet['text'],
#             'created_at': tweet['created_at'],
#             'public_metrics': str(tweet['public_metrics']),
#             'account': account,
#             'msg_media': ','.join(imgList),
#             'msg_hashtags': ','.join(hashList),
#             'msg_classification_tags': str(tweet.get('context_annotations', '')),
#             'msg_quality': self.cat.setQuality(currMsg)
#         })


    def run(self):
        print("Scraper running")
        while True:
            for account in self.listOfAccounts:
                tweets = self.getTweet(account)
                print("tweets:", tweets)
                if tweets != []:
                    for tweet in tweets:
                        print("tweets:", tweet)
                        imgList, hashList = [], []

                        if 'entities' in tweet: #media links and hashtags
                            
                            if 'urls' in tweet['entities']:
                                for i in tweet['entities']['urls']:
                                    imgList.append(i['url'])

                            if 'hashtags' in tweet['entities']:
                                for i in tweet['entities']['hashtags']:
                                    hashList.append(i['tag'])
                        
                        currMsg = Message(tweet['id'], tweet['text'], tweet['created_at'], tweet['public_metrics'], account, msgMedia=imgList, msgHashTags=hashList)
                        print(currMsg)
                        if 'context_annotations' in tweet: # classification tags
                            currMsg.msgClassificationTags = tweet['context_annotations']

                        currMsg.msgQuality = self.cat.setQuality(currMsg) #filtering - getting quality

                        self.program.addMessageToTopic(self.cat.setCategory(currMsg), currMsg)

            # for i in self.program.topicList['general-topic'].msgList: #-> Yes it works
            #     print (self.program.topicList['general-topic'].msgList[i].getMsg())
            #     print ("\n")

            time.sleep(5) #runs every 5 minutes