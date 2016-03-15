#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys
from collections import defaultdict


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = [list(i.strip().split()[0]) for i in test.strip().split('|')]
        count = 0

        for i in xrange(len(data) - 1):
            n_r = i + 1
            for j in xrange(len(data[0]) - 1):
                code_list = list()
                n_c = j + 1
                code_list.append(data[i][j])
                code_list.append(data[i][n_c])
                code_list.append(data[n_r][j])
                code_list.append(data[n_r][n_c])

                if ''.join(sorted(code_list)) == 'cdeo':
                    count += 1

        print count

if __name__ == '__main__':
    main()