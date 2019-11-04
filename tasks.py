from invoke import Collection, task

from c_playground import tasks as c_playground_tasks
from cpp_playground import tasks as cpp_playground_tasks
from rust_playground import tasks as rust_playground_tasks


@task
def setup(c, release=False):
    c_playground_tasks.setup(c, release)
    cpp_playground_tasks.setup(c, release)


@task
def build(c, release=False):
    c_playground_tasks.build(c, release)
    cpp_playground_tasks.build(c, release)
    rust_playground_tasks.build(c, release)


@task
def test(c, release=False):
    c_playground_tasks.test(c, release)
    cpp_playground_tasks.test(c, release)


@task
def format(c, release=False):
    c_playground_tasks.format(c, release)
    cpp_playground_tasks.format(c, release)
    rust_playground_tasks.format(c)


@task
def lint(c, release=False):
    c_playground_tasks.lint(c, release)
    cpp_playground_tasks.lint(c, release)
    rust_playground_tasks.lint(c)


namespace = Collection()
namespace.add_task(setup)
namespace.add_task(build)
namespace.add_task(test)
namespace.add_task(format)
namespace.add_task(lint)
namespace.add_collection(c_playground_tasks, name="c_playground")
namespace.add_collection(cpp_playground_tasks, name="cpp_playground")
namespace.add_collection(rust_playground_tasks, name="rust_playground")
