#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = [i.strip() for i in test.strip().split(',')]
        o_str, r_str = data[0], data[1]

        for ch in r_str:
            o_str = o_str.replace(ch, '')

        print o_str


if __name__ == '__main__':
    main()