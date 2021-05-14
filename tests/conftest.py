import pytest

from oref_analyzer import OrefAnalyzer


@pytest.fixture()
def analyzer():
    return OrefAnalyzer()
