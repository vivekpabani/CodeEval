#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys
import itertools


def main():

    num_dict = dict([('0', list('0')), ('1', list('1')), ('2', list('abc')), ('3', list('def')), ('4', list('ghi')),
                     ('5', list('jkl')), ('6', list('mno')), ('7', list('pqrs')), ('8', list('tuv')),
                     ('9', list('wxyz'))])

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        line = test.strip().split()[0]
        a_l = list()

        for ch in line:
            a_l.append(num_dict[ch])

        ans_l = list(itertools.product(a_l[0], a_l[1], a_l[2], a_l[3], a_l[4], a_l[5], a_l[6]))

        print ','.join(sorted(list(set(''.join(ans_l[i]) for i in xrange(len(ans_l))))))

    test_cases.close()


if __name__ == '__main__':
    main()