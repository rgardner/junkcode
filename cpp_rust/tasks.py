import sys

import invoke


@invoke.task
def setup(ctx):
    # type: (invoke.Context) -> None
    ctx.run(
        "cmake -Bbuild -S. -GNinja -DCMAKE_BUILD_TYPE=Debug", pty=sys.stdout.isatty()
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
        f"cmake --build build --target runTests --config {config}",
        pty=sys.stdout.isatty(),
    )


@invoke.task
def run(ctx, release=False):
    # type: (invoke.Context, bool) -> None
    config = "Release" if release else "Debug"
    ctx.run(
        f"cmake --build build --target run --config {config}", pty=sys.stdout.isatty()
    )


@invoke.task
def clean(ctx, release=False):
    # type: (invoke.Context, bool) -> None
    config = "Release" if release else "Debug"
    ctx.run(
        f"cmake --build build --target clean --config {config}", pty=sys.stdout.isatty()
    )

