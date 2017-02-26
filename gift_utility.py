#!/usr/bin/env python3

"""Module containing class for utility gifts."""


class GiftUtility:
    """Class for utility gifts.

    Methods:
        __init__ : Initialize gift.
    """
    def __init__(self, gift):
        """Method to initialize utility gift.

        Arguments:
            gift : Dictionary from input file.

        Object attributes:
            price : Price
            value : Value
            util_value : Utility value
            util_class : Utility class
        """
        self.price = gift['price']
        self.value = gift['value']
        self.util_value = gift['util_value']
        self.util_class = gift['util_class']
