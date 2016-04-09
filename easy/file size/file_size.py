#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import sys
import os


def main():

    print os.path.getsize(sys.argv[1])


if __name__ == '__main__':
    main()