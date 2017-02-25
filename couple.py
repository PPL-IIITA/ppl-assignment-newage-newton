#!/usr/bin/env python3

from logger import Logger


class Couple:
    def __init__(self, boy, girl):
        self.boy_name = boy.name
        self.girl_name = girl.name
        self.happiness = 0
        self.compatibility = 0
        boy.status = True
        girl.status = True
        boy.partner = girl.name
        girl.partner = boy.name

    @staticmethod
    def happy_gift(boy, girl, gifts):
        gift_basket = boy.gift_func(girl, gifts)
        Logger.gift_logger(gift_basket, boy, girl)
        girl.calc_happiness(gift_basket)
        boy.calc_happiness(girl)

    def calc_compatibility(self, boy, girl):
        self.compatibility = boy.budget - girl.cost + abs(boy.attrac - girl.attrac) + abs(boy.intel - girl.intel)

    def calc_happiness(self, boy, girl):
        self.happiness = boy.happiness + girl.happiness
