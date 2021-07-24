import random
from tidycsv.utils.customobjs import Path
import pytest

from typing import List

_ROOT_DIR: Path = Path(__file__).parent.absolute().parent.absolute()
_DATA_DIR: Path = _ROOT_DIR.joinpath("data")


@pytest.fixture
def random_csv_file() -> Path:
    """get a random csv file from the data directory"""
    data_dir: Path = _DATA_DIR
    csv_files: List[Path] = data_dir.lglob("*.csv")
    rnd_index: int = random.randint(0, len(csv_files) - 1)
    return csv_files[rnd_index]
