#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def armstrong_number(num):

    num_len = len(str(num))

    sum_num = 0
    temp_num = num

    while num:
        sum_num += (num % 10)**num_len
        num /= 10

    return sum_num == temp_num


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        number = int(test.strip())

        print armstrong_number(number)


if __name__ == '__main__':
    main()