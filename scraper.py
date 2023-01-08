import requests, json, time
from interface import Message

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
        self.bearerToken = 'AAAAAAAAAAAAAAAAAAAAAP7kkgEAAAAAsZY0lU3iSaGHru7XeYR8xhOm06g%3DVt7K6GWzH0mAZfSMsdyTpqKIRw0QobOaB5YIaLRcz7QAUSdeoh'

        self.lastTweet = {i : None for i in self.listOfAccounts}
        self.cat = categorizer()

    def getTweet(self, accountName, maxResults = 20):
        endpoint_url = "https://api.twitter.com/2/tweets/search/recent"
        headers = {"Authorization": f"Bearer {self.bearerToken}"}

        payload = {
            "query": f"from:{accountName}",
            "max_results": str(maxResults),
            "tweet.fields": "created_at,entities,public_metrics,context_annotations",
            "since_id": str(self.lastTweet[accountName])
        } if self.lastTweet[accountName] != None else {
            "query": f"from:{accountName}",
            "max_results": str(maxResults),
            "tweet.fields": "created_at,entities,public_metrics,context_annotations"
        }

        response = json.loads(requests.request("GET", endpoint_url, headers=headers, params=payload).text)

        try:
            if response['meta']['result_count'] == 0:
                print (f'No new tweets since last check for {accountName} at t = {time.time()}, last tweet id: {self.lastTweet[accountName]}')
                return []
            
            self.lastTweet[accountName] = response['meta']['newest_id']

            return response['data']
        except:
            return response

    def run(self):
        while True:
            for account in self.listOfAccounts:
                tweets = self.getTweet(account)
                
                if tweets != []:
                    for tweet in tweets:

                        imgList, hashList = [], []

                        if 'entities' in tweet: #media links and hashtags
                            
                            if 'urls' in tweet['entities']:
                                for i in tweet['entities']['urls']:
                                    imgList.append(i['url'])

                            if 'hashtags' in tweet['entities']:
                                for i in tweet['entities']['hashtags']:
                                    hashList.append(i['tag'])
                        
                        currMsg = Message(tweet['id'], tweet['text'], tweet['created_at'], tweet['public_metrics'], account, msgMedia=imgList, msgHashTags=hashList)

                        if 'context_annotations' in tweet: # classification tags
                            currMsg.msgClassificationTags = tweet['context_annotations']

                        currMsg.msgQuality = self.cat.setQuality(currMsg) #filtering - getting quality

                        self.program.addMessageToTopic(self.cat.setCategory(currMsg), currMsg)

            # for i in self.program.topicList['general-topic'].msgList: #-> Yes it works
            #     print (self.program.topicList['general-topic'].msgList[i].getMsg())
            #     print ("\n")

            time.sleep(300) #runs every 5 minutes