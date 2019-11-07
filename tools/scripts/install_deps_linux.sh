#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT=$(git rev-parse --show-toplevel)
readonly REPO_ROOT

sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt-get update

sudo apt-get install --yes --no-install-recommends \
  build-essential \
  ninja-build \
  python3.7 \
  python3.7-dev \
  python3.7-venv

if [ ! -d "${REPO_ROOT}/.venv/bin/activate" ]; then
  python3.7 -m venv "${REPO_ROOT}/.venv"
fi

. "${REPO_ROOT}/.venv/bin/activate"

python3 -m pip install --upgrade pip
python3 -m pip install invoke
