#! /usr/bin/env python3
from enum import Enum
from oref_analyzer.utils import AlertEntry
from requests import Session
from typing import List


class RequestPeriod(Enum):
    day = 1
    week = 2
    month = 3


class OrefAnalyzer(Session):
    def __init__(self, language: str = 'en', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.language = language
        self.headers = {
            'Host': 'www.oref.org.il',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https//www.oref.org.il//12481-he/Pakar.aspx',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache'
        }

        self.history = self.get_history(RequestPeriod.month)

    @property
    def empty(self):
        return len(self.history) == 0

    def get_history(self, mode: RequestPeriod) -> List:
        if not (response := self.get('https://www.oref.org.il//Shared/Ajax/'\
                                     f'GetAlarmsHistory.aspx?lang={self.language}&mode={mode.value}')):
            raise ConnectionError('Failed to send request!')

        return [AlertEntry(entry) for entry in response.json()]
