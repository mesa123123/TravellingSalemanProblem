from TSP import Problem_Matrix
from sys import maxsize
import random as random
from .Climbs import hill_climb
from .Climbs import steep_climb
from .Climbs import distance_check

#Get all cities that the salesman must travel to; in other words his hometown is 1 but not in the collection
number_of_cities = 10
optimization_goal = 20
current_best_distance = maxsize
cities = [x for x in range(2,number_of_cities+1)]
paver = Problem_Matrix.ProblemMatrix(number_of_cities+1,4)
paver.Make_Matrix()
roads = paver.city_matrix

#Algorithm that can pick a random route
def random_permutation(iterable, r=None):
    "Random selection from itertools.permutations(iterable, r)"
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))
route = list(random_permutation(cities))




#Start the distance checking loops here
current_best_route = hill_climb(optimization_goal,number_of_cities,route,roads)
current_best_distance = distance_check(current_best_route,roads,number_of_cities)

print("Hill Climb Result")
print(current_best_route)
print(current_best_distance)

print("Steep Climb Result")
print(current_best_route)
print(current_best_distance)