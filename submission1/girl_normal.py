#!/usr/bin/env python3

"""Module containing class for the normal girl"""

from utility import Utility


class GirlNormal:
    """Class for normal girl.

    Methods:
        __init__ : Initialize the attributes.
        calc_happiness : Calculate happiness of the girl.
    """
    def __init__(self, girl):
        """Initialize attributes.

        Arguments:
            girl : Dictionary read from csv input file.

        Object attributes:
            name : Name.
            attrac : Attractiveness.
            intel : Intelligence.
            cost : Maintenance cost.
            criterion : Criterion for choosing boyfriend.
            happiness : Happiness.
            gift_recv : Price of gifts received.
            status : Relationship status. [False -> single, True -> committed]
            partner : Name of girlfriend.
        """
        self.name = girl['name']
        self.attrac = int(girl['attrac'])
        self.intel = int(girl['intel'])
        self.cost = int(girl['cost'])
        self.criterion = girl['criterion']
        self.happiness = int(girl['happiness'])
        self.gift_recv = int(girl['gift_recv'])
        self.status = Utility.str_to_bool(girl['status'])
        self.partner = girl['partner']

    def calc_happiness(self, gift_basket):
        """Calculate happiness of choosy girl.

        Happiness of the girl is equal to the price of gifts received plus
        value of gifts received over maintenance cost.

        Arguments:
            gift_basket : List of all the gifts received.
        """
        for gift in gift_basket:
            self.gift_recv += gift['value']

        self.happiness = self.gift_recv / self.cost
