from tidycsv.core.parsing import *
from tidycsv.utils.customobjs import Path


def test_get_csv_counts_type(random_csv_file):
    """Assert that for any given csv file, the object returned is a dict."""
    assert isinstance(get_csv_counts(random_csv_file), dict)
