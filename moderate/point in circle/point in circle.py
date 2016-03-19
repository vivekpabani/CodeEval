#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        line = test.split(';')
        center = [float(i.strip()) for i in line[0].lstrip('Center: (').rstrip(')').split(',')]
        radius = float(line[1].lstrip(' Radius: '))
        point = [float(i.strip()) for i in line[2].lstrip(' Point: (').strip().rstrip(')').split(',')]

        dist = (point[0] - center[0])**2 + (point[1] - center[1])**2

        if dist <= radius**2:
            print "true"
        else:
            print "false"

if __name__ == '__main__':
    main()