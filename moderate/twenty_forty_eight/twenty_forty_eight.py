#!/usr/bin/env python


"""
Problem Definition :

https://www.codeeval.com/open_challenges/194/

TWENTY FORTY EIGHT

"""

__author__ = 'vivek'

import sys


def move(matrix, direction, length):

    if direction == "UP":

        for i in xrange(0, length):
            track_l = list()
            current = length - 1
            track_l.append(current)
            temp = track_l[-1] - 1

            while current != 0:

                if temp <= -1:
                    current = 0
                elif matrix[temp][i] == 0:
                    if temp == 0:
                        track_l.append(current)
                    temp = temp - 1
                elif matrix[temp][i] == matrix[current][i]:
                    matrix[temp][i] = matrix[temp][i] * 2
                    matrix[current][i] = 0
                    current = temp - 1
                    track_l.pop()
                    track_l.append(current + 1)
                    temp = current - 1
                else:
                    current = temp
                    track_l.append(current)
                    temp = temp - 1
            track_l = reversed(track_l)

            for item in track_l:
                for k in xrange(item):
                    if matrix[k][i] == 0:
                        matrix[k][i] = matrix[item][i]
                        matrix[item][i] = 0

    elif direction == "RIGHT":

        for i in xrange(0, length):
            track_l = list()
            current = 0
            track_l.append(current)
            temp = track_l[-1] + 1

            while current != length - 1:

                if temp >= length:
                    if temp == length - 1:
                        track_l.append(current)
                    current = length - 1
                elif matrix[i][temp] == 0:
                    temp = temp + 1
                elif matrix[i][temp] == matrix[i][current]:
                    matrix[i][temp] = matrix[i][temp] * 2
                    matrix[i][current] = 0
                    current = temp + 1
                    track_l.pop()
                    track_l.append(current - 1)
                    temp = current + 1
                else:
                    current = temp
                    track_l.append(current)
                    temp = temp + 1

            track_l = reversed(track_l)

            for item in track_l:
                for k in xrange(length-1, item, -1):
                    if matrix[i][k] == 0:
                        matrix[i][k] = matrix[i][item]
                        matrix[i][item] = 0

    elif direction == "LEFT":

        for i in xrange(0, length):
            track_l = list()
            current = length - 1
            track_l.append(current)
            temp = track_l[-1] - 1

            while current != 0:

                if temp <= -1:
                    if temp == 0:
                        track_l.append(current)
                    current = 0
                elif matrix[i][temp] == 0:
                    temp = temp - 1
                elif matrix[i][temp] == matrix[i][current]:
                    matrix[i][temp] = matrix[i][temp] * 2
                    matrix[i][current] = 0
                    current = temp - 1
                    track_l.pop()
                    track_l.append(current + 1)
                    temp = current - 1
                else:
                    current = temp
                    track_l.append(current)
                    temp = temp - 1

            track_l = reversed(track_l)

            for item in track_l:
                for k in xrange(item):
                    if matrix[i][k] == 0:
                        matrix[i][k] = matrix[i][item]
                        matrix[i][item] = 0

    elif direction == "DOWN":

        for i in xrange(0, length):
            track_l = list()
            current = 0
            track_l.append(current)
            temp = track_l[-1] + 1

            while current != length - 1:

                if temp >= length:
                    if temp == length - 1:
                        track_l.append(current)
                    current = length - 1
                elif matrix[temp][i] == 0:
                    temp = temp + 1
                elif matrix[temp][i] == matrix[current][i]:
                    matrix[temp][i] = matrix[temp][i] * 2
                    matrix[current][i] = 0
                    current = temp + 1
                    track_l.pop()
                    track_l.append(current - 1)
                    temp = current + 1
                else:
                    current = temp
                    track_l.append(current)
                    temp = temp + 1

            track_l = reversed(track_l)

            for item in track_l:
                for k in xrange(length-1, item, -1):
                    if matrix[k][i] == 0:
                        matrix[k][i] = matrix[item][i]
                        matrix[item][i] = 0
    output = ''

    for row in matrix:
        for item in row:
            output += (str(item) + ' ')
        output = output[:-1] + '|'

    print output[:-1]


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = test.split(';')
        direction = data[0]
        length = int(data[1])
        mat_lines = data[2].split('|')

        matrix = list()

        for line in mat_lines:
            matrix.append([int(i) for i in line.split()])

        move(matrix, direction, length)

    test_cases.close()


if __name__ == '__main__':
    main()