import pathlib
import sys

import invoke

THIS_DIR = pathlib.Path(__file__).absolute().parent


@invoke.task
def setup(ctx):
    # type: (invoke.Context) -> None
    ctx.run(
        "cmake -Bbuild -S. -G'Ninja Multi-Config'", pty=sys.stdout.isatty(),
    )


@invoke.task
def build(ctx, release=False):
    # type: (invoke.Context, bool) -> None
    config = "Release" if release else "Debug"
    ctx.run(f"cmake --build build --config {config}", pty=sys.stdout.isatty())


@invoke.task
def test(ctx, release=True):
    # type: (invoke.Context, bool) -> None
    config = "Release" if release else "Debug"
    ctx.run(
        f"cmake --build build --target test --config {config}",
        env={"CTEST_OUTPUT_ON_FAILURE": "1"},
        pty=sys.stdout.isatty(),
    )


@invoke.task
def run(ctx, release=False):
    # type: (invoke.Context, bool) -> None
    config = "Release" if release else "Debug"
    ctx.run(
        f"cmake --build build --target run --config {config}", pty=sys.stdout.isatty(),
    )


@invoke.task
def clean(ctx, release=False):
    # type: (invoke.Context, bool) -> None
    config = "Release" if release else "Debug"
    ctx.run(
        f"cmake --build build --target clean --config {config}", pty=sys.stdout.isatty()
    )

