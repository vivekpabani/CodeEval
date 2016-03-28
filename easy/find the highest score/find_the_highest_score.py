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

        data = [[int(j) for j in i.strip().split()] for i in test.strip().split('|')]
        updated_data = map(list, zip(*data))
        answer = ''

        for item in updated_data:
            answer += (str(max(item)) + ' ')

        print answer[:-1]


if __name__ == '__main__':
    main()