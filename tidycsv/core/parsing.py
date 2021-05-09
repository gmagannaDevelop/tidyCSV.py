from pathlib import Path
from typing import Dict, List
from functools import reduce


def get_csv_counts(file: Path):
    """ """
    with open(file.absolute().as_posix(), "r") as f:
        lines = f.readlines()

    csv_counts: Dict[int, List[str]] = {}

    for line in lines:
        n_commas = line.count(",")
        if n_commas in csv_counts.keys():
            csv_counts[n_commas].append(line)
        else:
            csv_counts.update({n_commas: [line]})

    return csv_counts

    # return reduce(lambda x, y: x if len(x[1]) > len(y[1]) else y, csv_counts.items())
