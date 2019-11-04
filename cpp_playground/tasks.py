"""Invoke tasks for C++ Playground."""

from __future__ import annotations

import enum
from enum import Enum
import os
from pathlib import Path
import shutil
import sys

from invoke import task


DOCKER_LINUX_TAG = "rgardner/junkcode/cpp-playground/linux:latest"


class TaskError(RuntimeError):
    ...


class Platform(Enum):
    MacOS = "macos"
    Linux = "linux"

    def __str__(self):
        return self.value

    @staticmethod
    def current() -> Platform:
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


def get_platform_build_path(build_type: BuildType, lint: bool = False) -> Path:
    base = Path.cwd() / "build" / str(Platform.current())
    if lint:
        base /= "lint"

    return base / str(build_type)


@task
def setup(c, release=False, lint=False):
    build_type = BuildType.Release if release else BuildType.Debug
    build_dir = get_platform_build_path(build_type, lint)
    build_dir.mkdir(exist_ok=True, parents=True)

    args = f"cmake -B {build_dir} -S. -GNinja -DCMAKE_BUILD_TYPE={build_type}"
    if lint:
        clang_tidy_path = shutil.which("clang-tidy")
        if clang_tidy_path is None:
            raise TaskError("clang-tidy could not be found on your PATH")

        args += f" -DCMAKE_CXX_CLANG_TIDY={clang_tidy_path}"

    c.run(args, pty=sys.stdout.isatty())


@task
def build(c, release=False, lint=False):
    build_type = BuildType.Release if release else BuildType.Debug
    build_dir = get_platform_build_path(build_type, lint)
    c.run(f"cmake --build {build_dir}", pty=sys.stdout.isatty())


@task
def test(c, release=False):
    build_type = BuildType.Release if release else BuildType.Debug
    build_dir = get_platform_build_path(build_type)
    c.run(f"cmake --build {build_dir} --target run", pty=sys.stdout.isatty())


@task
def format(c, release=False):
    # Format C++ code

    build_type = BuildType.Release if release else BuildType.Debug
    build_dir = get_platform_build_path(build_type)
    c.run(f"cmake --build {build_dir} --target format")

    # Format CMakeLists.txt files

    def cmake_format(full_path):
        c.run(f"cmake-format --in-place {full_path}")

    cmake_format(Path.cwd() / "CMakeLists.txt")
    for root, dirs, files in os.walk(Path.cwd() / "src"):
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
    c.run(
        f"docker run --interactive --tty \
		--volume {Path.cwd()}:/usr/src/cpp-playground --rm \
		--workdir /usr/src/cpp-playground {DOCKER_LINUX_TAG} /bin/bash",
        pty=sys.stdin.isatty(),
    )