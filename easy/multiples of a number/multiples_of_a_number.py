#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        numbers = [int(i) for i in test.strip().split(',')]

        start = 1

        while True:
            if numbers[1] * start >= numbers[0]:
                print numbers[1] * start
                break
            start += 1


if __name__ == '__main__':
    main()