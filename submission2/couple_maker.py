#!/usr/bin/env python3

"""Module to make couples."""

from ObjectAlloc import ObjectAlloc
from couple import Couple
from logger import Logger
from operator import itemgetter


class CoupleMaker:
    """Implement method to make couple

    Methods:
        make_couple : Find a suitable boy for a girl and make a couple.
        find_girl : Find a suitable girl for a boy and make a couple.
    """
    @staticmethod
    def make_couple(girl, boys, gifts, couples):
        """Find a suitable boy for a girl and initialize a couple.

        Find a suitable boy from the list of all boys and initialize a couple.
        Then perform gifting and calculate happiness, compatibility according
        to the type of boy and girl in the couple.
        Update the data in the list of all boys and list of all girls.

        Arguments :
            girl : A girl from the list of girls.
            boys : List of all boys.
            gifts : List of all gifts.
            couples : List of all couples.
        """
        fem = ObjectAlloc.find_object(girl)

        suit_boy = {}
        if fem.criterion == 'a':
            """For maximum attractiveness."""
            suit_boy = {'name': None, 'attrac': 0}
            for boy in boys:
                b = ObjectAlloc.find_object(boy)
                if b.status is False and b.budget >= fem.cost and b.name != fem.partner and \
                        fem.attrac >= b.min_attrac_req and b.attrac > suit_boy['attrac']:
                    suit_boy['name'] = b.name
                    suit_boy['attrac'] = b.attrac

        elif fem.criterion == 'r':
            """For maximum girlfriend budget."""
            suit_boy = {'name': None, 'budget': 0}
            for boy in boys:
                b = ObjectAlloc.find_object(boy)
                if b.status is False and b.budget >= fem.cost and b.name != fem.partner and \
                        fem.attrac >= b.min_attrac_req and b.budget > suit_boy['budget']:
                    suit_boy['name'] = boy['name']
                    suit_boy['budget'] = int(boy['budget'])

        elif fem.criterion == 'i':
            """For maximum intelligence."""
            suit_boy = {'name': None, 'intel': 0}
            for boy in boys:
                b = ObjectAlloc.find_object(boy)
                if b.status is False and b.budget >= fem.cost and b.name != fem.partner and \
                        fem.attrac >= b.min_attrac_req and b.intel > suit_boy['intel']:
                    suit_boy['name'] = boy['name']
                    suit_boy['intel'] = int(boy['intel'])

        if suit_boy['name'] is None:
            return

        else:
            boy = {}
            for boy in boys:
                if boy['name'] == suit_boy['name']:
                    break

            male = ObjectAlloc.find_object(boy)

            couple = Couple(male, fem)
            couple.happy_gift(male, fem, gifts)
            couple.calc_happiness(male, fem)
            couple.calc_compatibility(male, fem)
            couples.append(vars(couple))

            log = Logger()
            log.couple_logger(vars(couple))
            """Log couple information in csv file format."""

            girl['status'] = 'True'
            girl['partner'] = male.name
            girl['happiness'] = fem.happiness
            girl['gift_recv'] = fem.gift_recv

            for boy in boys:
                if boy['name'] == male.name:
                    boy['status'] = 'True'
                    boy['partner'] = fem.name
                    boy['amount_spent'] = male.amount_spent
                    boy['happiness'] = male.happiness
                    break

    @staticmethod
    def find_girl(boy, girls, gifts, couples):
        """Find a suitable girl for a boy and make a couple.

        Sort the girls in decreasing order of attractiveness.
        Find the most attractive girl who satisfies the constraints and
        form couple and do gifting.

        Arguments:
            boy: Boy from the list of all boys.
            girls: List of all girls.
            gifts: List of all gifts.
            couples: List of all couples.
        """
        girls.sort(key=itemgetter('attrac'), reverse=True)

        male = ObjectAlloc.find_object(boy)
        fem = None
        for girl in girls:
            g = ObjectAlloc.find_object(girl)
            if g.status == False and g.cost <= male.budget and g.attrac >= male.min_attrac_req:
                fem = g
                break

        if fem == None:
            return

        couple = Couple(male, fem)
        couple.happy_gift(male, fem, gifts)
        couple.calc_happiness(male, fem)
        couple.calc_compatibility(male, fem)
        couples.append(vars(couple))

        log = Logger()
        log.couple_logger(vars(couple))

        for girl in girls:
            if girl['name'] == fem.name:
                girl['status'] = 'True'
                girl['partner'] = male.name
                girl['happiness'] = fem.happiness
                girl['gift_recv'] = fem.gift_recv
                break

        boy['status'] = 'True'
        boy['partner'] = fem.name
        boy['amount_spent'] = male.amount_spent
        boy['happiness'] = male.happiness