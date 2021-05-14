#! /usr/bin/env python3
from enum import Enum
from typing import List
from requests import Session
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator
from oref_analyzer.utils import AlertEntry


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

    def __getitem__(self, name: str) -> List[AlertEntry]:
        return [entry for entry in self.history if entry.location == name or name in entry.location]

    def _format_history(self, history: List[AlertEntry]) -> None:
        x_axis = [] # time
        y_axis = [] # total alerts

        counter = 0
        for entry in history:
            x_axis.append(entry.time)
            y_axis.append(counter)
            counter += 1

        return x_axis, y_axis

    @property
    def empty(self):
        return len(self.history) == 0

    def get_history(self, mode: RequestPeriod) -> List[AlertEntry]:
        """
        gets history from the last period
        """

        if not (response := self.get('https://www.oref.org.il//Shared/Ajax/'\
                                     f'GetAlarmsHistory.aspx?lang={self.language}&mode={mode.value}')):
            raise ConnectionError('Failed to send request!')

        return sorted(AlertEntry(entry) for entry in response.json())

    def get_alerts(self) -> List[AlertEntry]:
        """
        gets alerts that are happening right now
        adds them to history
        """
        if not (response := self.get('https://www.oref.org.il/WarningMessages/alert/alerts.json')):
            raise ConnectionError('Failed to send request!')

        response_as_json = response.json()
        alert_time = datetime.utcfromtimestamp(response_as_json['id'] / 1000)
        alerts = [AlertEntry(location, alert_time) for location in response_as_json['data']]

        self.history.extend(alerts)
        self.history = sorted(self.history)

        return alerts

    def show_history(self, location: str = '', start_date: datetime = datetime.utcfromtimestamp(0)):
        history = self[location] if location else self.history
        x_axis, y_axis = self._format_history(entry for entry in history if entry.time > start_date)

        plt.title(f'Red alerts in {location if location else "Israel"}')
        plt.xlabel('Date')
        plt.ylabel('Red alerts')

        plt.gcf().autofmt_xdate()
        plt.plot([start_date] + x_axis, [0] + y_axis)
        plt.gcf().axes[0].xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y %H:%M'))
        plt.gcf().axes[0].yaxis.set_major_locator(MaxNLocator(integer=True))

        plt.show()
