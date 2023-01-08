from scraper import Scraper
from httpserver import RESTful
from interface import Interface

class mainProgram:
    def __init__(self):
        self.program = Interface()
        self.server = RESTful(self.program)
        self.scraper = Scraper(self.program, listOfAccounts = ['POTUS'])

    def run(self):
        self.server.run()
        self.scraper.run()

mainProgram().run()
