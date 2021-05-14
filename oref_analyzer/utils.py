from datetime import datetime


class AlertEntry:
    def __init__(self, *args):
        if len(args) == 1:
            self._from_dict(*args)
        elif len(args) == 2:
            self._from_params(*args)
        else:
            raise TypeError(f'Failed to build {type(self)}')

    def _from_dict(self, entry_json: dict):
        self.time = datetime.strptime(entry_json['datetime'], '%Y-%m-%dT%H:%M:%S')
        self.location = entry_json['data']

    def _from_params(self, location: str, time: datetime):
        self.time = time
        self.location = location

    def __str__(self) -> str:
        return f'Alert at {self.location} at {self.time}'

    def __le__(self, other) -> bool:
        return self.time <= other.time

    def __lt__(self, other) -> bool:
        return self.time < other.time
