from TSP import Problem_Matrix
from TSP.Climbs import *
from TSP.Route import Route
from TSP.See_Salesman import plot_travels
from TSP.Simulated_Annealing import *


#DON'T TOUCH THIS PLEASE
def optimizer(optimization_show, number_of_cities, longest_distance):
    if optimization_show:
        return number_of_cities*(longest_distance//2)
    else:
        return 0

#The variables that control the outputs
same_start = True
optimization_show = True
number_of_cities = 50
longest_distance = 4
optimization_goal = number_of_cities*(longest_distance/2)
optimization_show = optimizer(optimization_show, number_of_cities, longest_distance)  #Shows whether or not we want the
                                                                                      # optimization goal to show up
                                                                                      # on the graph
cities = [x for x in range(2,number_of_cities+1)]
repeats = number_of_cities//5
init_temp = number_of_cities*repeats

#set up the roads between the cities
paver = Problem_Matrix.ProblemMatrix(number_of_cities+1,longest_distance)
paver.Make_Matrix()
paver.road_rule = list(Problem_Matrix.ProblemMatrix.random_permutation(cities))
roads = paver.city_matrix

#set up the routes, I've got many of them just in case you'd like to radomize the start points
hill_route = Route(paver, cities, same_start)
steep_route = Route(paver, cities, same_start)
repeated_hill_route = Route(paver, cities, same_start)
repeated_steep_route = Route(paver, cities, same_start)
annealing_route = Route(paver, cities, same_start)

#Implemennts the Algorithms and Plots them on a graph
journeys = []
#journeys.append([hill_climb(optimization_goal , hill_route.route, roads), 'hill_climb'])
#journeys.append([steep_climb(optimization_goal, steep_route.route, roads), 'steep_climb'])
#journeys.append([simulated_annealing(annealing_route.route, roads, init_temp), 'simulated_annealing'])
journeys.append([repeated_climb(optimization_goal, repeated_hill_route.route, roads, repeats), 'repeat_hill'])
journeys.append([repeated_climb(optimization_goal, repeated_steep_route.route, roads, repeats, True), 'steep_repeat'])
journeys.append([repeated_anneal(annealing_route.route, roads, init_temp, repeats),'repeated_simulated_annealing'])
plot_travels(journeys, optimization_goal, optimization_show)

