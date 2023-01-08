APIkey = 'MqSnfNuYNaCRHIfE0gbawImfZ'
APISec = 'P1lPeFnkupNBzSPmXiWTtSbdbxHhcZQQSeJcqFdYt3Qmfwk9et'
Accesskey = '1464807135771045890-IvWaECfLmuP2dqQpkJJYAcusXfkCI1'
AccessSec = '3rfX4cq8ha3tFRBqfHpCWzg6EX7Ergj4P8OfBZW6kWgxJ'

import requests, json

class Scraper:
        
    def __init__(self, interfaceObject, listOfAccounts):
        self.program = interfaceObject
        self.bearer_token = 'AAAAAAAAAAAAAAAAAAAAAP7kkgEAAAAAsZY0lU3iSaGHru7XeYR8xhOm06g%3DVt7K6GWzH0mAZfSMsdyTpqKIRw0QobOaB5YIaLRcz7QAUSdeoh'
        self.listOfAccounts = listOfAccounts
        self.header = {"Authorization": f"Bearer {self.bearer_token}"}

    

    


class categorizer:
    def __init__(self):
        pass
    
    def setCategory(self, data):
        return 1


