import contextlib
import os
import os.path
from pathlib import Path

from invoke import task


def get_source_dir() -> Path:
    return Path(os.path.dirname(os.path.abspath(__file__)))


@task
def build(c, release=False):
    with c.cd(str(get_source_dir())):
        if release:
            c.run("cargo build --release")
        else:
            c.run("cargo build")


@task
def run(c, bin, release=False):
    with c.cd(str(get_source_dir())):
        if release:
            c.run(f"cargo run --bin {bin} --release")
        else:
            c.run(f"cargo run --bin {bin}")


@task
def format(c):
    with c.cd(str(get_source_dir())):
        c.run("cargo fmt")


@task
def lint(c):
    with c.cd(str(get_source_dir())):
        c.run("cargo clippy --all")
