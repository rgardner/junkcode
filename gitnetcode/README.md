# gitnetcode

Processes `git log --pretty=tformat: --shortstat` output to get total number of
lines of code added/removed. See [gitnetcode.py](gitnetcode.py) for usage and
examples.

## Tests

```shell
pip install --user pytest
pytest gitnetcode_test.py
```
