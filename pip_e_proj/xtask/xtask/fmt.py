"""Formatting utilities."""

import argparse
import subprocess

from . import location


def reformat() -> None:
    """Reformats the code."""
    subprocess.run(["black", location.proj_root()], check=True)


def check_formatting() -> None:
    """Checks Python code formatting, raises exception if unformatted code found."""
    subprocess.run(["black", "--check", location.proj_root()], check=True)


def add_arguments(parser: argparse.ArgumentParser):
    """Configures argument parser for formatting functionality."""
    parser.add_argument("-c", "--check", action="store_true", help="Check formatting.")
    parser.set_defaults(func=_fmt_main)


def _fmt_main(args: argparse.Namespace) -> None:
    """Main module entrypoint."""
    if args.check:
        check_formatting()
    else:
        reformat()
