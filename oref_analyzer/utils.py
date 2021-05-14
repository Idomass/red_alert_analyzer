from datetime import datetime


class AlertEntry:
    def __init__(self):
        self.time = datetime.now()
        self.location = 'Noder'
