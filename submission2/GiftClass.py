#!/usr/bin/env python3

"""Module containing class for gifts."""


class Gift:
    """Class for gifts.

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


class GiftEssential(Gift):
    """Class for essential gifts."""
    pass


class GiftUtility(Gift):
    """Class for utility gifts.

    Methods:
        __init__ : Initialize gift.
    """
    def __init__(self, gift):
        """Method to initialize utility gift.

        Arguments:
            gift : Dictionary from input file.

        Object attributes:
            util_value : Utility value
            util_class : Utility class
        """
        super(GiftUtility, self).__init__(gift)
        self.util_value = gift['util_value']
        self.util_class = gift['util_class']


class GiftLuxury(Gift):
    """Class for luxury gifts.

    Methods:
        __init__ : Initialize gifts.
    """
    def __init__(self, gift):
        """Method to initialize luxury gift.

        Arguments:
            gift : Dictionary from input file.

        Object attributes:
            lux_rating : Luxury rating
            lux_diff : Difficulty to obtain.
        """
        super(GiftLuxury, self).__init__(gift)
        self.lux_rating = gift['lux_rating']
        self.lux_diff = gift['lux_diff']
