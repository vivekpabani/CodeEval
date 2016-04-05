#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = test.strip().split(',')

        bin_n = str(bin(int(data[0])))[2:]

        if bin_n[-int(data[1])] == bin_n[-int(data[2])]:
            print 'true'
        else:
            print 'false'

if __name__ == '__main__':
    main()