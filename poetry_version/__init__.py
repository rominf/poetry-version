#!/usr/bin/env python

from pathlib import Path

import tomlkit


def extract(source_file):
    d = Path(source_file)
    result = None
    while d.parent != d and result is None:
        d = d.parent
        pyproject_toml_path = d / 'pyproject.toml'
        if pyproject_toml_path.exists():
            with open(file=str(pyproject_toml_path)) as f:
                pyproject_toml = tomlkit.parse(string=f.read())
                if 'tool' in pyproject_toml and 'poetry' in pyproject_toml['tool']:
                    # noinspection PyUnresolvedReferences
                    result = pyproject_toml['tool']['poetry']['version']
    return result


if __name__ == '__main__':
    print(extract(__file__))
