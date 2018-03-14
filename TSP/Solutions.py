from TSP import Problem_Matrix
from TSP.Climbs import hill_climb
import pylab as pyl
from TSP.Problem_Matrix import ProblemMatrix



#Get all cities that the salesman must travel to; in other words his hometown is 1 but not in the collection
number_of_cities = 50
optimization_goal = number_of_cities*2
longest_distance = 4
cities = [x for x in range(2,number_of_cities+1)]
paver = Problem_Matrix.ProblemMatrix(number_of_cities+1,longest_distance)
paver.Make_Matrix()
roads = paver.city_matrix

#Algorithm that can pick a random route
route = list(ProblemMatrix.random_permutation(cities))


journey = hill_climb(optimization_goal,number_of_cities,route,roads)
journey2 = hill_climb(optimization_goal,number_of_cities,route,roads)
xValues = range(0,len(max(journey,journey2)))
optimization_line = [optimization_goal]*len(xValues)
#figure out how to make the lengths of journey and journey2 the same, so the shorter one just extends its final value

pyl.plot(xValues,optimization_line, 'r-')
pyl.plot(xValues, journey, 'b--')
pyl.plot(xValues, journey2, 'c--')
pyl.xlabel('Search Steps')
pyl.ylabel('Distance Found')
pyl.title('Hill_Climb Algorithm')
pyl.show()