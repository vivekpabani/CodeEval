#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys
import string


def main():

    # create a list of alphabets, with 0 to blank character.
    alpha_list = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                  'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    sq_num = 26*26
    num = 26

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        col_num = int(test.strip())

        # Logic: the first letter from left is the coefficient(multiple) of square of 26
        # the second letter is the coefficient(multiple) of 26
        # so find those individual offsets, ranging between 0 to 26 inclusive
        # 0 -> '', 1-> 'A', 26-> 'Z'

        c1 = col_num/sq_num
        col_num %= sq_num

        c2 = col_num/num
        col_num %= num

        c3 = col_num

        # in case it is in form like x*26*26 + y*26 + 0 or x*26*26 + 0 + y
        # replace those trailing zeros with 26 -> 'Z', and deduct one from previous char.
        if c3 == 0 and c2 > 0:
            c3 = num
            c2 -= 1
        if c2 == 0 and c1 > 0:
            c2 = num
            c1 -= 1

        col_name = alpha_list[c1] + alpha_list[c2] + alpha_list[c3]

        print col_name

    test_cases.close()


if __name__ == '__main__':
    main()