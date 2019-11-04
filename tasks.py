from invoke import Collection, task

from cpp_playground import tasks as cpp_playground_tasks


@task
def setup(c, release=False):
    cpp_playground_tasks.setup(c, release)


@task
def build(c, release=False):
    cpp_playground_tasks.build(c, release)


@task
def test(c, release=False):
    cpp_playground_tasks.test(c, release)


@task
def format(c, release=False):
    cpp_playground_tasks.format(c, release)


namespace = Collection()
namespace.add_task(setup)
namespace.add_task(build)
namespace.add_task(test)
namespace.add_task(format)
namespace.add_collection(cpp_playground_tasks, name="cpp_playground")
