import time

class Message:
    def __init__(self, id, msgText, msgTime, msgStats, msgSender, msgQuality = -2, msgMedia = [], msgHashTags = [], msgClassificationTags = []):
        self.id = id
        self.msgText = msgText
        self.msgTime = msgTime
        self.stats = msgStats
        self.msgSender = msgSender

        self.msgQuality = msgQuality
        self.msgMedia = msgMedia
        self.msgHashTags = msgHashTags
        self.msgClassificationTags = msgClassificationTags

    def getMsg(self):
        return {'text' : self.msgText, 
                'time' : self.msgTime, 
                'sender' : self.msgSender, 
                'stats' : self.stats,
                'quality' : self.msgQuality,
                'media' : self.msgMedia,
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
        self.subList = {} # topic name : topic sensitivity
    
    def addSub(self, topicName, sensitivity = 0):
        self.subList[topicName] = sensitivity
    
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
    def userSubscribe(self, userName, topicName, sensitivity):
        self.userList[userName].addSub(topicName, sensitivity)

    def userChangeSensitivity(self, userName, topicName, sensitivity):
        self.userList[userName].subList[topicName] = sensitivity

    def userUnsubscribe(self, userName, topicName):
        self.userList[userName].removeSub(topicName)

    #topic
    def addTopic(self, topicName):
        self.topicList[topicName] = Topic(topicName)

    #application
    def getUserTopics(self, userName):
        return self.userList[userName].subList

    def getMessagesByTopic(self, topicName, sensitivity):
        lst = []

        for id in self.topicList[topicName].msgList:
            if id.msgQuality >= sensitivity:
                lst.append(self.topicList[topicName].msgList[id].getMsg())
        
        return lst

    def addMessageToTopic(self, topicName, newMsg):  
        if topicName not in self.topicList:
            self.addTopic(topicName)      
        self.topicList[topicName].addMsg(newMsg.id, newMsg)

