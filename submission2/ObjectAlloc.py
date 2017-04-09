#!/usr/bin/env python3

"""Module containing function to create object according to category."""

import BoyClass
import GiftClass
import GirlClass

class ObjectAlloc:
    """Class containing function to create object according to category.

    Methods:
        find_object: Instantiate object according to category.
    """
    @staticmethod
    def find_object(val):
        """Instantiate object according to category.

        Arguments:
            val: Dictionary containing boy, girl or gift data.

        Returns:
            Instantiated object of appropriate type.
        """
        if val['category'] == 'gk':
            return BoyClass.BoyGeek(val)

        elif val['category'] == 'mi':
            return BoyClass.BoyMiser(val)

        elif val['category'] == 'gs':
            return BoyClass.BoyGenerous(val)

        elif val['category'] == 'n':
            return GirlClass.GirlNormal(val)

        elif val['category'] == 'c':
            return GirlClass.GirlChoosy(val)

        elif val['category'] == 'd':
            return GirlClass.GirlDesperate(val)

        elif val['category'] == 'e':
            return GiftClass.GiftEssential(val)

        elif val['category'] == 'u':
            return GiftClass.GiftUtility(val)

        elif val['category'] == 'l':
            return GiftClass.GiftLuxury(val)

        else:
            print("Object doesn't belong to any category")