#! /usr/bin/env python3
from enum import Enum
from requests import Session
from typing import List


class RequestPeriod(Enum):
    day = 1
    week = 2
    month = 3


class OrefAnalyzer(Session):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.history = self.get_history(RequestPeriod.month)

    @property
    def empty(self):
        return len(self.history) == 0


    def get_history(self, mode: RequestPeriod) -> List:
        return []
