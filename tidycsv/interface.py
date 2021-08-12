"""
    The interface to get tidy CSVs from messy CSVs.
"""

from io import StringIO
from typing import Union, Dict, List, Optional
import pathlib

from .core import parsing as tidyparsing


class TidyCSV:
    """
    A context manager that allows accessing the largest
    (by number of lines) group of coherent csv entries.

    >>> with TidyCSV("my-file.csv") as tidy:
    >>>    x = tidy.readlines()

    Or even better:

    >>> import pandas as pd
    >>> with TidyCSV("my-file.csv") as tidy:
    >>>    x = pd.read_csv(tidy)

    If the separator is not a comma, then it shouldn't be called
    a csv, but anyways here's how to tell that to TidyCSV:

    >>> import pandas as pd
    >>> with TidyCSV("my-file.csv", ";") as tidy:
    >>>    x = pd.read_csv(tidy)

    """

    def __init__(
        self, csv_file: Union[str, pathlib.Path], separator: Optional[str] = None
    ):
        self._csv_file: Union[str, pathlib.Path] = csv_file
        self._separator: str = separator or ","
        self.__csv_groups: Dict[int, List[str]]
        self._max_group: List[str]
        self._tidy_handle: StringIO

    def __repr__(self):
        return f"TidyCSV context manager at {hex(id(self))}"

    def __enter__(self):
        # Get csv sets
        self.__csv_groups = tidyparsing.get_csv_counts(
            self._csv_file, separator=self._separator
        )
        # Select the largest
        self._max_group = tidyparsing.get_maximum_csv_group(self.__csv_groups)
        # Create a handle joining the lines contained in the largest group
        self._tidy_handle = StringIO("".join(self._max_group))
        return self._tidy_handle

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._tidy_handle.close()
