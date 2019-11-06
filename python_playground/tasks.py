import os.path
from pathlib import Path

from invoke import task


def get_source_dir() -> Path:
    return Path(os.path.dirname(os.path.abspath(__file__)))


@task
def setup(c):
    with c.cd(str(get_source_dir())):
        c.run("python3 -m pipenv install --dev")


@task
def run(c, bin):
    with c.cd(str(get_source_dir())):
        c.run(f"python3 -m pipenv run python {bin}")


@task
def test(c):
    with c.cd(str(get_source_dir())):
        c.run("python3 -m pipenv run pytest --cov --doctest-modules")


@task
def format(c):
    with c.cd(str(get_source_dir())):
        c.run("python3 -m pipenv run black --target-version py37 .")
        c.run("python3 -m pipenv run isort --apply")


@task
def lint(c):
    with c.cd(str(get_source_dir())):
        c.run("python3 -m pipenv run flake8")
        c.run("python3 -m pipenv run mypy")
