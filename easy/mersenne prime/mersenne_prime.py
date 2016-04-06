#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys
import math


def is_prime(number):
    if number == 2 or number == 3:
        return 1
    elif number % 2 == 0 or number % 3 == 0 or number == 1:
        return 0
    else:
        start = 5
        while start <= int(math.sqrt(number)):

            if number % start == 0:
                return 0
                break
            if number % (start+2) == 0:
                return 0
                break
            start += 6
        return 1


def mersenne_prime(num):

    mersenne_prime_list = [3, 7, 31, 127, 2047]
    prime_list = list()

    for item in mersenne_prime_list:
        if item < num:
            prime_list.append(item)

    return prime_list


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        number = int(test.strip())

        print ', '.join(str(i) for i in mersenne_prime(number))


if __name__ == '__main__':
    main()