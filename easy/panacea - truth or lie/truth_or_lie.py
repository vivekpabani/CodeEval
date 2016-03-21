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
        hexa_dec = data[0].strip().split()
        binary = data[1].strip().split()

        hexa_num_list = list()
        for item in hexa_dec:
            hexa_num_list.append(int(item, 16))

        bin_num_list = list()
        for item in binary:
            bin_num_list.append(int(item, 2))
        if set(hexa_num_list) == set(bin_num_list) or sum(hexa_num_list) <= sum(bin_num_list):
            print('True')
        else:
            print('False')

if __name__ == '__main__':
    main()