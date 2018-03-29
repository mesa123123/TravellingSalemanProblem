from Tools.Random_Permutation import random_permutation


class Route:
    route = None

    def __init__(self, cities, fix_start, paver = None):

        if not fix_start:
            self.route = list(random_permutation(cities))
        else:
            self.route = list(paver.road_rule)
