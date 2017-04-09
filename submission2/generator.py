#!/usr/bin/env python3

"""Module to generate random boys, girls and gifts in csv file format."""

import string
import csv
import random


class Generator(object):
    """Class containing methods to generate random boys, girls and gifts.

    Methods:
        boy_generator : Generate a csv file containing information of boys.
        girl_generator : Generate a csv file containing information of girls.
        gift_generator : Generate a csv file containing information of gifts.
    """
    @staticmethod
    def boy_generator(name, num):
        """Method to generate random information for boys.

        Arguments:
            name : Name of csv file to be generated.
            num : No. of boys to be generated.

        Fieldnames:
            name : Name - 6 lowercase alphabets].
            attrac : Attractiveness - integer 1-10.
            intel : Intelligence - integer 1-10.
            budget : Girlfriend budget - integer 1000-5000.
            min_attrac_req : Minimum attraction requirement from girlfriend - integer 1-10.
            happiness : Happiness.
            amount_spent : Amount spent in buying gifts.
            status : Relationship status - bool True-Committed, False-Single.
            partner : Name of girlfriend.
            category : mi-miser, gk-geek, gs-generous.
        """
        try:
            file = open(name, 'w')
            fieldnames = ['name', 'attrac', 'intel', 'budget', 'min_attrac_req', 'happiness', 'amount_spent', 'status',
                          'partner', 'category']
            csvout = csv.DictWriter(file, fieldnames=fieldnames)
            csvout.writeheader()

            for i in range(num):
                boy = {'name': ''.join(random.choice(string.ascii_lowercase) for j in range(6)),
                       'attrac': random.randint(1, 10),
                       'intel': random.randint(1, 10),
                       'budget': random.randrange(1000, 5000, 100),
                       'min_attrac_req': random.randint(1, 10),
                       'happiness': 0,
                       'amount_spent': 0,
                       'status': False,
                       'partner': None,
                       'category': random.choice(['mi', 'gk', 'gs'])}

                csvout.writerow(boy)

        except OSError as err:
            print("OS error: {0}".format(err))

    @staticmethod
    def girl_generator(name, num):
        """Method to generate random information for girls.

        Arguments:
            name : Name of csv file to be generated.
            num : No. of girls to be generated.

        Fieldnames:
            name : Name - 6 lowercase alphabets].
            attrac : Attractiveness - integer 1-10.
            intel : Intelligence - integer 1-10.
            cost : Maintenance cost - integer 1000-5000.
            criterion : Criterion for choosing boyfriend - a-most attractive, r-richest, i-most intelligent.
            happiness : Happiness.
            gift_recv : Cost of gifts received.
            status : Relationship status - bool True-Committed, False-Single.
            partner : Name of boyfriend..
            category : d-desperate, c-choosy, n-normal.
        """
        try:
            file = open(name, 'w')
            fieldnames = ['name', 'attrac', 'intel', 'cost', 'criterion', 'happiness', 'gift_recv', 'status',
                          'partner', 'category']
            csvout = csv.DictWriter(file, fieldnames=fieldnames)
            csvout.writeheader()

            for i in range(num):
                girl = {'name': ''.join(random.choice(string.ascii_lowercase) for j in range(6)),
                        'attrac': random.randint(1, 10),
                        'intel': random.randint(1, 10),
                        'cost': random.randrange(1000, 5000, 100),
                        'criterion': random.choice(['a', 'r', 'i']),
                        'happiness': 0,
                        'gift_recv': 0,
                        'status': False,
                        'partner': None,
                        'category': random.choice(['d', 'c', 'n'])}

                csvout.writerow(girl)

        except OSError as err:
            print("OS error: {0}".format(err))

    @staticmethod
    def gift_generator(name, num):
        """Method to generate random information for gifts.

        Arguments:
            name : Name of csv file to generated.
            num : No. of gifts to be generated.

        Fieldnames:
            category : e-essential, u-utility, l-luxury
            price : Price of gift.
            value : Value of gift.
            util_value : Utility value - nonzero for utility gifts, zero otherwise.
            util_class : Utility class - nonzero for utility gifts, zero otherwise.
            lux_rating : Luxury rating - nonzero for luxury gifts, zero otherwise.
            lux_diff : Difficulty to obtain - nonzero for luxury gifts, zero otherwise.
        """
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
                    gift['price'] = random.randrange(100, 600, 50)
                    gift['value'] = random.randint(1, 5)
                    gift['util_value'] = 0
                    gift['util_class'] = 0
                    gift['lux_rating'] = 0
                    gift['lux_diff'] = 0
                elif j <= 80:
                    gift['category'] = 'u'
                    gift['price'] = random.randrange(300, 1200, 50)
                    gift['value'] = random.randint(3, 7)
                    gift['util_value'] = random.randint(1, 5)
                    gift['util_class'] = random.randint(1, 4)
                    gift['lux_rating'] = 0
                    gift['lux_diff'] = 0
                else:
                    gift['category'] = 'l'
                    gift['price'] = random.randrange(500, 1500, 100)
                    gift['value'] = random.randint(7, 10)
                    gift['util_value'] = 0
                    gift['util_class'] = 0
                    gift['lux_rating'] = random.randint(1, 5)
                    gift['lux_diff'] = random.randint(1, 3)

                csvout.writerow(gift)

        except OSError as err:
            print("OS error: {0}".format(err))
