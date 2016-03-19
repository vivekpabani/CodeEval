#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys
from collections import defaultdict


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        line = [int(i) for i in test.strip().split(',')]

        p1 = [[line[0], line[1]], [line[2], line[3]]]
        p2 = [[line[4], line[5]], [line[6], line[7]]]

        overlapped = True

        if p1[0][0] > p2[1][0] or p2[0][0] > p1[1][0] or p1[0][1] < p2[1][1] or p2[0][1] < p1[1][1]:
            overlapped = False

        if overlapped:
            print "True"
        else:
            print "False"

if __name__ == '__main__':
    main()