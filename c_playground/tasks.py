"""Invoke tasks for C Playground."""

import enum
from enum import Enum
import os
from pathlib import Path
import shutil
import sys

from invoke import task


DOCKER_LINUX_TAG = "rgardner/junkcode/c-playground/linux:latest"


class TaskError(RuntimeError):
    ...


class Platform(Enum):
    MacOS = "macos"
    Linux = "linux"

    def __str__(self):
        return self.value

    @staticmethod
    def current() -> "Platform":
        if sys.platform.startswith("linux"):
            return Platform.Linux
        elif sys.platform.startswith("darwin"):
            return Platform.MacOS
        else:
            raise TaskError("Unsupported platform")


class BuildType(Enum):
    Debug = "Debug"
    Release = "Release"

    def __str__(self):
        return self.value


def get_source_dir() -> Path:
    return Path(os.path.dirname(os.path.abspath(__file__)))


def get_platform_build_path(
    build_type: BuildType, lint: bool = False, valgrind: bool = False
) -> Path:
    base = get_source_dir() / "build" / str(Platform.current())
    if valgrind:
        base /= "valgrind"

    if lint:
        base /= "lint"

    return base / str(build_type)


@task
def setup(c, release=False, valgrind=False, lint=False):
    build_type = BuildType.Release if release else BuildType.Debug
    build_dir = get_platform_build_path(build_type, lint=lint, valgrind=valgrind)
    build_dir.mkdir(exist_ok=True, parents=True)

    args = ["cmake", "-GNinja", f"-DCMAKE_BUILD_TYPE={build_type}"]
    if valgrind:
        args.append("-DC_PLAYGROUND_USE_VALGRIND:BOOL=ON")

    if lint:
        clang_tidy_path = shutil.which("clang-tidy")
        if clang_tidy_path is None:
            raise TaskError("clang-tidy could not be found on your PATH")

        args.append(f"-DCMAKE_CXX_CLANG_TIDY={clang_tidy_path}")

    args.append(str(get_source_dir()))
    with c.cd(str(build_dir)):
        c.run(" ".join(args), pty=sys.stdout.isatty())


@task
def build(c, release=False, lint=False, valgrind=False):
    build_type = BuildType.Release if release else BuildType.Debug
    build_dir = get_platform_build_path(build_type, lint=lint, valgrind=valgrind)
    c.run(f"cmake --build {build_dir}", pty=sys.stdout.isatty())


@task
def test(c, release=False, valgrind=False):
    build_type = BuildType.Release if release else BuildType.Debug
    build_dir = get_platform_build_path(build_type, valgrind=valgrind)
    c.run(f"cmake --build {build_dir} --target runTests", pty=sys.stdout.isatty())


@task
def format(c, release=False):
    # Format CMakeLists.txt files

    def cmake_format(full_path):
        c.run(f"cmake-format --in-place {full_path}")

    source_dir = get_source_dir()
    cmake_format(source_dir / "CMakeLists.txt")
    for root, dirs, files in os.walk(source_dir / "src"):
        for f in files:
            if f == "CMakeLists.txt":
                full_path = os.path.join(root, f)
                cmake_format(full_path)


@task
def lint(c, release=False):
    setup(c, release, lint=True)
    build(c, release, lint=True)


@task
def docker_build(c):
    c.run(f"docker build docker/linux --tag {DOCKER_LINUX_TAG}")


@task
def docker_run(c):
    source_dir = get_source_dir()
    c.run(
        f"docker run --interactive --tty \
		--volume {source_dir}:/usr/src/c-playground --rm \
		--workdir /usr/src/c-playground {DOCKER_LINUX_TAG} /bin/bash",
        pty=sys.stdin.isatty(),
    )
