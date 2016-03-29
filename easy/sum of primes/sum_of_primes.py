#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

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


def main():

    answer, num, count = 2, 3, 1

    while count < 1000:
        if is_prime(num):
            answer += num
            count += 1
        num += 2

    print answer

if __name__ == '__main__':
    main()