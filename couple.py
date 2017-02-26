#!/usr/bin/env python3

"""Module containing class to manage couples

This module contains functions to initialize a couple object.
Perform exchange of gifts between boy and girl and calculate their respective happiness.
Calculate the compatibility and happiness of the couple.
"""

from logger import Logger


class Couple(object):
    """Class  to manage couples.

    Methods:
        __init__ : Initialize a couple
        happy_gift : Exchange gifts between boy and girl and calculate their happiness.
        calc_compatibility : Calculate compatibility of the couple.
        calc_happiness : Calculate happiness of the couple.
    """
    def __init__(self, boy, girl):
        """Initialize a couple.

        Arguments:
            boy : Boyfriend.
            girl : Girlfriend.

        Object attributes:
            boy_name : Name of boyfriend.
            girl_name : Name of girlfriend.
            happiness : happiness of the couple.
            compatibility : compatibility of the couple.
        """
        self.boy_name = boy.name
        self.girl_name = girl.name
        self.happiness = 0
        self.compatibility = 0
        boy.status = True
        girl.status = True
        boy.partner = girl.name
        girl.partner = boy.name

    @staticmethod
    def happy_gift(boy, girl, gifts):
        """Perform exchange of gifts between boy and girl, and then calculate their happiness.

        Arguments:
            boy : Boyfriend.
            girl : Girlfriend.
            gifts : List of all the gifts.
        """
        gift_basket = boy.gift_func(girl, gifts)
        Logger.gift_logger(gift_basket, boy, girl)
        """Log the gift exchange in csv file format."""
        girl.calc_happiness(gift_basket)
        boy.calc_happiness(girl)

    def calc_compatibility(self, boy, girl):
        """Calculate the compatibility of the couople.

        Arguments:
            boy : Boyfriend.
            girl : Girlfriend.
        """
        self.compatibility = boy.budget - girl.cost + abs(boy.attrac - girl.attrac) + abs(boy.intel - girl.intel)

    def calc_happiness(self, boy, girl):
        """Calculate the happiness of the couple.

        Arguments:
            boy : Boyfriend.
            girl : Girlfriend.
        """
        self.happiness = boy.happiness + girl.happiness
