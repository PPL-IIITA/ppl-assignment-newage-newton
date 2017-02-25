#!/usr/bin/env python3

import csv


class Reader:
    @staticmethod
    def readfile(name):
        try:
            file = open(name, 'r')
            csvin = csv.DictReader(file)
            data = [row for row in csvin]
            return data

        except OSError as err:
            print('OS error: {0}'.format(err))
