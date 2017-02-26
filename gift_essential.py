#!/usr/bin/env python3

"""Module containing class for essential gifts."""


class GiftEssential(object):
    """Class for essential gifts.

    Methods:
        __init__ : Initialize gift.
    """
    def __init__(self, gift):
        """Method to initialize essential gift.

        Arguments:
            gift : Dictionary from input file.

        Object attributes:
            price : Price
            value : Value
        """
        self.price = gift['price']
        self.value = gift['value']
