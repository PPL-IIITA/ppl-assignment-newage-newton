#!/usr/bin/python3

from utility import Utility
from operator import itemgetter


class BoyMiser:
    def __init__(self, boy):
        self.name = boy['name']
        self.attrac = int(boy['attrac'])
        self.intel = int(boy['intel'])
        self.budget = int(boy['budget'])
        self.min_attrac_req = int(boy['min_attrac_req'])
        self.happiness = int(boy['happiness'])
        self.amount_spent = int(boy['amount_spent'])
        self.status = Utility.str_to_bool(boy['status'])
        self.partner = boy['partner']

    def gift_func(self, fem, gifts):
        gifts.sort(key=itemgetter('price'))
        gift_basket = []
        for gift in gifts:
            if self.amount_spent < fem.cost:
                gift_basket.append(gift)
                self.amount_spent += gift['price']
            else:
                break
        fem.gift_recv = self.amount_spent
        return gift_basket

    def calc_happiness(self, fem):
        self.happiness = self.budget - self.amount_spent
