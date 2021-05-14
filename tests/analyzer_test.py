from typing import List
from datetime import datetime
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
    for entry in analyzer.history:
        assert isinstance(entry, AlertEntry)
