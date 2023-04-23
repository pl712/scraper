import openai
import pandas as pd

api_key = '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'


'''
from categorize import getSinglePrediction
getSinglePrediction(api_key, 'This is a test tweet') -> string of category
getListPrediction(api_key, ['This is a test tweet', 'This is another test tweet']) -> list of categories
'''

def getSinglePrediction(apiKey, content:str) -> str:
  openai.api_key = apiKey

  lstOfCategories = ['web3 activities and events', 'web3 announcements', 'web3 research output', 'web3 meme', 'crypto and markets', 'web3 phishing or irrelevant', 'unknown']

  response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Decide which category the Tweet best classify as {lstOfCategories}.\n\nTweet: \"{content}\"\nCategory: ",
      temperature=0,
      max_tokens=60,
      top_p=1,
      frequency_penalty=0.5,
      presence_penalty=0
    )

  result = response['choices'][0]['text']

  return result[-len(result)+1:]

def getListPrediction(apiKey, contentList:list) -> list:
    openai.api_key = apiKey
    returnLst = []

    lstOfCategories = ['web3 activities and events', 'web3 announcements', 'web3 research output', 'web3 meme', 'crypto and markets', 'web3 phishing or irrelevant', 'unknown']

    for i in contentList:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Decide which category the Tweet best classify as {lstOfCategories}.\n\nTweet: \"{i}\"\nCategory: ",
            temperature=0,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0
        )

        result = response['choices'][0]['text']

        returnLst.append(result[-len(result)+1:])

    return returnLst

def getPredictionDF(apiKey, csv_path, return_path = 'categorized.csv'):
  openai.api_key = apiKey

  lstOfCategories = ['web3 activities and events', 'web3 announcements', 'web3 research output', 'web3 meme', 'crypto and markets', 'web3 phishing or irrelevant', 'unknown']

  currDF = pd.read_csv(csv_path)
  returnDF = pd.DataFrame(columns=['user', 'tweet_content', 'category'])

  for _, row in currDF.iterrows():
    content = row['tweet_content']

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Decide which category the Tweet best classify as {lstOfCategories}.\n\nTweet: \"{content}\"\nCategory: ",
      temperature=0,
      max_tokens=60,
      top_p=1,
      frequency_penalty=0.5,
      presence_penalty=0
    )

    result = response['choices'][0]['text']

    returnDF.loc[len(returnDF)] = {'user': row['user'], 'tweet_content': row['tweet_content'], 'category': result[-len(result)+1:]}

  returnDF.to_csv(return_path, index=False)