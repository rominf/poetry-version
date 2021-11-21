# poetry-version (deprecated)

## What to use instead

Now there is a better way to extract the version of the package.

Assuming your package is named `mypackage`:
```python
import importlib.metadata

__version__ = importlib.metadata.version("mypackage")
```

This code should work as is if you are using Python >= 3.8.

For Python 3.6 and 3.7 you need to install a backport: https://pypi.org/project/importlib-metadata/
