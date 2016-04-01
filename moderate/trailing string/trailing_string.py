#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        line = test.strip().split(',')
        if line[0].endswith(line[1]):
            print '1'
        else:
            print '0'


if __name__ == '__main__':
    main()