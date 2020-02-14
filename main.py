#!/usr/bin/env python
import argparse
import sys

import requests
from requests.exceptions import RequestException, TooManyRedirects


def run(urls):
    errors = 0
    for url in urls:
        errors += run_url(url) or 0
        print()
    return errors


def bold(s):
    return "\033[1m{}\033[0m".format(s)


def run_url(url):
    try:
        r = requests.get(url)
    except TooManyRedirects as exception:
        print("⚠️ ", "Too many redirects! Will give up after 30", "🌩")
        r = exception.response
    except RequestException as exception:
        print("😱 ❌ ⛈", str(exception))
        return 2

    for i, response in enumerate(r.history):
        print(i, i * ">", response.url, bold(response.status_code))
    i += 1
    print(i, i * ">", r.url, bold(r.status_code))


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "url", help="URL to start at (can be multiple)", nargs="+",
    )
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    return run(args.url)


if __name__ == "__main__":
    sys.exit(main())
