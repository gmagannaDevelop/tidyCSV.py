"""
"""

from io import StringIO
from pathlib import Path
from typing import Dict, List, Union
from functools import reduce

__all__ = ["get_csv_counts"]


def get_csv_counts(file: Union[str, Path]) -> Dict[int, List[str]]:
    """
    Get groups of semantically consistsent

    Parameters
    ----------
        file : a string, pathlib.Path to used within a
               call to `open(file, "r") as f`.

    Returns
    -------
        A dictionnary containing the number of commas as keys
        and the lines which have said number of commas.
        i.e.

            {
                3: [
                    "x1,x2,x3",
                    "11,21,31",
                    "12,22,33",
                ],
                2: [
                    "extrainfo,date",
                    "none,2020-05-05"
                ]
            }
    """
    with open(file, "r") as f:
        lines: List[str] = f.readlines()

    csv_counts: Dict[int, List[str]] = {}

    for line in lines:
        n_commas: int = line.count(",")
        if n_commas in csv_counts.keys():
            csv_counts[n_commas].append(line)
        else:
            csv_counts.update({n_commas: [line]})

    return csv_counts


def get_biggest_():
    pass
    # return reduce(lambda x, y: x if len(x[1]) > len(y[1]) else y, csv_counts.items())
