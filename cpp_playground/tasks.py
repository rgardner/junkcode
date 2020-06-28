"""Invoke tasks for C++ Playground."""

from __future__ import annotations

import enum
from enum import Enum
import os
import pathlib
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


def get_source_dir() -> pathlib.Path:
    return pathlib.Path(os.path.dirname(os.path.abspath(__file__)))


def get_platform_build_path(build_type: BuildType, lint: bool = False) -> pathlib.Path:
    base = get_source_dir() / "build" / str(Platform.current())
    if lint:
        base /= "lint"

    return base / str(build_type)


def run_clang_format(ctx, cpp_source_dir: pathlib.Path):
    run_clang_format_path = (
        get_source_dir().parent
        / "submodules"
        / "run-clang-format"
        / "run-clang-format.py"
    )
    ctx.run(f"{run_clang_format_path} --recursive {cpp_source_dir}")


@task
def setup(c, release=False, lint=False):
    c.run("pip install cmake-format==0.6.10")

    build_type = BuildType.Release if release else BuildType.Debug
    build_dir = get_platform_build_path(build_type, lint)
    build_dir.mkdir(exist_ok=True, parents=True)
    source_dir = get_source_dir()

    args = f"cmake -B{build_dir} -S{source_dir} -GNinja -DCMAKE_BUILD_TYPE={build_type}"
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
def fmt(c, release=False, check=False):
    # Format C++ code

    if check:
        run_clang_format(c, get_source_dir() / "src")
    else:
        build_type = BuildType.Release if release else BuildType.Debug
        build_dir = get_platform_build_path(build_type)
        cpp_format_args = ["cmake", "--build", str(build_dir), "--target"]
        cpp_format_args.append("fmt-check" if check else "fmt")
        c.run(" ".join(cpp_format_args))

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
		--volume {source_dir}:/usr/src/cpp-playground --rm \
		--workdir /usr/src/cpp-playground {DOCKER_LINUX_TAG} /bin/bash",
        pty=sys.stdin.isatty(),
    )
