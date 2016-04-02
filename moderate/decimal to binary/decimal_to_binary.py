#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        d_num = int(test.strip())
        print str(bin(d_num))[2:]


if __name__ == '__main__':
    main()

