#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'


def main():
    answer = ''

    for i in xrange(1, 13):
        for j in xrange(1, 13):
            answer += "{:{}}".format(i*j, 4)
        answer += '\n'

    print answer


if __name__ == '__main__':
    main()