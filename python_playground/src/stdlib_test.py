#!/usr/bin/env python3

"""
Interesting functions from Python's stdlib
"""

import difflib
import operator
import os.path
import sys
from functools import partial
from textwrap import dedent


def test_rel_path():
    # Thanks to /u/status_quo99 on Reddit
    rel_path = partial(os.path.join, os.path.dirname(__file__))
    f = rel_path("../config/foo.ini")
    expected = os.path.dirname(__file__) + "/../config/foo.ini"
    assert f == expected


def test_print_err(capsys):
    # Thanks to /u/kalgynirae on Reddit
    print_err = partial(print, file=sys.stderr)
    print_err("failed")
    captured = capsys.readouterr()
    assert captured.err == "failed\n"


def test_dedent():
    # Thanks again to /u/kalgynirae on Reddit
    message = dedent(
        """
        This is a reasonably lengthy message:
            * point 1
            * point 2
        And there you have it!
    """
    ).strip()
    assert (
        message
        == """
This is a reasonably lengthy message:
    * point 1
    * point 2
And there you have it!
""".strip()
    )


def test_difflib_close_matches():
    # Thanks to /u/smnslwl on Reddit
    result = difflib.get_close_matches("appel", ["ape", "apple", "peach", "puppy"])
    assert result == ["apple", "ape"]


def test_sorted_operators():
    # Thanks to /u/Dev Jeanpierre on SO
    x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

    # sort on keys
    sorted_keys = sorted(x.items(), key=operator.itemgetter(0))
    assert sorted_keys == [(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)]

    # sort on values
    sorted_values = sorted(x.items(), key=operator.itemgetter(1))
    assert sorted_values == [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]


def chunk_read_binary(filename, chunk_size=4096):
    """Read chunks of a binary file.

    Thanks to /u/totally_the_OP
    http://www.reddit.com/r/Python/comments/34cdfm/what_are_your_favorite_little_tricks/cqtlwv0
    """
    with open(filename, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), ""):
            pass


def cli_select_log_level() -> int:
    """Use repeatable -v and -q to select the logging level.

    Thanks to /u/masklinn

    Example:
        script -vv  -> DEBUG
        script -v   -> INFO
        script      -> WARNING
        script -q   -> ERROR
        script -qq  -> CRITICAL
        script -qqq -> no logging at all
    """
    import argparse
    import logging

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="count", default=0)
    parser.add_argument("-q", "--quiet", action="count", default=0)
    args = parser.parse_args()

    logging_level = logging.WARN + 10 * args.quiet - 10 * args.verbose
    return logging_level


def loading():
    """Draw bars and pipes loading indicators using carriage returns."""
    import time

    while True:
        for char in ["/", "-", "\\", "|", "/", "-", "\\", "|"]:
            print(char, end="\r", flush=True)
            time.sleep(0.1)


def tuple_op(a, b, op):
    """Perform operation on two tuples.

    >>> import operator
    >>> tuple_op((0, 1), (2, 3), operator.add)
    (2, 4)
    >>> tuple_op(1, 2, operator.add)
    Traceback (most recent call last):
        ...
    TypeError: 'int' object is not iterable
    """
    return tuple([op(item1, item2) for item1, item2 in zip(a, b)])
