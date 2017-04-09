#!/usr/bin/env python3

"""Module containing class for logging."""

import csv
import os
from datetime import datetime


class Logger:
    """Class for logging.

    Methods:
        couple_logger : Log information about couples in csv file format.
        gift_logger : Log details of gift exchanges in csv file format.
        breakup_logger : Log details of breakups in csv file format.
    """
    @staticmethod
    def couple_logger(c):
        """Method to log information about couples.

        Arguments:
            c : Couple.
        """
        c['time'] = datetime.now()
        file = open('couples.csv', 'a')
        csvout = csv.DictWriter(file, list(sorted(c.keys())))

        if os.stat('couples.csv').st_size == 0:
            csvout.writeheader()
        csvout.writerow(c)

    @staticmethod
    def gift_logger(gift_basket, boy, girl):
        """Method to log gift exchange information.

        Arguments:
            gift_basket : List of all gifts sent by the boy.
            boy : Boy who sent the gifts.
            girl : Girl who received the gifts.
        """
        row = {'from': boy.name, 'to': girl.name, 'gifts': gift_basket, 'time': datetime.now()}

        file = open('gift_exchange.csv', 'a')
        csvout = csv.DictWriter(file, list(sorted(row.keys())))

        if os.stat('gift_exchange.csv').st_size == 0:
            csvout.writeheader()
        csvout.writerow(row)

    @staticmethod
    def breakup_logger(couple):
        """Method to log breakup details.

        Arguments:
            couple : Dictionary containing the couple data which broke up.
        """

        row = {'boy_name': couple['boy_name'], 'girl_name': couple['girl_name'], 'time': datetime.now()}

        file = open('breakups.csv', 'a')
        csvout = csv.DictWriter(file, list(sorted(row.keys())))

        if os.stat('gift_exchange.csv').st_size == 0:
            csvout.writeheader()
        csvout.writerow(row)
