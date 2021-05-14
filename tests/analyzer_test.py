from typing import List
from oref_analyzer import OrefAnalyzer, AlertEntry
from datetime import datetime
from typing import List


def test_entry_creation(entry: AlertEntry):
    assert isinstance(entry.time, datetime)
    assert isinstance(entry.location, str)


def test_analyzer_creation(analyzer: OrefAnalyzer):
    assert isinstance(analyzer.history, List)

    if len(analyzer.history):
        for entry in analyzer.history:
            assert isinstance(entry, AlertEntry)
    else:
        assert analyzer.empty
