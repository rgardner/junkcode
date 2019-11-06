#!/usr/bin/env bash

if [ "$#" -ne 1 ]; then
  echo "Invalid number of arguments" >&2
  echo "usage: $0 task_name" >&2
  exit 1
fi

readonly task_name="$1"

. junkcode-env/bin/activate
python3 -m invoke "${task_name}"
