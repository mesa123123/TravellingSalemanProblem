from TSP import Problem_Matrix
from TSP.Climbs import *
from TSP.Route import Route
import pylab as pyl



#Get all cities that the salesman must travel to; in other words his hometown is 1 but not in the collection
same_start = False
number_of_cities = 50
longest_distance = 4
optimization_goal = number_of_cities*(longest_distance/2)
cities = [x for x in range(2,number_of_cities+1)]


paver = Problem_Matrix.ProblemMatrix(number_of_cities+1,longest_distance)
paver.Make_Matrix()
paver.road_rule = list(Problem_Matrix.ProblemMatrix.random_permutation(cities))
roads = paver.city_matrix


hill_route = Route(paver, cities, same_start)
steep_route = Route(paver, cities, same_start)
repeated_hill_route = Route(paver, cities, same_start)


journey = hill_climb(optimization_goal,number_of_cities,hill_route.route,roads)
journey2 = steep_climb(optimization_goal,number_of_cities,steep_route.route,roads)
journey3 = repeated_climb(optimization_goal, number_of_cities, repeated_hill_route.route, roads, 5)
xValues = range(0,max(len(journey),len(journey2),len(journey3)))
optimization_line = [optimization_goal]*len(xValues)
#figure out how to make the lengths of journey and journey2 the same, so the shorter one just extends its final value
shortFall = len(xValues) - int(min(len(journey),len(journey2)))
for i in range(0,shortFall):
    if len(journey) < len(xValues):
        journey.append(journey[-1])
    if len(journey2) < len(xValues):
        journey2.append(journey2[-1])
    if len(journey3) < len(xValues):
        journey3.append(journey3[-1])
pyl.plot(xValues,optimization_line, 'r-')
pyl.plot(xValues, journey, 'b--', label='Hill Climb')
pyl.plot(xValues, journey2, 'k--', label='Steep-Hill Climb')
pyl.plot(xValues, journey3, 'y--', label='repeated_hill_climb')
pyl.legend(loc='upper right')
pyl.xlabel('Search Steps')
pyl.ylabel('Distance Found')
pyl.title('Hill_Climb Algorithm')
pyl.show()