from new_scraper import Scraper
from httpserver import RESTful
from interface import Interface
import threading

class mainProgram:
    def __init__(self):
        self.program = Interface()
        self.server = RESTful(self.program)
        non_web3 = ['elonmusk', 'POTUS', 'BillGates', 'sama', 'zlj517']
        big_orgs = ['paradigm','a16z','sequoia','Stepnofficial','MantaNetwork','okxweb3','binance','kucoincom','cz_binance','twobitidiot']
        projects = ['Nakamigos', 'TheMuppethShow', 'Cat_Mouse_game', 'Ronin_Network', 'ZooDAO']
        research = ['zachxbt', 'jphackworth42', 'drakefjustin', 'BTC__options']
        self.accounts = non_web3 + big_orgs + projects + research
        self.scraper = Scraper(self.program, listOfAccounts = self.accounts)

    def run_scraper(self):
        self.scraper.run()
        self.scraper.save_tweets_to_csv()
    
    def run(self):
        print("Running scraper thread")
        scraper_thread = threading.Thread(target=self.run_scraper)
        scraper_thread.start()

        print("Running Flask server")
        self.server.run()

mainProgram().run()
