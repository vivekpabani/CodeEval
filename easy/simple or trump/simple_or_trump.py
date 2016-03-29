#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys


def main():

    test_cases = open(sys.argv[1], 'r')

    card_dict = dict([('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10),
                      ('J', 11), ('Q', 12), ('K', 13), ('A', 14)])
    for test in test_cases:

        data = test.strip().split('|')
        trump = data[1].strip()
        cards = [i.strip() for i in data[0].split()]

        val_suit = [(cards[0][:-1], cards[0][-1]), (cards[1][:-1], cards[1][-1])]
        val1, suit1 = val_suit[0][0], val_suit[0][1]
        val2, suit2 = val_suit[1][0], val_suit[1][1]

        if card_dict[val1] == card_dict[val2]:
            index_list = [0, 1]
        elif card_dict[val1] > card_dict[val2]:
            index_list = [0]
        else:
            index_list = [1]

        if (suit1 == suit2) or (suit1 != trump and suit2 != trump):
            answer = ' '.join(cards[i] for i in index_list)
        elif suit1 == trump:
            answer = cards[0]
        elif suit2 == trump:
            answer = cards[1]

        print answer


if __name__ == '__main__':
    main()