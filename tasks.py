#!/usr/bin/env python3

import os.path
import sys

from invoke import Collection, task

from c_playground import tasks as c_playground_tasks
from cpp_playground import tasks as cpp_playground_tasks
from python_playground import tasks as python_playground_tasks
from rust_playground import tasks as rust_playground_tasks

sys.path.insert(
    1, os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools", "build")
)
from buildlib import ALL_PROJECTS


@task
def setup(c, release=False):
    c_playground_tasks.setup(c, release)
    cpp_playground_tasks.setup(c, release)
    python_playground_tasks.setup(c)


@task
def build(c, release=False):
    c_playground_tasks.build(c, release)
    cpp_playground_tasks.build(c, release)
    rust_playground_tasks.build(c, release)


@task
def test(c, release=False):
    c_playground_tasks.test(c, release)
    cpp_playground_tasks.test(c, release)
    python_playground_tasks.test(c)


@task
def format(c, release=False):
    c_playground_tasks.format(c, release)
    cpp_playground_tasks.format(c, release)
    rust_playground_tasks.format(c)
    python_playground_tasks.format(c)


@task(iterable=["projects"])
def lint(c, projects, release=False):
    if not projects:
        projects = ALL_PROJECTS

    if "c" in projects:
        c_playground_tasks.lint(c, release)
    if "cpp" in projects:
        cpp_playground_tasks.lint(c, release)
    if "rust" in projects:
        rust_playground_tasks.lint(c)
    if "python" in projects:
        python_playground_tasks.lint(c)


ns = Collection()
ns.add_task(setup)
ns.add_task(build)
ns.add_task(test)
ns.add_task(format)
ns.add_task(lint)
ns.add_collection(c_playground_tasks, name="c_playground")
ns.add_collection(cpp_playground_tasks, name="cpp_playground")
ns.add_collection(rust_playground_tasks, name="rust_playground")
ns.add_collection(python_playground_tasks, name="python_playground")
