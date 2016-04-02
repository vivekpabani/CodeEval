#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def reverse_and_add(num, trial):
    r_num = num[::-1]

    if num == r_num:
        return num,  trial

    else:
        ans = int(num) + int(r_num)
        return reverse_and_add(str(ans), trial + 1)


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        num = ''.join(test.strip())
        answer, trial = reverse_and_add(num, 0)
        print trial,
        print answer


if __name__ == '__main__':
    main()