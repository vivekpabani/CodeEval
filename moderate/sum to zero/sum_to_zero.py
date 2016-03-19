#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = [int(i) for i in test.strip().split(',')]

        pair_m = [[-1 for i in xrange(len(data))] for j in xrange(len(data))]

        for i in xrange(len(data)):
            for j in xrange(i+1, len(data)):
                pair_m[i][j] = data[i] + data[j]

        count = 0

        for i in xrange(len(data)):
            for j in xrange(i+1, len(data)):
                for k in xrange(j+1, len(data)):
                    for l in xrange(k+1, len(data)):
                        if pair_m[i][j] + pair_m[k][l] == 0:
                            count += 1

        print count

if __name__ == '__main__':
    main()