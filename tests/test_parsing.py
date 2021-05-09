from tidycsv.core.parsing import *
from tidycsv.utils.customobjs import Path


def test_get_csv_counts(random_csv_file):
    print(Path(".").abs)
    assert isinstance(get_csv_counts(random_csv_file), dict)