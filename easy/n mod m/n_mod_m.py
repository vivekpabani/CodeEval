#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def n_mod_m(n, m):
    if n >= m:
        return n_mod_m(n-m, m)
    else:
        return n


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = test.strip().split(',')

        print n_mod_m(int(data[0]), int(data[1]))


if __name__ == '__main__':
    main()