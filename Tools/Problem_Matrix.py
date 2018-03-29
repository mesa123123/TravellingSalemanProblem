
import numpy as np
import random as rnd

class ProblemMatrix:
    city_matrix = None
    road_rule = None

    def __init__(self, size: int, longest: int):
        self.size = size
        self.longest = longest


    def Make_Matrix(self):
        city_weights = (self.size,self.size)
        city_weights = np.zeros(city_weights)
        for i in range(0,self.size):
            for j in range(self.size-1,0,-1):
                if i != j :
                    randWeighting = round(rnd.uniform(1, self.longest), 3)
                    city_weights[i][j] = randWeighting
                    city_weights[j][i] = randWeighting
        self.city_matrix = city_weights

    def random_permutation(list, r=None):
        #    "Random selection from itertools.permutations(iterable, r)"
        pool = tuple(list)
        r = len(pool) if r is None else r
        return tuple(rnd.sample(pool, r))