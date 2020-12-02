from invoke import Collection, task

from c_playground import tasks as c_playground_tasks
from cpp_playground import tasks as cpp_playground_tasks
from python_playground import tasks as python_playground_tasks
from rust_playground import tasks as rust_playground_tasks

PYTHON_DEPENDENCIES = [
    "black==19.10b0",
    "mypy==0.782",
    "pipenv==2020.6.2",
    "pylint==2.5.3",
]


@task
def setup(c, release=False):
    c.run(f"pip install {' '.join(PYTHON_DEPENDENCIES)}")
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
def fmt(c, release=False):
    c_playground_tasks.fmt(c, release)
    cpp_playground_tasks.fmt(c, release)
    rust_playground_tasks.fmt(c)
    python_playground_tasks.fmt(c)


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
ns.add_task(fmt)
ns.add_task(lint)
ns.add_collection(c_playground_tasks, name="c_playground")
ns.add_collection(cpp_playground_tasks, name="cpp_playground")
ns.add_collection(rust_playground_tasks, name="rust_playground")
ns.add_collection(python_playground_tasks, name="python_playground")
