#!/usr/bin/env python


"""
Problem Definition :

https://www.codeeval.com/open_challenges/194/

TWENTY FORTY EIGHT

"""

__author__ = 'vivek'

import time
import sys


def main():
    start_time = time.time()

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = test.split(';')
        direction = data[0]
        length = int(data[1])
        mat_lines = data[2].split('|')

        matrix = list()

        for line in mat_lines:
            matrix.append([int(i) for i in line.split()])

    test_cases.close()

    print "Run time...{} secs \n".format(round(time.time() - start_time, 4))


if __name__ == '__main__':
    main()