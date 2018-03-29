import Tools.Problem_Matrix as P_M
from Tools.Random_Permutation import random_permutation

class Route:
    route = None

    def __init__(self, paver, cities, fix_start):

        if not fix_start:
            self.route = list(random_permutation(cities))
        else:
            self.route = list(paver.road_rule)

