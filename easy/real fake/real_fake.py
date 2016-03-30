#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def find_real_fake(num_str):

    length = len(num_str)
    even = 0
    answer = 0

    while length > 0:
        digit = int(num_str[length-1])

        if even:
            digit *= 2
        answer += digit

        even = 1 - even
        length -= 1
    return answer


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = ''.join(test.strip().split())
        answer = find_real_fake(data)

        if answer % 10 == 0:
            print 'Real'
        else:
            print 'Fake'


if __name__ == '__main__':
    main()