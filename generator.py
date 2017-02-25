#!/usr/bin/env python3

import string
import csv
import random


class Generator:
    @staticmethod
    def boy_generator(name, num):
        try:
            file = open(name, 'w')
            fieldnames = ['name', 'attrac', 'intel', 'budget', 'min_attrac_req', 'happiness', 'amount_spent', 'status',
                          'partner', 'category']
            csvout = csv.DictWriter(file, fieldnames=fieldnames)
            csvout.writeheader()

            for i in range(num):
                boy = {'name': ''.join(random.choice(string.ascii_lowercase) for j in range(6)),
                       'attrac': random.randint(1, 10), 'intel': random.randint(1, 10),
                       'budget': random.randrange(1000, 5000, 100), 'min_attrac_req': random.randint(1, 10),
                       'happiness': 0, 'amount_spent': 0, 'status': False, 'partner': None,
                       'category': random.choice(['mi', 'gk', 'gs'])}

                csvout.writerow(boy)

        except OSError as err:
            print("OS error: {0}".format(err))

    @staticmethod
    def girl_generator(name, num):
        try:
            file = open(name, 'w')
            fieldnames = ['name', 'attrac', 'intel', 'cost', 'criterion', 'happiness', 'gift_recv', 'status',
                          'partner', 'category']
            csvout = csv.DictWriter(file, fieldnames=fieldnames)
            csvout.writeheader()

            for i in range(num):
                girl = {'name': ''.join(random.choice(string.ascii_lowercase) for j in range(6)),
                        'attrac': random.randint(1, 10), 'intel': random.randint(1, 10),
                        'cost': random.randrange(1000, 5000, 100), 'criterion': random.choice(['a', 'r', 'i']),
                        'happiness': 0, 'gift_recv': 0, 'status': False, 'partner': None,
                        'category': random.choice(['d', 'c', 'n'])}

                csvout.writerow(girl)

        except OSError as err:
            print("OS error: {0}".format(err))

    @staticmethod
    def gift_generator(name, num):
        try:
            file = open(name, 'w')
            fieldnames = ['category', 'price', 'value', 'util_value', 'util_class', 'lux_rating', 'lux_diff']
            csvout = csv.DictWriter(file, fieldnames=fieldnames)
            csvout.writeheader()

            for i in range(num):
                gift = {}
                j = random.randint(1, 100)
                if j <= 50:
                    gift['category'] = 'e'
                    gift['price'] = random.randrange(10, 300, 10)
                    gift['value'] = random.randint(1, 5)
                    gift['util_value'] = 0
                    gift['util_class'] = 0
                    gift['lux_rating'] = 0
                    gift['lux_diff'] = 0
                elif j <= 80:
                    gift['category'] = 'u'
                    gift['price'] = random.randrange(200, 1000, 50)
                    gift['value'] = random.randint(3, 7)
                    gift['util_value'] = random.randint(1, 5)
                    gift['util_class'] = random.randint(1, 4)
                    gift['lux_rating'] = 0
                    gift['lux_diff'] = 0
                else:
                    gift['category'] = 'l'
                    gift['price'] = random.randrange(700, 2000, 100)
                    gift['value'] = random.randint(7, 10)
                    gift['util_value'] = 0
                    gift['util_class'] = 0
                    gift['lux_rating'] = random.randint(1, 5)
                    gift['lux_diff'] = random.randint(1, 3)

                csvout.writerow(gift)

        except OSError as err:
            print("OS error: {0}".format(err))
