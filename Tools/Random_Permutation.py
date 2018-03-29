import random as rnd
import itertools as iter

def send_all(members):
    x = list(iter.permutations(members))
    rnd.shuffle(x)
    return x

def send_one(members):
    x = list(iter.permutations(members))
    y = x[rnd.randint(0,len(x))]
    return y