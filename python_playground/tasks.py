import os.path
from pathlib import Path

from invoke import task


def get_source_dir() -> Path:
    return Path(os.path.dirname(os.path.abspath(__file__)))


@task
def setup(c):
    with c.cd(str(get_source_dir())):
        c.run("pip install pipenv==2020.6.2")
        c.run("pipenv install --dev")
        c.run("""pipenv run python -c 'import nltk; nltk.download("wordnet")'""")


@task
def run(c, bin):
    with c.cd(str(get_source_dir())):
        c.run(f"pipenv run python {bin}")


@task
def test(c):
    with c.cd(str(get_source_dir())):
        c.run("pipenv run pytest --cov --doctest-modules")


@task
def fmt(c, check=False):
    with c.cd(str(get_source_dir())):
        black_args = ["pipenv", "run", "black", "--target-version", "py38", "."]
        if check:
            black_args.append("--check")
        c.run(" ".join(black_args))

        isort_args = ["pipenv", "run", "isort"]
        if check:
            isort_args.append("--check-only")
        else:
            isort_args.append("--apply")
        c.run(" ".join(isort_args))


@task
def lint(c):
    with c.cd(str(get_source_dir())):
        c.run("pipenv run flake8")
        c.run("pipenv run mypy")
