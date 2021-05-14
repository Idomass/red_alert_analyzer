import json
import pytest
from pytest_mock import MockerFixture
from oref_analyzer import OrefAnalyzer, AlertEntry


class HistoryResponseMock:
	def json(self):
		with open('tests/history.json', 'r') as src:
			return json.load(src)

class AlertsResponseMock:
    def json(self):
        with open('tests/alerts.json', 'r') as src:
            return json.load(src)


def assert_sorted(analyzer: OrefAnalyzer):
	assert all(analyzer.history[i] <= analyzer.history[i+1] for i in range(len(analyzer.history)-1))

@pytest.fixture()
def entry_json():
    return {
		"data": "Eitan",
		"date": "14.05.2021",
		"time": "13:56",
		"datetime": "2021-05-14T13:56:00"
	}


@pytest.fixture()
def entry(entry_json):
    return AlertEntry(entry_json)


@pytest.fixture()
def analyzer(mocker: MockerFixture):
	mocker.patch.object(OrefAnalyzer, 'get', return_value=HistoryResponseMock())
	return OrefAnalyzer()


@pytest.fixture()
def alerts_mock_analyzer(mocker: MockerFixture, analyzer: OrefAnalyzer):
	mocker.patch.object(OrefAnalyzer, 'get', return_value=AlertsResponseMock())
	return analyzer
