#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():
    test_cases = open(sys.argv[1], 'r')
    char_l = list('abcdefghij')

    for test in test_cases:

        data = test.strip()
        num = ''

        for ch in data:
            if ch.isdigit():
                num += ch
            elif ch in char_l:
                num += str(char_l.index(ch))

        if num:
            print num
        else:
            print "NONE"

    test_cases.close()


if __name__ == '__main__':
    main()