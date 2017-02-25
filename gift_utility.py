#!/usr/bin/env python3


class GiftUtility:
    def __init__(self, gift):
        self.price = gift['price']
        self.value = gift['value']
        self.util_value = gift['util_value']
        self.util_class = gift['util_class']
