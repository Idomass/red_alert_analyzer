from datetime import datetime


class AlertEntry:
    def __init__(self, entry_json: dict):
        self.time = datetime.strptime(entry_json['datetime'], '%Y-%m-%dT%H:%M:%S')
        self.location = entry_json['data']

    def __str__(self) -> str:
        return f'Alert at {self.location} at {self.time}'
