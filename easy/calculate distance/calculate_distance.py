#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys
import math


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = test.strip().split()

        p1, p2 = list(), list()

        p1.append(int(data[0].lstrip('(').rstrip(',')))
        p1.append(int(data[1].rstrip(')')))
        p2.append(int(data[2].lstrip('(').rstrip(',')))
        p2.append(int(data[3].rstrip(')')))

        print int(math.sqrt((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2))

if __name__ == '__main__':
    main()