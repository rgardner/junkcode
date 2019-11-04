import os.path
from pathlib import Path

from invoke import task


def get_source_dir() -> Path:
    return Path(os.path.dirname(os.path.abspath(__file__)))


@task
def setup(c):
    with c.cd(str(get_source_dir())):
        c.run("pipenv install --dev")


@task
def run(c, bin):
    with c.cd(str(get_source_dir())):
        c.run(f"pipenv run python {bin}")


@task
def test(c):
    with c.cd(str(get_source_dir())):
        c.run("pipenv run pytest --cov --doctest-modules")


@task
def format(c):
    with c.cd(str(get_source_dir())):
        c.run("pipenv run black --target-version py37 .")
        c.run("pipenv run isort --apply")


@task
def lint(c):
    with c.cd(str(get_source_dir())):
        c.run("pipenv run flake8")
        c.run("pipenv run mypy")
