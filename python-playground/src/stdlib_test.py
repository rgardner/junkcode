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

