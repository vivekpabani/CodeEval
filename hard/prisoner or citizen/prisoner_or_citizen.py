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

        t = [int(i) for i in data[1].strip().split()]

        jail = [[int(j) for j in i.strip().split()] for i in data[0].strip().split(',')]

        p1, p2, p3, p4 = jail[0], jail[1], jail[2], jail[3]

        con1 = (p1[0] <= t[0] <= p2[0] or p2[0] <= t[0] <= p1[0]) and (p3[0] <= t[0] <= p4[0] or p4[0] <= t[0] <= p3[0])
        con2 = (p2[0] <= t[0] <= p3[0] or p3[0] <= t[0] <= p2[0]) and (p1[0] <= t[0] <= p4[0] or p4[0] <= t[0] <= p1[0])
        con3 = (p2[1] <= t[1] <= p3[1] or p3[1] <= t[1] <= p2[1]) and (p1[1] <= t[1] <= p4[1] or p4[1] <= t[1] <= p1[1])
        con4 = (p1[1] <= t[1] <= p2[1] or p2[1] <= t[1] <= p1[1]) and (p3[1] <= t[1] <= p4[1] or p4[1] <= t[1] <= p3[1])

        if (con1 and con4) or (con2 and con3):
            print "Citizen"
        else:
            print "Prisoner"

    test_cases.close()


if __name__ == '__main__':
    main()