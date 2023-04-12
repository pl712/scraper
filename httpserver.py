from flask import Flask

class RESTful:
    def __init__(self, interfaceObject):
        self.program = interfaceObject

    def run(self):
        app = Flask(__name__)

        @app.route('/register/<userName>/<password>')
        def register(userName, password):
            self.program.addUser(userName, password)
            return "User registered successfully"

        @app.route('/login/<userName>/<password>')
        def login(userName, password):
            if self.program.verifyUserLogin(userName, password):
                return 0
            else:
                return 1

        @app.route('/changeSensitivity/<userName>/<topicName>')
        def changeSensitivity(userName, topicName, sensitivity):
            if topicName in self.program.userList[userName].subList:
                self.program.userChangeSensitivity(userName, topicName, sensitivity)
                return 0
            return 1

        @app.route('/subscribe/<userName>/<topicName>/<sensitivity>')
        def subscribe(userName, topicName, sensitivity):
            if topicName in self.program.topicList:
                if topicName not in self.program.userList[userName].subList:
                    self.program.userSubscribe(userName, topicName, sensitivity)
                    return 0
            return 1

        @app.route('/unsubscribe/<userName>/<topicName>')
        def unsubscribe(userName, topicName):
            if topicName in self.program.userList[userName].subList:
                self.program.userUnsubscribe(userName, topicName)
                return 0
            return 1
        
        @app.route('/getTopics/<userName>')
        def getTopics(userName):
            return self.program.getTopicsByUser(userName)

        @app.route('/getMessages/<topicName>/<sensitivity>')
        def getMessages(topicName, sensitivity):
            return self.program.getMessagesByTopic(topicName, sensitivity)

        app.run(debug=True)
        