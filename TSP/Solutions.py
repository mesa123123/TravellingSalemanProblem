from TSP import Problem_Matrix
from sys import maxsize
import random as random
from TSP.Climbs import hill_climb
from TSP.Climbs import steep_climb
from TSP.Climbs import distance_check

#Get all cities that the salesman must travel to; in other words his hometown is 1 but not in the collection
number_of_cities = 50
optimization_goal = number_of_cities*2
longest_distance = 4
current_best_distance = maxsize
cities = [x for x in range(2,number_of_cities+1)]
paver = Problem_Matrix.ProblemMatrix(number_of_cities+1,longest_distance)
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
current_best_distance = sum(distance_check(current_best_route,roads,number_of_cities))

print("Hill Climb Result")

if current_best_distance < optimization_goal:
    print("Optimal Route Found: ")
    print(current_best_route)
    print("Total Distance of Route: ")
    print(current_best_distance)
else:
    print("Solution Failure; Best Found: ")
    print(current_best_route)
    print("Total Distance of Route: ")
    print(current_best_distance)
