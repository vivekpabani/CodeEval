#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():
    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = test.split(',')
        in_s = data[0].strip()
        ch = data[1].strip()

        if ch in in_s:
            print in_s.rindex(ch)
        else:
            print '-1'

    test_cases.close()


if __name__ == '__main__':
    main()