#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = test.strip().split()
        num_door = int(data[0])
        num_iter = int(data[1])
        if num_iter > 1:
            open_count, close_count, neutral_count = 0, 0, 0

            for i in xrange(num_door):
                if (i+1) % 6 == 0:
                    open_count += 1
                elif (i+1) % 3 == 0:
                    neutral_count += 1
                elif (i+1) % 2 == 0:
                    close_count += 1
                else:
                    open_count += 1

            if num_iter % 2 == 0:
                close_count += neutral_count
            else:
                open_count += neutral_count
        else:
            open_count, close_count, neutral_count = num_door, 0, 0

        if num_iter > 0:
            if num_door % 6 == 0:
                close_count += 1
                open_count -= 1
            elif num_door % 3 == 0:
                if num_iter % 2 == 0:
                    open_count += 1
                    close_count -= 1
                else:
                    close_count += 1
                    open_count -= 1
            elif num_door % 2 == 0:
                open_count += 1
                close_count -= 1
            else:
                close_count += 1
                open_count -= 1

        print open_count


if __name__ == '__main__':
    main()