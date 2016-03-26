#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = test.strip().split('|')
        num_iter = int(data[1].strip())
        num_list = [int(i.strip()) for i in data[0].split()]

        for i in xrange(num_iter):
            first = 0
            second = 1
            changed = 0

            while not changed and second < len(num_list):
                if num_list[first] > num_list[second]:
                    num_list[first], num_list[second] = num_list[second], num_list[first]
                    changed = 1
                else:
                    first += 1
                    second += 1

        print ' '.join(str(e) for e in num_list)
if __name__ == '__main__':
    main()