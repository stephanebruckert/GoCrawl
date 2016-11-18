#!/usr/bin/python

import argparse
from gocrawl.core import core

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GoCrawl")

    parser.add_argument('-L', '--link', type=str, required=True,
                        help='Entry point URL')
    parser.add_argument('--silent', dest='silent', action='store_false',
                        help='Silent mode')
    parser.add_argument('-W', '--wait', type=int, required=False,
                        help='Minimum wait time in seconds between each \
                        request')
    parser.set_defaults(progress=True)

    args = parser.parse_args()
    core(args.link, args.progress, args.wait)
