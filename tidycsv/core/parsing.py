"""
    Parsing functions

    All the functions needed to parse an arbitrary
    csv file and find the biggest semantically coherent
    group (set) of lines.

    This maximum set is what we call a "tidy csv",
    implying that the underlying idea of a consistent
    comma-separated observations are present.

    Some programs can "magically" parse poorly specified,
    invalid, and heterogeneous csv files.
    This is not the case for all functions. This set of functions
    aims to be this interface which allows other programs to access
    data from a csv file even when it has been poorly written.

"""

# TODO : review or shorten docstring ?

from pathlib import Path
from typing import Dict, List, Union, Optional
from functools import reduce

__all__ = ["get_csv_counts", "get_maximum_csv_group"]


def get_csv_counts(
    file: Union[str, Path], separator: Optional[str] = None
) -> Dict[int, List[str]]:
    """
    Get groups of semantically consistsent csv lines.
    i.e. same number of commas

    Parameters
    ----------
        file : a string, pathlib.Path to used within a
               call to `open(file, "r") as f`.

        separator: (optional) a string indicating the token
                    that is to be taken as column delimiter.
                    it defaults to ","

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
    _separator: str = separator or ","

    with open(file, "r") as file_reader:
        lines: List[str] = file_reader.readlines()

    csv_counts: Dict[int, List[str]] = {}

    for line in lines:
        n_commas: int = line.count(_separator)
        if n_commas in csv_counts.keys():
            csv_counts[n_commas].append(line)
        else:
            csv_counts.update({n_commas: [line]})

    return csv_counts


def get_maximum_csv_group(csv_counts: Dict[int, List[str]]) -> List[str]:
    """Get the list with the maximum number of
    semantically consistent csv lines, from
    a dictionary of number of lines"""
    return reduce(lambda x, y: x if len(x[1]) > len(y[1]) else y, csv_counts.items())[1]
