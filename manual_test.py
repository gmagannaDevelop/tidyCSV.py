
import random
from tidycsv.utils.customobjs import Path
from tidycsv.core.parsing import get_csv_counts

def random_csv_file() -> Path:
    """get a random csv file from the data directory
    WARNING : Hardcoded"""
    data_dir = Path("/home/gml/Proyects/Personal/tidycsv/data")
    csv_files = data_dir.lglob("*.csv")
    rnd_index = random.randint(0, len(csv_files) - 1)
    return csv_files[rnd_index]


