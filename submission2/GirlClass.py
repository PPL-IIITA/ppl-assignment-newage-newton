#!/usr/bin/env python3

"""Module containing classes for girls."""

import math
from utility import Utility


class Girl:
    """Class for girl.

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
            partner : Name of boyfriend.
            category : Category of the girl. [Choosy, Desperate, Normal]
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
        self.category = girl['category']

    def calc_happiness(self, gift_basket):
        """Calculate happiness of the girl."""
        pass


class GirlChoosy(Girl):
    """Class for choosy girl.

    Methods:
        calc_happiness : Calculate happiness of the girl.
    """

    def calc_happiness(self, gift_basket):
        """Calculate happiness of choosy girl.

        Happiness of the girl is equal to logarithm of the price of gifts received plus
        value (twice the value, in case of luxury gifts) of gifts received over maintenance cost.

        Arguments:
            gift_basket : List of all the gifts received.
        """
        for gift in gift_basket:
            if gift['category'] == 'l':
                self.gift_recv += 2 * gift['value']
            else:
                self.gift_recv += gift['value']
        self.happiness = math.log(self.gift_recv / self.cost)


class GirlDesperate(Girl):
    """Class for desperate girl.

    Methods:
        calc_happiness : Calculate happiness of the girl.
    """

    def calc_happiness(self, gift_basket):
        """Calculate happiness of choosy girl.

        Happiness of the girl is equal to exponential of the price of gifts received over maintenance cost.

        Arguments:
            gift_basket : List of all the gifts received.
        """
        self.happiness = math.exp(self.gift_recv / self.cost)


class GirlNormal(Girl):
    """Class for normal girl.

    Methods:
        calc_happiness : Calculate happiness of the girl.
    """

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
