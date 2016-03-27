#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    digit_dict = dict([
        (2, [2, 4, 8, 6]),
        (3, [3, 9, 7, 1]),
        (4, [4, 6]),
        (5, [5]),
        (6, [6]),
        (7, [7, 9, 3, 1]),
        (8, [8, 4, 2, 6]),
        (9, [9, 1]),
    ])

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:
        temp_l = [(i, 0) for i in xrange(10)]
        ld_dict = dict(temp_l)

        data = [int(i) for i in test.strip().split()]
        a, n = data[0], data[1]

        ld_list = digit_dict[a]
        length = len(ld_list)

        x = n / length
        y = n % length

        for item in ld_list:
            ld_dict[item] = x

        for i in xrange(y):
            ld_dict[ld_list[i]] = ld_dict[ld_list[i]] + 1

        answer = ''

        for i in xrange(10):
            answer += (str(i) + ': ' + str(ld_dict[i]) + ', ')

        print answer[:-2]

    test_cases.close()


if __name__ == '__main__':
    main()