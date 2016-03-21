#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')

    l1 = "-**--,--*--,***--,***--,-*---,****-,-**--,****-,-**--,-**--".split(',')
    l2 = "*--*-,-**--,---*-,---*-,*--*-,*----,*----,---*-,*--*-,*--*-".split(',')
    l3 = "*--*-,--*--,-**--,-**--,****-,***--,***--,--*--,-**--,-***-".split(',')
    l4 = "*--*-,--*--,*----,---*-,---*-,---*-,*--*-,-*---,*--*-,---*-".split(',')
    l5 = "-**--,-***-,****-,***--,---*-,***--,-**--,-*---,-**--,-**--".split(',')
    l = "-----"

    for test in test_cases:

        data = test.strip()

        p_line = ''

        for ch in data:
            if ch.isdigit():
                p_line += ch

        line1, line2, line3, line4, line5, line = '', '', '', '', '', ''

        for ch in p_line:
            line1 += l1[int(ch)]
            line2 += l2[int(ch)]
            line3 += l3[int(ch)]
            line4 += l4[int(ch)]
            line5 += l5[int(ch)]
            line += l

        print line1
        print line2
        print line3
        print line4
        print line5
        print line


if __name__ == '__main__':
    main()