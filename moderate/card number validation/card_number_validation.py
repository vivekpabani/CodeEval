#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def find_luhn_sum(num_str):

    length = len(num_str)
    even = 0
    answer = 0

    while length > 0:
        digit = int(num_str[length-1])

        if even:
            digit *= 2

            if digit > 9:
                temp_sum = 0
                while digit > 0:
                    temp_sum += (digit % 10)
                    digit /= 10
                answer += temp_sum
            else:
                answer += digit
        else:
            answer += digit

        even = 1 - even
        length -= 1
    return answer


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = ''.join(test.strip().split())
        answer = find_luhn_sum(data)
        if answer % 10 == 0:
            print '1'
        else:
            print '0'


if __name__ == '__main__':
    main()