#!/usr/bin/env python3
"""
usage: git log --pretty=tformat: --shortstat | gitnetcode

Calculates the total number of lines of code added/removed.

Examples:
git log --pretty=tformat: --shortstat | gitnetcode
git log --author "Jane Smith" --pretty=tformat: --shortstat | gitnetcode
"""

import fileinput


def calc_net_lines(git_line) -> int:
    """
    Calculate net lines of code added/removed.

    example:
    ' 8 files changed, 247 insertions(+), 135 deletions(-)'
        = 247 - 135
        = 112
    """
    # remove leading/trailing spaces
    git_line = git_line.strip()
    parts = git_line.split(', ')
    insertions = 0
    deletions = 0
    for part in parts:
        if 'insertion' in part:
            # '247 insertions(+)'
            insertions = int(part.split(' ')[0])
        elif 'deletion' in part:
            # '135 deletions(-)'
            deletions = int(part.split(' ')[0])

    return insertions - deletions


def main():
    print(sum(calc_net_lines(line) for line in fileinput.input()))


if __name__ == '__main__':
    main()
