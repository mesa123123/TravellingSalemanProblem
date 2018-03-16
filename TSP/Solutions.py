from TSP import Problem_Matrix
from TSP.Climbs import *
from TSP.Route import Route
import pylab as pyl
from TSP.Simulated_Annealing import simulated_annealing


#Get all cities that the salesman must travel to; in other words his hometown is 1 but not in the collection
same_start = True
number_of_cities = 50
longest_distance = 4
optimization_goal = number_of_cities*(longest_distance/2)
cities = [x for x in range(2,number_of_cities+1)]
repeats = number_of_cities//5
init_temp = number_of_cities*repeats


paver = Problem_Matrix.ProblemMatrix(number_of_cities+1,longest_distance)
paver.Make_Matrix()
paver.road_rule = list(Problem_Matrix.ProblemMatrix.random_permutation(cities))
roads = paver.city_matrix


hill_route = Route(paver, cities, same_start)
steep_route = Route(paver, cities, same_start)
repeated_hill_route = Route(paver, cities, same_start)
repeated_steep_route = Route(paver, cities, same_start)
annealing_route = Route(paver, cities, same_start)


journey = hill_climb(optimization_goal , hill_route.route, roads)
journey2 = steep_climb(optimization_goal, steep_route.route, roads)
journey3 = repeated_climb(optimization_goal, repeated_hill_route.route, roads, repeats)
journey4 = repeated_climb(optimization_goal, repeated_steep_route.route, roads, repeats, True)
journey5 = simulated_annealing(optimization_goal, annealing_route.route, roads, init_temp)

xValues = range(0,max(len(journey),len(journey2),len(journey3),len(journey4), len(journey5)))
optimization_line = [optimization_goal]*len(xValues)
while len(xValues) > int(min(len(journey), len(journey2), len(journey3), len(journey4), len(journey5))):
    if len(journey) < len(xValues):
        journey.append(journey[-1])
    if len(journey2) < len(xValues):
        journey2.append(journey2[-1])
    if len(journey3) < len(xValues):
        journey3.append(journey3[-1])
    if len(journey4) < len(xValues):
        journey4.append(journey4[-1])
    if len(journey5) < len(xValues):
        journey5.append(journey5[-1])
pyl.plot(xValues,optimization_line, 'r-')
pyl.plot(xValues, journey, 'b--', label='Hill Climb')
pyl.plot(xValues, journey2, 'c--', label='Steep-Hill Climb')
pyl.plot(xValues, journey3, 'y--', label='repeated_hill_climb')
pyl.plot(xValues, journey4, 'k--', label='repeated_steep_climb')
pyl.plot(xValues, journey5, 'g--', label='simulated_annealing')
pyl.legend(loc='upper left')
pyl.xlabel('Search Steps')
pyl.ylabel('Distance Found')
pyl.title('Hill_Climb Algorithm')
pyl.show()