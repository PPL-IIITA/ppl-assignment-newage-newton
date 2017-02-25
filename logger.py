#!/usr/bin/env python3

import csv
import os
from datetime import datetime


class Logger:
    @staticmethod
    def couple_logger(c):
        c['time'] = datetime.now()
        file = open('couples.csv', 'a')
        csvout = csv.DictWriter(file, list(sorted(c.keys())))

        if os.stat('couples.csv').st_size == 0:
            csvout.writeheader()
        csvout.writerow(c)

    @staticmethod
    def gift_logger(gift_basket, boy, girl):
        row = {'from': boy.name, 'to': girl.name, 'gifts': gift_basket, 'time': datetime.now()}

        file = open('gift_exchange.csv', 'a')
        csvout = csv.DictWriter(file, list(sorted(row.keys())))

        if os.stat('gift_exchange.csv').st_size == 0:
            csvout.writeheader()
        csvout.writerow(row)



