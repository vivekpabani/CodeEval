#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')
    answer = 0

    for test in test_cases:

        number = int(test.strip())
        answer += number

    print answer

if __name__ == '__main__':
    main()