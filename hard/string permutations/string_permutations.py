#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def find_all_per(o_str):
    """
    To find all permutations of a given string and store in a list.
    :param o_str: original string
    :return: list of permuted strings of the original string
    """
    per_list = list()
    find_per(o_str, '', per_list)

    return per_list


def find_per(o_str, per_str, per_list):
    """
    finds permutation of the given string and appends to the permuted list.
    it adds one character to the current permuted string and calls the function
    with the updated permuted and original string.
    :param o_str: original string
    :param per_str: current version of permuted string
    :param per_list: list of permuted strings of the original string
    :return:
    """
    # if length of original string is 0, means all characters have been used towards the permuted string.
    # so add the permuted string to the permuted list.
    if len(o_str) == 0:
        per_list.append(per_str)

    # else if there are still characters in the original string, move those characters from the original string
    # and append to the current permuted string. Then call the function with these new versions of both strings.
    else:
        for i in xrange(len(o_str)):
            find_per(o_str[:i] + o_str[i+1:], per_str + o_str[i], per_list)


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = test.strip()
        per_list = find_all_per(data)

        per_list = sorted(per_list)

        print ','.join(per_list)

    test_cases.close()


if __name__ == '__main__':
    main()