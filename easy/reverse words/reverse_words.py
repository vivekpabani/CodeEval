#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        o_str = test.strip()
        rev_str = o_str[::-1]
        words = rev_str.split()

        rev_words = list()

        for word in words:
            rev_words.append(word[::-1])

        print ' '.join(rev_words)


if __name__ == '__main__':
    main()