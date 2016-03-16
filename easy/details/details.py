#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = [list(i.strip().split()[0]) for i in test.strip().split(',')]
        min_dist = len(data[0]) + 1

        for item in data:
            x_i = ''.join(item).rfind('X')
            y_i = item.index('Y')
            dist = y_i - x_i - 1
            if dist < min_dist:
                min_dist = dist

        print min_dist


if __name__ == '__main__':
    main()