#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def happy_number(num):

    num_list = list()

    while True:

        if num == 1:
            happy = 1
            break

        if num in num_list:
            happy = 0
            break

        num_list.append(num)

        sum_num = 0

        while num:
            sum_num += (num % 10)**2
            num /= 10

        num = sum_num

    return happy


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        number = int(test.strip())

        print happy_number(number)


if __name__ == '__main__':
    main()