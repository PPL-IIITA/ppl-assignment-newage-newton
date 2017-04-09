#!/usr/bin/env python3

"""Module containing classes for boys."""

from operator import itemgetter
from utility import Utility


class Boy:
    """Class for boy.

        Methods :
            __init__ : Initialize the attributes.
            gift_func : Set the gift basket for the girlfriend.
            calc_happiness : Calculate happiness of the boy.
    """

    def __init__(self, boy):
        """Initialize attributes.

        Arguments:
            boy : Dictionary read from csv input file.

        Object attributes:
            name : Name.
            attrac : Attractiveness.
            intel : Intelligence.
            budget : Girlfriend budget.
            min_attrac_req : Minimum attraction requirement from girlfriend.
            happiness : Happiness.
            amount_spent : Amount spent on gifts.
            status : Relationship status. [False -> single, True -> committed]
            partner : Name of girlfriend.
            category : Category of the boy. [Geek, Generous, Miser]
        """
        self.name = boy['name']
        self.attrac = int(boy['attrac'])
        self.intel = int(boy['intel'])
        self.budget = int(boy['budget'])
        self.min_attrac_req = int(boy['min_attrac_req'])
        self.happiness = int(boy['happiness'])
        self.amount_spent = int(boy['amount_spent'])
        self.status = Utility.str_to_bool(boy['status'])
        self.partner = boy['partner']
        self.category = boy['category']

    def gift_func(self, fem, gifts):
        """Set the gift basket."""
        pass

    def calc_happiness(self, fem):
        """Calculate happiness of the boy."""
        pass


class BoyGeek(Boy):
    """Class for geek boy.

    Methods :
        gift_func : Set the gift basket for the girlfriend.
        calc_happiness : Calculate happiness of the boy.
    """

    def gift_func(self, fem, gifts):
        """Set the gift basket.

        Sort the list of gifts by price. Add gifts to the basket
        until amount spent is equal to or greater than maintenance cost
        of girlfriend.
        If budget allows give one additional luxury gift.

        Arguments:
            fem : Girlfriend.
            gifts : List of all gifts.

        Returns:
            gift_basket : List of all gifts given to the girlfriend.
        """
        gifts.sort(key=itemgetter('price'))
        gift_basket = []
        for gift in gifts:
            if self.amount_spent < fem.cost:
                gift_basket.append(gift)
                self.amount_spent += gift['price']

            elif gift['category'] == 'l' and self.amount_spent + gift['price'] < self.budget:
                gift_basket.append(gift)
                self.amount_spent += gift['price']
                break
        fem.gift_recv = self.amount_spent
        return gift_basket

    def calc_happiness(self, fem):
        """Calculate happiness of the geek boy.

        Happiness of the boy is equal to the intelligence of his girlfriend.

        Arguments:
            fem : Girlfriend.
        """
        self.happiness = fem.intel


class BoyGenerous(Boy):
    """Class for generous boy.

    Methods:
        gift_func : Set the gift basket for the girlfriend.
        calc_happiness : Calculate happiness of the boy.
    """

    def gift_func(self, fem, gifts):
        """Set the gift basket.

        Sort the list of gifts by price. Add gifts to the basket
        until amount spent is equal to or less than girlfriend budget.

        Arguments:
            fem : Girlfriend.
            gifts : List of all gifts.

        Returns:
            gift_basket : List of all gifts given to the girlfriend.
        """
        gifts.sort(key=itemgetter('price'))
        gift_basket = []
        for gift in gifts:
            if self.amount_spent + gift['price'] <= self.budget:
                gift_basket.append(gift)
                self.amount_spent += gift['price']
            else:
                break
        fem.gift_recv = self.amount_spent
        return gift_basket

    def calc_happiness(self, fem):
        """Calculate happiness of the generous boy.

        Happiness of the boys is equal to the happiness of the girlfriend.

        Arguments:
            fem : Girlfriend.
        """
        self.happiness = fem.happiness


class BoyMiser(Boy):
    """Class for miser boy.

    Methods:
        gift_func : Set the gift basket for the girlfriend.
        calc_happiness : Calculate happiness of the boy.
    """

    def gift_func(self, fem, gifts):
        """Set the gift basket.

        Sort the list of gifts by price. Add gifts to the basket
        until amount spent is equal to or greater than maintenance cost
        of girlfriend.

        Arguments:
            fem : Girlfriend.
            gifts : List of all gifts.

        Returns:
            gift_basket : List of all gifts given to the girlfriend.
        """
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
        """Calculate happiness of the miser boy.

        Happiness of the boy is equal to the amount left in his budget.

        Arguments:
            fem : Girlfriend.
        """
        self.happiness = self.budget - self.amount_spent
