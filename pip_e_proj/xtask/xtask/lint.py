"""Linting utilities."""

import argparse
import contextlib
import subprocess

with contextlib.suppress(ImportError):
    import pylint.lint

from . import location

PACKAGE_NAME = "xtask"
MAIN_SCRIPT = "x"


def lint_mypy() -> None:
    """Checks Python types, raising exception if issues found."""
    subprocess.run(["mypy"], check=True, cwd=location.proj_root() / PACKAGE_NAME)


def lint_pylint() -> None:
    """Lints Python files, raising exception if issues found."""
    proj_root = location.proj_root()
    pylint.lint.Run(
        [str(proj_root / MAIN_SCRIPT), str(proj_root / PACKAGE_NAME / PACKAGE_NAME)]
    )


def add_arguments(parser: argparse.ArgumentParser):
    """Configures argument parser for formatting functionality."""
    parser.set_defaults(func=_lint_main)


def _lint_main(_args: argparse.Namespace) -> None:
    """Main module entrypoint."""
    lint_mypy()
    lint_pylint()
