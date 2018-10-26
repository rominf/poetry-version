# poetry-version
Python library for extracting version from poetry pyproject.toml file

## Installation
To install `poetry-version` from [PyPI](https://pypi.org/project/poetry-version/) run:
```shell
$ pip install poetry-version
```

## Usage
Put these lines somewhere in the main module:
```python
import poetry_version

__version__ = poetry_version.extract(source_file=__file__)
```
