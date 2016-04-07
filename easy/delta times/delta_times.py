#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = [[int(j) for j in i.split(':')] for i in test.strip().split()]

        date1, date2 = data[0], data[1]

        if date1[0] != date2[0]:
            if date1[0] < date2[0]:
                date1, date2 = date2, date1
        elif date1[1] != date2[1]:
            if date1[1] < date2[1]:
                date1, date2 = date2, date1
        else:
            if date1[2] < date2[2]:
                date1, date2 = date2, date1

        hour, minute, sec = 0, 0, 0

        sec_diff = date1[2] - date2[2]

        if sec_diff < 0:
            sec_diff += 60
            minute -= 1
        sec += sec_diff

        if sec < 10:
            sec = '0' + str(sec)

        minute_diff = date1[1] - date2[1]

        if minute_diff < 0:
            minute_diff += 60
            hour -= 1
        minute += minute_diff

        hour += (date1[0] - date2[0])

        if sec < 10:
            sec = '0' + str(sec)
        if minute < 10:
            minute = '0' + str(minute)
        if hour < 10:
            hour = '0' + str(hour)
        print str(hour) + ':' + str(minute) + ':' + str(sec)


if __name__ == '__main__':
    main()