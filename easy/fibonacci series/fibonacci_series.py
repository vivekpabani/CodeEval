#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def fibonacci(num):
    fib_l = [0, 1]

    for i in xrange(num-1):
        fib_l.append(fib_l[-1] + fib_l[-2])

    return fib_l[num]


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        num = int(test.strip())

        print fibonacci(num)


if __name__ == '__main__':
    main()