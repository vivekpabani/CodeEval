#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys
from collections import defaultdict


def count_before(pos, dist):
    count = 0
    temp_pos = pos

    while temp_pos >= 6:
        count += 1
        temp_pos -= dist

    return count-1


def count_after(pos, dist, w_len):
    count = 0
    temp_pos = pos

    while w_len - temp_pos >= 6:
        count += 1
        temp_pos += dist

    return count-1


def count_middle(start, end, dist):
    count = 0
    temp_pos = start

    while end - temp_pos >= dist:
        count += 1
        temp_pos += dist

    return count-1


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        line = test.split()
        w_len = int(line[0])
        dist = int(line[1])
        bat_count = int(line[2])
        bat_pos = line[3:]
        count = 0

        if bat_count == 0:
            if w_len >= 12:
                count = 1 + count_after(6, dist, w_len)
        elif bat_count == 1:
            count = count_before(int(bat_pos[0]), dist) + count_after(int(bat_pos[0]), dist, w_len)
        else:
            count += count_before(int(bat_pos[0]), dist)

            for i in xrange(len(bat_pos) - 1):
                count += count_middle(int(bat_pos[i]), int(bat_pos[i+1]), dist)

            count += count_after(int(bat_pos[-1]), dist, w_len)

        print count


if __name__ == '__main__':
    main()