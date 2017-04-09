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
    boys.sort(key=itemgetter('attrac'), reverse=True)
    girls = Reader.readfile('girls.csv')
    girls.sort(key=itemgetter('cost'))
    gifts = Reader.readfile('gifts.csv')

    for gift in gifts:
        for key in gift:
            if key != 'category':
                gift[key] = int(gift[key])

    coupler = CoupleMaker()
    couples = []
    i = j = 0
    while i < len(girls) and j < len(boys):
        if girls[i]['status'] == 'False':
            coupler.make_couple(girls[i], boys, gifts, couples)
        i = i + 1

        if boys[j]['status'] == 'False':
            coupler.find_girl(boys[i], girls, gifts, couples)
        j = j + 1

    couples.sort(key=itemgetter('happiness'), reverse=True)
    print(str(k) + ' Happiest couples')
    for couple, i in zip(couples, range(k)):
        print(couple)

