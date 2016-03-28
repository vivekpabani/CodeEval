#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys
import re


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        line = test.strip()
        u_line = re.sub('[^a-zA-Z]+', ' ', line)

        print ' '.join(word.lower() for word in u_line.split())


if __name__ == '__main__':
    main()