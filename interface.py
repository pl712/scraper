import time
from scraper import Scraper
from httpserver import RESTful

class Message:
    def __init__(self, id, msgText, msgTime, msgSender, msgQuality, msgPic = None, msgHashTags = None, msgClassificationTags = None):
        self.id = id
        self.msgText = msgText
        self.msgTime = msgTime
        self.msgSender = msgSender
        self.msgQuality = msgQuality
        self.msgPic = msgPic
        self.msgHashTags = msgHashTags
        self.msgClassificationTags = msgClassificationTags

    def getMsg(self):
        return {'text' : self.msgText, 
                'time' : self.msgTime, 
                'sender' : self.msgSender, 
                'quality' : self.msgQuality, # -1 0 1
                'pic' : self.msgPic, 
                'hashTags' : self.msgHashTags, 
                'classificationTags' : self.msgClassificationTags}

class Topic:
    def __init__(self, topicName, startDate = time.time()):
        self.name = topicName
        self.startDate = startDate
        self.lastUpdate = startDate
        self.msgList = {} # tweet id : message object

    def addMsg(self, id, msgObj):
        self.msgList[id] = msgObj
        self.lastUpdate = time.time()
    
    def removeMsg(self, id):
        del self.msgList[id]
        self.lastUpdate = time.time()

class UserAccount:
    def __init__(self, password):
        self.password = password
        self.subList = {} # topic name : topic object
    
    def addSub(self, topicName, topicObj):
        self.subList[topicName] = topicObj
    
    def removeSub(self, topicName):
        del self.subList[topicName]

class Interface:
    def __init__(self):
        self.userList = {} # user name : user object
        self.topicList = {} # topic name : topic object
        
    #login
    def verifyUserLogin(self, userName, password):
        if userName in self.userList:
            if self.userList[userName].password == password:
                return True
        return False

    def addUser(self, userName, password):
        self.userList[userName] = UserAccount(password)
    
    #subscribe
    def userSubscribe(self, userName, topicName):
        self.userList[userName].addSub(topicName, self.topicList[topicName])

    def userUnsubscribe(self, userName, topicName):
        self.userList[userName].removeSub(topicName)

    #topic
    def addTopic(self, topicName):
        self.topicList[topicName] = Topic(topicName)

    #application
    def getUserTopics(self, userName):
        return list(self.userList[userName].subList.keys())

    def getMessagesByTopic(self, topicName):
        lst = []

        for msg in self.topicList[topicName].msgList:
            lst.append(msg.getMsg())
        
        return lst

    def addMessageToTopic(self, topicName, **kwargs):
        newMsg = Message(kwargs['id'], kwargs['msgText'], kwargs['msgTime'], kwargs['msgSender'], kwargs['msgQuality'], kwargs['msgPic'], kwargs['msgHashTags'], kwargs['msgClassificationTags'])
        
        self.topicList[topicName].addMsg(newMsg)

class mainProgram:
    def __init__(self):
        self.program = Interface()
        self.server = RESTful(self.program)
        self.scraper = Scraper(self.program, listOfUsers = ['POTUS'])

    def main(self):
        self.scraper.run()
        self.server.run()
