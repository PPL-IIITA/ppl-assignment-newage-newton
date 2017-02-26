#!/usr/bin/env python3

"""Module containing class for luxury gits."""


class GiftLuxury(object):
    """Class for luxury gifts.

    Methods:
        __init__ : Initialize gifts.
    """
    def __init__(self, gift):
        """Method to initialize luxury gift.

        Arguments:
            gift : Dictionary from input file.

        Object attributes:
            price : Price
            value : Value
            lux_rating : Luxury rating
            lux_diff : Difficulty to obtain.
        """
        self.price = gift['price']
        self.value = gift['value']
        self.lux_rating = gift['lux_rating']
        self.lux_diff = gift['lux_diff']
