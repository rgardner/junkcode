#!/usr/bin/env python3

import os.path
from pathlib import Path
from typing import List

from invoke import task


def get_source_dir() -> Path:
    return Path(os.path.dirname(os.path.abspath(__file__)))


def run_pipenv_commands(c, commands: List[str]):
    with c.cd(str(get_source_dir())):
        for command in commands:
            full_command = f"python3 -m pipenv {command}"
            c.run(full_command, env={"PIPENV_IGNORE_VIRTUALENVS": "1"})


@task
def setup(c):
    run_pipenv_commands(
        c,
        ["install --dev", """run python -c 'import nltk; nltk.download("wordnet")'"""],
    )


@task
def run(c, bin):
    run_pipenv_commands(c, [f"run python {bin}"])


@task
def test(c):
    run_pipenv_commands(c, ["run pytest --cov --doctest-modules"])


@task
def format(c):
    run_pipenv_commands(c, ["run black --target-version py37 .", "run isort --apply"])


@task
def lint(c):
    run_pipenv_commands(c, ["run flake8", "run mypy"])
