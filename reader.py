#!/usr/bin/env python3

"""Module containing class to read data from csv files."""
import csv


class Reader:
    """Class for reading data from csv files.

    Methods:
        readfile : Read a csv file.
    """
    @staticmethod
    def readfile(name):
        """Read csv file and return list of dictionaries containing data.

        Arguments:
            name : Name of file to be read.

        Returns:
            data : List of dictionaries.
        """
        try:
            file = open(name, 'r')
            csvin = csv.DictReader(file)
            data = [row for row in csvin]
            return data

        except OSError as err:
            print('OS error: {0}'.format(err))
