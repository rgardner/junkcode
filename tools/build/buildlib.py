#!/usr/bin/env python3

from __future__ import annotations

from enum import Enum
import os
import shutil
import sys
from typing import List


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


def apt_get_install_packages(c, packages: List[str]):
    packages_str = " ".join(packages)
    c.run(f"sudo apt-get install --yes --no-install-recommends {packages_str}")


def install_clang_tidy(c) -> str:
    """Installs clang-tidy and returns its path."""

    platform = Platform.current()
    if platform == platform.Linux:
        apt_get_install_packages(c, ["libllvm6.0", "clang-tidy-6.0", "clang-tidy"])
    elif platform == platform.MacOS:
        c.run("brew install llvm")
        os.symlink("/usr/local/opt/llvm/bin/clang-tidy", "/usr/local/bin/clang-tidy")
    else:
        raise TaskError("Unsupported platform to install clang-tidy")

    clang_tidy_path = shutil.which("clang-tidy")
    if clang_tidy_path is None:
        raise TaskError("clang-tidy is still not installed")

    return clang_tidy_path
