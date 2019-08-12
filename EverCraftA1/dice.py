from random import randrange


def roll():
    return randrange(1,20)


def rollprint(roller):
    r=randrange(1,20)
    print(roller.get_name(),"rolled",r)
    return r