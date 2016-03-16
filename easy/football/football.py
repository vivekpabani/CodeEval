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

        data = [i.strip().split() for i in test.strip().split('|')]
        team_dict = defaultdict(lambda: list())

        for i in xrange(len(data)):
            country = i + 1
            team_list = data[i]

            for item in team_list:
                team_dict[int(item)].append(country)

        answer = ''

        for key in sorted(team_dict.keys()):
            answer += (str(key) + ':')
            for value in sorted(team_dict[key]):
                answer += (str(value) + ',')
            answer = answer[:-1] + '; '

        print(answer[:-1])

if __name__ == '__main__':
    main()