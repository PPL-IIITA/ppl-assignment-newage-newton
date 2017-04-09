#!/usr/bin/env python3

"""Module for breakups"""

from ObjectAlloc import ObjectAlloc
from logger import Logger

class Breakup:
    """Implements a method for breaking up a couple.

    Method:
        breakup : Break-up a couple.
    """
    @staticmethod
    def breakup(couple, girls, boys):
        """Perform breakup of a couple.

        Change the status of boy and girl.and update it in the list of
        all boys and all girls.

        Arguments:
            couple : Couple to break up.
            girls : List of all girls.
            boys : List of all boys.
        """
        male = None
        fem = None
        for boy in boys:
            b = ObjectAlloc.find_object(boy)
            if b.name == couple['boy_name']:
                male = b

        for girl in girls:
            g = ObjectAlloc.find_object(girl)
            if g.name == couple['girl_name']:
                fem = g

        male.partner = None
        male.status = False
        fem.status = False
        fem.gift_recv = 0
        fem.happiness = 0
        male.amount_spent = 0
        male.happiness = 0

        Logger.breakup_logger(couple)

        for girl in girls:
            if girl['name'] == fem.name:
                girl['status'] = str(fem.status)
                girl['gift_recv'] = fem.gift_recv
                girl['happiness'] = fem.happiness

        for boy in boys:
            if boy['name'] == male.name:
                boy['status']  = str(male.status)
                boy['amount_spent'] = male.amount_spent
                boy['happiness'] = male.happiness
                boy['partner'] = str(male.partner)

        return