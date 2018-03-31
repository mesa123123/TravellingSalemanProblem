import numpy as np
import random as rnd
from Tools.Random_Permutation import random_permutation


class ProblemMatrix:
    city_matrix = None
    road_rule = None
    size = None
    longest = None

    def __init__(self, size: int, longest: int):
        self.size = size + 1
        self.longest = longest
        cities_model = [x for x in range(2, size)]
        self.road_rule = random_permutation(cities_model)

    def make_matrix(self):
        city_weights = (self.size, self.size)
        city_weights = np.zeros(city_weights)
        for i in range(0, self.size):
            for j in range(self.size-1, 0, -1):
                if i != j:
                    rand_weighting = round(rnd.uniform(1, self.longest), 3)
                    city_weights[i][j] = rand_weighting
                    city_weights[j][i] = rand_weighting
        self.city_matrix = city_weights
