#!/usr/bin/env bash
#
# This script was created to enable the project to use a newer version of
# Python than the system default.

if [ "$#" -ne 1 ]; then
  echo "Invalid number of arguments" >&2
  echo "usage: $0 task_name" >&2
  exit 1
fi

readonly task_name="$1"

# Tell pipenv to create a new virtual environment if needed instead of relying
# on the project-wide virtual environment.
. .venv/bin/activate
PIPENV_IGNORE_VIRTUALENVS=1 python3 -m invoke "${task_name}"
