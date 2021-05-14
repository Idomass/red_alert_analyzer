import pytest

from oref_analyzer import OrefAnalyzer, AlertEntry


@pytest.fixture()
def entry():
    return AlertEntry()

@pytest.fixture()
def analyzer():
    return OrefAnalyzer()
