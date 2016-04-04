#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = test.strip().split()
        word = ''

        for item in data:
            if len(item) > len(word):
                word = item

        print word

if __name__ == '__main__':
    main()