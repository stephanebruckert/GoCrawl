#!/usr/bin/python

import argparse
from gocrawl.core import core

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="What and how to parse")

    parser.add_argument('-L', '--link', type=str, required=True,
                        help='Entry point URL')
    parser.add_argument('-S', '--speed', type=int, required=False,
                        help='Time in seconds between each request')
    parser.add_argument('--progress', dest='progress', action='store_true',
                        help='Prints the progression')
    parser.set_defaults(progress=True)

    args = parser.parse_args()
    core(args.link, args.progress)
