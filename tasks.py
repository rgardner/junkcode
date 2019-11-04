from invoke import Collection, task

from c_playground import tasks as c_playground_tasks
from cpp_playground import tasks as cpp_playground_tasks
from python_playground import tasks as python_playground_tasks
from rust_playground import tasks as rust_playground_tasks


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


@task
def lint(c, release=False):
    c_playground_tasks.lint(c, release)
    cpp_playground_tasks.lint(c, release)
    rust_playground_tasks.lint(c)
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
