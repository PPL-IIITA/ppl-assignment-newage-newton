#!/usr/bin/env python3

from utility import Utility


class GirlNormal:
    def __init__(self, girl):
        self.name = girl['name']
        self.attrac = int(girl['attrac'])
        self.intel = int(girl['intel'])
        self.cost = int(girl['cost'])
        self.criterion = girl['criterion']
        self.happiness = int(girl['happiness'])
        self.gift_recv = int(girl['gift_recv'])
        self.status = Utility.str_to_bool(girl['status'])
        self.partner = girl['partner']

    def calc_happiness(self, gift_basket):
        for gift in gift_basket:
            self.gift_recv += gift['value']

        self.happiness = self.gift_recv / self.cost
