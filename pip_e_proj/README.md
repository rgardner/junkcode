# Editable Pip Project

```sh
$ pip install -e 'xtask[dev,lint]'
$ ./x.py --help
usage: x.py [-h] {fmt,lint} ...

positional arguments:
  {fmt,lint}

optional arguments:
  -h, --help  show this help message and exit
```

Comparison with `sys.path` changes for importing local scripts:

- Pro, better IDE completions b/c installed in virtualenv. Otherwise
  need to mess with `PYTHONPATH`
- Pro, easier to refactor b/c paths don't need to be changed. And no
  more root counting!
- Con, bootstrap issue (can be solved by docs)
