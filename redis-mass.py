#!/usr/bin/env python
"""
    redis-mass.py
    ~~~~~~~~~~~~~
    Prepares a newline-separated file of Redis commands for mass insertion.

    :copyright: (c) 2015 by Tim Simmons.
    :license: BSD, see LICENSE for more details.
"""
import sys

def proto(line):
    result = "*%s\r\n$%s\r\n%s\r\n" % (str(len(line)), str(len(line[0])), line[0])
    for arg in line[1:]:
        result += "$%s\r\n%s\r\n" % (str(len(arg)), arg)
    return result

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        f = open(filename, 'r')
    except IndexError:
        f = sys.stdin.readlines()

    for line in f:
        print proto(line.rstrip().split(' ')),
