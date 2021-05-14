import json
from typing import List
from datetime import datetime
from tests.conftest import assert_sorted
from oref_analyzer import OrefAnalyzer, AlertEntry, RequestPeriod


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


def test_get_current_alerts(alerts_mock_analyzer: OrefAnalyzer):
    alerts = alerts_mock_analyzer.get_alerts()

    assert not alerts_mock_analyzer.empty
    for alert in alerts:
        assert isinstance(alert, AlertEntry)


def test_history_sorted_by_date(analyzer: OrefAnalyzer):
    assert_sorted(analyzer)


def test_history_sorted_by_date_after_getting_alerts(alerts_mock_analyzer: OrefAnalyzer):
    alerts_mock_analyzer.get_alerts()
    assert_sorted(alerts_mock_analyzer)


def test_get_location_history(analyzer: OrefAnalyzer):
    assert analyzer['Nachal Oz']


def test_get_non_existant_location_history(analyzer: OrefAnalyzer):
    assert not analyzer['Ness Ziona']


def test_location_history_sorted(analyzer: OrefAnalyzer):
    location_history = analyzer['Nachal Oz']
    assert_sorted(analyzer)
