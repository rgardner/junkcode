#!/usr/bin/env python3
"""Return random GIF urls"""

from __future__ import print_function

import requests


def main():
    endpoint = "http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC"
    r = requests.get(endpoint)
    print(r.json()["data"]["image_url"])


if __name__ == "__main__":
    main()
