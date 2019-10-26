# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['poetry_version']

package_data = \
{'': ['*']}

install_requires = \
['tomlkit>=0.4.6,<0.6.0']

setup_kwargs = {
    'name': 'poetry-version',
    'version': '0.1.5',
    'description': 'Python library for extracting version from poetry pyproject.toml file',
    'long_description': '# poetry-version\nPython library for extracting version from poetry pyproject.toml file\n\n## Installation\nTo install `poetry-version` from [PyPI](https://pypi.org/project/poetry-version/) run:\n```shell\n$ pip install poetry-version\n```\n\n## Usage\nPut these lines somewhere in the main module:\n```python\nimport poetry_version\n\n__version__ = poetry_version.extract(source_file=__file__)\n```\n',
    'author': 'Roman Inflianskas',
    'author_email': 'infroma@gmail.com',
    'url': 'https://github.com/rominf/poetry-version',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
}


setup(**setup_kwargs)
