import contextlib
import os
import os.path
from pathlib import Path

from invoke import task


def get_source_dir() -> Path:
    return Path(os.path.dirname(os.path.abspath(__file__)))


@task
def build(c, release=False, verbose=False):
    with c.cd(str(get_source_dir())):
        args = ["cargo", "build"]
        if release:
            args.append("--release")
        if verbose:
            args.append("--verbose")
        c.run(" ".join(args))


@task
def run(c, bin, release=False):
    with c.cd(str(get_source_dir())):
        args = ["cargo", "run", "--bin", bin]
        if release:
            args.append("--release")
        c.run(" ".join(args))


@task
def fmt(c, check=False):
    with c.cd(str(get_source_dir())):
        args = ["cargo", "fmt"]
        if check:
            args.extend(["--", "--check"])
        c.run(" ".join(args))


@task
def lint(c, check=False):
    with c.cd(str(get_source_dir())):
        args = ["cargo", "clippy", "--all"]
        if check:
            args.extend(["--", "-D", "warnings"])
        c.run(" ".join(args))
