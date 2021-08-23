"""Import file system locations."""

import pathlib


def proj_root() -> pathlib.Path:
    """Returns absolute path to project root."""
    p_r = pathlib.Path(__file__).parents[2]
    assert p_r.is_absolute()
    return p_r
