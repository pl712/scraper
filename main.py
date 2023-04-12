from scraper import Scraper
from httpserver import RESTful
from interface import Interface
import threading

class mainProgram:
    def __init__(self):
        self.program = Interface()
        self.server = RESTful(self.program)
        self.scraper = Scraper(self.program, listOfAccounts = ['POTUS'])

    def run_scraper(self):
        self.scraper.run()
    
    def run(self):
        print("Running scraper thread")
        scraper_thread = threading.Thread(target=self.run_scraper)
        scraper_thread.start()

        print("Running Flask server")
        self.server.run()

mainProgram().run()
