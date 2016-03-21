#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        print int(test.strip(), 16)


if __name__ == '__main__':
    main()