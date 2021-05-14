import json
from typing import List
from datetime import datetime
from pytest_mock import MockerFixture
from oref_analyzer import OrefAnalyzer, AlertEntry, RequestPeriod



class AlertsResponseMock:
    def json(self):
        with open('tests/alerts.json', 'r') as src:
            return json.load(src)

def test_entry_creation(entry: AlertEntry):
    assert isinstance(entry.time, datetime)
    assert isinstance(entry.location, str)


def test_analyzer_creation(analyzer: OrefAnalyzer):
    assert isinstance(analyzer.history, List)

    if not len(analyzer.history):
        assert analyzer.empty

def test_get_history(analyzer: OrefAnalyzer):
    history = analyzer.get_history(RequestPeriod.month)

    assert not analyzer.empty
    for entry in history:
        assert isinstance(entry, AlertEntry)

def test_get_current_alerts(mocker: MockerFixture, analyzer: OrefAnalyzer):
    mocker.patch.object(OrefAnalyzer, 'get', return_value=AlertsResponseMock())
    alerts = analyzer.get_alerts()

    assert not analyzer.empty
    for alert in alerts:
        assert isinstance(alert, AlertEntry)
