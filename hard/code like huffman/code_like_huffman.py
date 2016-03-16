#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys
import collections


class Node(object):

    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        message = '(' + str(self.key) + ',' + str(self.value) + ')'

        return message

    def __str__(self):
        message = '(' + str(self.key) + ',' + str(self.value) + ')'

        return message


def find_path(node, path, path_dict):

    if node.left is None and node.right is None:
        path_dict[node.key] = path
    else:
        if node.left is not None:
            find_path(node.left, path + '0', path_dict)
        if node.right is not None:
            find_path(node.right, path + '1', path_dict)


def cal_huffman(root):

    path_dict = dict()

    find_path(root, '', path_dict)

    return path_dict


def main():

    test_cases = open(sys.argv[1], 'r')

    for test in test_cases:

        data = test.strip()
        data_dict = collections.Counter(data)
        node_list = list()

        for key, value in data_dict.items():
            node_list.append(Node(key, value))

        node_list = sorted(node_list, key=lambda x: (x.value, x.key))

        while len(node_list) > 1:
            node1 = node_list.pop(0)
            node2 = node_list.pop(0)

            new_key = node2.key + node1.key
            new_value = node1.value + node2.value
            new_node = Node(new_key, new_value, node1, node2)

            i = 0

            while i < len(node_list) and node_list[i].value < new_value:
                i += 1

            if i < len(node_list) and node_list[i].value == new_value:
                while i < len(node_list) and len(node_list[i].key) != 1:
                    i += 1

            node_list.insert(i, new_node)

        path_dict = cal_huffman(node_list[0])
        answer = ''

        for key in sorted(path_dict.keys()):
            answer += (key + ': ' + path_dict[key] + '; ')

        print answer[:-1]

    test_cases.close()


if __name__ == '__main__':
    main()