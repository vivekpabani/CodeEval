#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():
    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = test.split()
        x, y, n = int(data[0]), int(data[1]), int(data[2])

        output = ''

        for i in xrange(1, n+1):
            if i % x == 0 and i % y == 0:
                output += 'FB '
            elif i % x == 0:
                output += 'F '
            elif i % y == 0:
                output += 'B '
            else:
                output += (str(i) + ' ')

        print(output[:-1])

    test_cases.close()


if __name__ == '__main__':
    main()