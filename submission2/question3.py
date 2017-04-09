#!/usr/bin/env python3

from reader import Reader
from generator import Generator
from couple_maker import CoupleMaker
from operator import itemgetter

if __name__ == "__main__":
    k = int(input("Enter k: "))
    Generator.boy_generator('boys.csv', 100)
    Generator.girl_generator('girls.csv', 10)
    Generator.gift_generator('gifts.csv', 100)

    boys = Reader.readfile('boys.csv')
    girls = Reader.readfile('girls.csv')
    gifts = Reader.readfile('gifts.csv')

    for gift in gifts:
        for key in gift:
            if key != 'category':
                gift[key] = int(gift[key])

    coupler = CoupleMaker()
    couples = []
    for girl in girls:
        coupler.make_couple(girl, boys, gifts, couples)

    couples.sort(key=itemgetter('happiness'), reverse=True)
    print(str(k) + ' Happiest couples')
    for couple, i in zip(couples, range(k)):
        print(couple)

    couples.sort(key=itemgetter('compatibility'), reverse=True)
    print(str(k) + ' Most compatible couples')
    for couple, i in zip(couples, range(k)):
        print(couple)
