import TSP.Problem_Matrix as P_M

class Route:
    route = None

    def __init__(self, paver, cities, fix_start):

        if not fix_start:
            self.route = list(P_M.ProblemMatrix.random_permutation(cities))
        else:
            self.route = list(paver.road_rule)

