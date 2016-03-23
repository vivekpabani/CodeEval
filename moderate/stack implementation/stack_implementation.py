#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


class Stack(object):

    def __init__(self):
        self.count = 0
        self.item_list = list()

    def push(self, item):
        self.item_list.append(item)
        self.count += 1

    def pop(self):
        if self.count > 0:
            self.count -= 1
            return self.item_list.pop()
        else:
            return 'NA'


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        line = [int(i) for i in test.strip().split()]
        stack = Stack()

        for item in line:
            stack.push(item)

        answer = ''
        alternate = 1

        while True:
            popped = stack.pop()

            if popped == 'NA':
                break
            if alternate:
                answer += (str(popped) + ' ')

            alternate = 1 - alternate

        print answer[:-1]



if __name__ == '__main__':
    main()