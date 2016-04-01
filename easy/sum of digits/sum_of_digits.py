#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        number = int(test.strip())
        answer = 0

        while number > 0:
            answer += number%10
            number /= 10

        print answer

if __name__ == '__main__':
    main()