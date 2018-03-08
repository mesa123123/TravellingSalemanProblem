import itertools as iter
from TSP import Problem_Matrix
from sys import maxsize

#Get all cities that the salesman must travel to; in other words his hometown is 0
number_of_cities = 10
optimization_goal = 20
current_best_distance = maxsize
current_best = []
route = [x for x in range(0,number_of_cities+1)]
paver = Problem_Matrix.ProblemMatrix(10,4)
paver.Make_Matrix()
roads = paver.city_matrix
#this allows the algorithm to pick a random path but it needs to return one, not all of them!
# allPerm = iter.permutations(route)
# for item in allPerm:
#     print(item)

#then check the routes distance
distance = []
for i in range(0,10):
    if i < 9:
        a = route[i]
        b = route[i+1]
    else:
        a = route[9]
        b = route[0]
    distance.append(roads[a][b])

#is it the best we've found so far?
if sum(distance) < current_best_distance:
    current_best_distance = sum(distance)
    current_best = route

#is it optimal? if so we're done here if not, keep on going baby!
if current_best_distance <= optimization_goal:
    pass #this will be a break statement eventually

