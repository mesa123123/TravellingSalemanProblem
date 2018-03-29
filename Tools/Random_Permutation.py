import random as rnd


def random_permutation(iterable, r=None):
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(rnd.sample(pool, r))


def random_shuffle(members):
    rnd.shuffle(members)
    return tuple(members)
