#!/usr/bin/env python3

"""Module to make couples."""

from girl_choosy import GirlChoosy
from girl_desparate import GirlDesperate
from girl_normal import GirlNormal
from boy_generous import BoyGenerous
from boy_geek import BoyGeek
from boy_miser import BoyMiser
from utility import Utility
from couple import Couple
from logger import Logger


class CoupleMaker(object):
    """Implement method to make couple

    Methods:
        make_couple : Find a suitable boy for a girl and make a couple.
    """
    @staticmethod
    def make_couple(girl, boys, gifts, couples):
        """Find a suitable boy for a girl and initialize a couple.

        Find a suitable boy from the list of all boys and initialize a couple.
        Then perform gifting and calculate happiness, compatibility according to the type of boy and girl
        in the couple.
        Update the data in the list of all boys and list of all girls.

        Arguments :
            girl : A girl from the list of girls.
            boys : List of all boys.
            gifts : List of all gifts.
            couples : List of all couples.
        """
        fem = None
        male = None
        if girl['category'] == 'c':
            fem = GirlChoosy(girl)

        elif girl['category'] == 'n':
            fem = GirlNormal(girl)

        elif girl['category'] == 'd':
            fem = GirlDesperate(girl)

        suit_boy = {}
        if fem.criterion == 'a':
            """For maximum attractiveness."""
            suit_boy = {'name': None, 'attrac': 0}
            for boy in boys:
                if (Utility.str_to_bool(boy['status']) is False) and (int(boy['budget']) >= fem.cost) \
                        and (fem.attrac >= int(boy['min_attrac_req'])) and (int(boy['attrac']) > suit_boy['attrac']):
                    suit_boy['name'] = boy['name']
                    suit_boy['attrac'] = int(boy['attrac'])

        elif fem.criterion == 'r':
            """For maximum girlfriend budget."""
            suit_boy = {'name': None, 'budget': 0}
            for boy in boys:
                if (Utility.str_to_bool(boy['status']) is False) and (int(boy['budget']) >= fem.cost) \
                        and (fem.attrac >= int(boy['min_attrac_req'])) and (int(boy['budget']) > suit_boy['budget']):
                    suit_boy['name'] = boy['name']
                    suit_boy['budget'] = int(boy['budget'])

        elif fem.criterion == 'i':
            """For maximum intelligence."""
            suit_boy = {'name': None, 'intel': 0}
            for boy in boys:
                if (Utility.str_to_bool(boy['status']) is False) and (int(boy['budget']) >= fem.cost) \
                        and (fem.attrac >= int(boy['min_attrac_req'])) and (int(boy['intel']) > suit_boy['intel']):
                    suit_boy['name'] = boy['name']
                    suit_boy['intel'] = int(boy['intel'])

        if suit_boy['name'] is None:
            return

        else:
            boy = {}
            for boy in boys:
                if boy['name'] == suit_boy['name']:
                    break

            if boy['category'] == 'mi':
                male = BoyMiser(boy)
            elif boy['category'] == 'gk':
                male = BoyGeek(boy)
            elif boy['category'] == 'gs':
                male = BoyGenerous(boy)

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
