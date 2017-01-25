from eventemitter import EventEmitter

class SlackEventAdapter(EventEmitter):
    def __init__(self, verification_token):
        super(EventEmitter, self).__init__()
        self.verification_token = verification_token

    def create_server(self):
        pass
