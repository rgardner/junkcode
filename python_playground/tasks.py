#!/usr/bin/env python3

import importlib
import os.path
from pathlib import Path
import sys
from typing import List

from invoke import task

sys.path.insert(
    1, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools", "build")
)
from buildlib import TaskError


def get_source_dir() -> Path:
    return Path(os.path.dirname(os.path.abspath(__file__)))


def does_python_module_exist(module: str):
    return importlib.util.find_spec(module) is not None


def run_pipenv_commands(c, commands: List[str]):
    with c.cd(str(get_source_dir())):
        for command in commands:
            full_command = f"python3 -m pipenv {command}"
            c.run(full_command, env={"PIPENV_IGNORE_VIRTUALENVS": "1"})


@task
def setup(c):
    if not does_python_module_exist("pipenv"):
        c.run("python3 -m pip install pipenv")

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
