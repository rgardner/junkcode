#!/usr/bin/env bash

sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt-get update

sudo apt-get install --yes --no-install-recommends \
  build-essential \
  ninja-build \
  python3.7 \
  python3.7-dev \
  python3.7-venv

python3.7 -m venv .venv && . .venv/bin/activate

python3 -m pip install --upgrade pip
python3 -m pip install invoke pipenv
