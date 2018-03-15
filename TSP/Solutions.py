from TSP import Problem_Matrix
from TSP.Climbs import hill_climb, steep_climb
from TSP.Route import Route
import pylab as pyl
from TSP.Problem_Matrix import ProblemMatrix



#Get all cities that the salesman must travel to; in other words his hometown is 1 but not in the collection
number_of_cities = 50
optimization_goal = number_of_cities*2
longest_distance = 4
cities = [x for x in range(2,number_of_cities+1)]


paver = Problem_Matrix.ProblemMatrix(number_of_cities+1,longest_distance)
paver.Make_Matrix()
paver.road_rule = list(Problem_Matrix.ProblemMatrix.random_permutation(cities))
roads = paver.city_matrix


hill_route = Route(paver, cities, False)
steep_route = Route(paver, cities, False)


journey = hill_climb(optimization_goal,number_of_cities,hill_route.route,roads)
journey2 = steep_climb(optimization_goal,number_of_cities,steep_route.route,roads)
print(journey2)
xValues = range(0,max(len(journey),len(journey2)))
optimization_line = [optimization_goal]*len(xValues)
#figure out how to make the lengths of journey and journey2 the same, so the shorter one just extends its final value
shortFall = len(xValues) - int(min(len(journey),len(journey2)))
for i in range(0,shortFall):
    if len(journey) < len(xValues):
        journey.append(journey[-1])
    elif len(journey2) < len(xValues):
        journey2.append(journey2[-1])
pyl.plot(xValues,optimization_line, 'r-')
pyl.plot(xValues, journey, 'b--')
pyl.plot(xValues, journey2, 'c--')
pyl.xlabel('Search Steps')
pyl.ylabel('Distance Found')
pyl.title('Hill_Climb Algorithm')
pyl.show()