#!/usr/bin/env bash

sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt-get update

sudo apt-get install --yes --no-install-recommends \
  ninja-build \
  python3.7 \
  python3.7-venv

python3.7 -m venv junkcode-env && . junkcode-env/bin/activate

python3 -m pip install invoke pipenv
