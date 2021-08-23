#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
# pylint: disable=invalid-name

"""Build system entrypoint."""

import argparse
import contextlib

import xtask.fmt
import xtask.lint

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    fmt_parser = subparsers.add_parser("fmt")
    xtask.fmt.add_arguments(fmt_parser)

    lint_parser = subparsers.add_parser("lint")
    xtask.lint.add_arguments(lint_parser)

    with contextlib.suppress(ImportError):
        import argcomplete

        argcomplete.autocomplete(parser)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
