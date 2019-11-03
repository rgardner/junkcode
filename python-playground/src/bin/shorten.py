#!/usr/bin/env python3
"""Bit.ly CLI client."""

import json
import os
import sys
import urllib.parse


def build_request(api_url, access_token, url):
    query_format = "/v3/shorten?access_token={}&longUrl={}"
    return api_url + query_format.format(access_token, url)


def main():
    if len(sys.argv) != 2:
        print("usage: {} <url>", sys.argv[0], file=sys.stderr)

    long_url = sys.argv[1]
    long_url_encoded = urllib.parse.urlencode(long_url)

    api_url = "https://api-ssl.bitly.com"
    access_token = os.environ["BITLY_ACCESS_TOKEN"]
    request = build_request(api_url, access_token, long_url_encoded)
    response = urllib.request.urlopen(request)
    data = json.loads(response.read().decode("utf-8"))

    if int(data["status_code"]) != 200:
        print("Error: {}", data["status_txt"], file=sys.stderr)

    print(data["data"]["url"])


if __name__ == "__main__":
    main()
