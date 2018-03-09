from TSP import Problem_Matrix
from sys import maxsize
import random as random

#Get all cities that the salesman must travel to; in other words his hometown is 1 but not in the collection
number_of_cities = 10
optimization_goal = 20
current_best_distance = maxsize
current_best = []
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
route = random_permutation(cities)

#Start the distance checking loops here


#then check the routes distance
distance = []
#append the distance from the hometown to the first stop
distance.append(roads[1][route[0]])
for i in range(1,number_of_cities-1):
    if i < number_of_cities-1:
        a = route[i-1]
        b = route[i]
    else:
        a = route[9]
        b = route[0]
    distance.append(roads[a][b])


#is it the best we've found so far?
if sum(distance) < current_best_distance:
    current_best_distance = sum(distance)
    #if so save it
    current_best = route
#is it optimal? if so we're done here if not, keep on going baby!
if current_best_distance <= optimization_goal:
    pass #this will be a break statement eventually

#make a swap,
#   if you can't, admit defeat
#and then loop around       - Distance checking loop ends
