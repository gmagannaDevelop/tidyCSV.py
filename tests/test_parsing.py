"""
Tests for the parsing module, the core of tidycsv.
"""

from tidycsv.core.parsing import *
from tidycsv.utils.customobjs import Path


def test_get_csv_counts_type(random_csv_file):
    """Assert that for any given csv file, the object returned is a dict."""
    _csv_counts = get_csv_counts(random_csv_file)
    assert isinstance(
        _csv_counts, dict
    ), f"get_csv_counts() returned {type(_csv_counts)}, expected 'dict'"


def test_get_maximum_csv_group(random_csv_file):
    """Verify that parsing.get_maximum_csv_group() does
    indeed return the semantically consistent set containing
    the maximum number of lines."""
    csv_counts = get_csv_counts(random_csv_file)
    _biggest: List[str] = get_maximum_csv_group(csv_counts)
    assert len(_biggest) == max(
        map(len, csv_counts.values())
    ), "get_maximum_csv_group() did not return the csv group with the maximum number of lines."
