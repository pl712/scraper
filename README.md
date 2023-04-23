# Filtered Twitter

DEMO Video Link: https://drive.google.com/file/d/1v3NmrgSW0Pj6dVYo32JZOhJeB70g3dpT/view

## Project Description
Our team was inspired to develop the Crypto News Aggregator because we noticed that researching cryptocurrency news using Twitter can be challenging due to the abundance of information and lack of efficient search functionality. We saw an opportunity to create a tool that filters Twitter messages into different categories based on their relevance to cryptocurrency news and research. This way, users can quickly and easily find the information they need without having to sift through irrelevant content.

## How to run the Twitter scraper and chatGPT labeling

1. Clone the repository.
2. Change into the project root directory.
3. Create a python environment and install dependencies: 
```
pip install -r requirements.txt
```
4. Create an .env file with the following variables. This requires a twitter developer account and an openai API key.
```
CONSUMER_KEY= <your twitter consumer key>
CONSUMER_SECRET= <your twitter consumer secret>
ACCESS_TOKEN= <your twitter access token>
ACCESS_TOKEN_SECRET= <your twitter access token secret>
OPENAI_API_KEY = <your openai api key>
```

5. To run the twitter scraper and real-time labeling by chatGPT API, run the following command

```
python main.py
```
6. This command will start the scraper and fetch the recent tweets from a few selected accounts related to crypto. In this version, we selected the following accounts:

```
        non_web3 = ['elonmusk', 'POTUS', 'BillGates', 'sama', 'zlj517']
        big_orgs = ['paradigm','a16z','sequoia','Stepnofficial','MantaNetwork',
                    'okxweb3','binance','kucoincom','cz_binance','twobitidiot']
        projects = ['Nakamigos', 'TheMuppethShow', 'Cat_Mouse_game', 'Ronin_Network', 'ZooDAO']
        research = ['zachxbt', 'jphackworth42', 'drakefjustin', 'BTC__options']
```

7. For each tweet it fetches, it will call the openai ChatGPT API to label the tweets among seven categories
```
['web3 activities and events', 'web3 announcements', 'web3 research output', 'web3 meme', 'crypto and markets', 'web3 phishing or irrelevant', 'unknown']
```
8. The results is saved in JSON files for frontend rendering.




## How to start the frontend app
1. Change into the frontend directory
```
cd frontend
```
2. Install frontend dependencies
```
npm install
```
3. Start the frontend app
```
npm start
```
4. The frontend app will be running on http://localhost:3000/ by default.