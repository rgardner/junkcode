#!/usr/bin/env python3
"""
Interesting functions from Python's stdlib

"""

import difflib
from functools import partial
import os.path
import operator
from textwrap import dedent

def main():
    # Thanks to /u/status_quo99 on Reddit
    rel_path = partial(os.path.join, os.path.dirname(__file__))
    f = rel_path('../config/foo.ini')

    # Thanks to /u/kalgynirae on Reddit
    print_err = partial(print, file=sys.stderr)

    # Thanks again to /u/kalgynirae on Reddit
    message = dedent("""
        This is a reasonably lengthy message:
            * point 1
            * point 2
        And there you have it!
    """).strip()

    # Thanks to /u/smnslwl on Reddit
    difflib.get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])

    # Thanks to /u/Dev Jeanpierre on SO
    x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    # sort on values
    sorted_x = sorted(x.items(), key=operator.itemgetter(1))
    # sort on keys
    sorted_x = sorted(x.items(), key=operator.itemgetter(0))
