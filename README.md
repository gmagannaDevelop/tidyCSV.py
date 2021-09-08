# tidyCSV.py

[![CI build](https://github.com/gmagannaDevelop/tidyCSV.py/actions/workflows/main.yml/badge.svg)](https://github.com/gmagannaDevelop/tidyCSV.py/actions/workflows/main.yml)
[![mypy](https://github.com/gmagannaDevelop/tidyCSV.py/actions/workflows/mypy.yml/badge.svg)](https://github.com/gmagannaDevelop/tidyCSV.py/actions/workflows/mypy.yml)
[![tests](https://github.com/gmagannaDevelop/tidyCSV.py/actions/workflows/tests.yml/badge.svg)](https://github.com/gmagannaDevelop/tidyCSV.py/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/gmagannaDevelop/tidyCSV.py/branch/main/graph/badge.svg?token=H1H5RHHI9O)](https://codecov.io/gh/gmagannaDevelop/tidyCSV.py)
![](https://enlyvfs9zh2z4g7.m.pipedream.net)

![](https://img.shields.io/github/last-commit/gmagannaDevelop/tidyCSV.py)
<a href="https://github.com/psf/black">
	<img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
</a>
<a href="https://github.com/gmagannaDevelop/tidyCSV.py/blob/main/LICENSE">
	<img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg">
</a>
<a href="https://lifecycle.r-lib.org/articles/stages.html">
	<img alt="experimental" src="https://img.shields.io/badge/lifecycle-experimental-orange"> 
 </a>

<!-- Additions from black are the lincese and code style badges -->

Tired of having pseudo CSV files full of invalid entries ? Me too, this is my solution.



It has probably occurred to you as it has to me to get this error 
when reading a csv into Python using [pandas](https://pandas.pydata.org/).

```python
ParserError: Error tokenizing data. C error: Expected 8 fields in line 7, saw 47
```

This happens because some lines in your
file have more columns than you have
 in the header, or simply other kind of inconsistencies such as intermediate blank lines or lines containing random tokens.

Fear no more because _tidyCSV_ provides a simple and clear interface to access
the semantically coherent chunks of your csv file (if there are any). By default it selects the biggest group found (that is the one containing the most lines).

Maybe I'll add an option to select how many columns you expect, in order to filter the groups according to a preconceived criteria. 
Eventually I would like this project to become a command line tool as well as having a richer set of features, but It currently serves its purpose so it is not a priority.

## Installation

The package has been published to PyPI! You can install it as any other package using **pip** (I recommend installing it 
within a virtual environment created in a per project basis).
```bash
pip install tidycsv
```

Otherwise you can install the latest development version using:

```bash
pip install git+https://github.com/gmagannaDevelop/tidyCSV.py
```

## Usage

Use the context manager provided at top-level 
to read an otherwise unreadable csv as follows:

```python
import pandas as pd
from tidycsv import TidyCSV as tidycsv

with tidycsv("your-messy-csv-file.csv") as tidy:
	df = pd.read_csv(tidy)

```

Now you have a dataframe ready to be used instead of an Exception.

## Bugs and feature requests

If you find that _tidyCSV_ is not behaving as you would expect it to, please feel free to open an issue. The same goes for feature requests.
