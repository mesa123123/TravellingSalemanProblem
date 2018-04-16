from Tools import Problem_Matrix
from Tools.Route import Route
from TSP.Climbs import *
from Tools.See_Salesman import plot_travels
from TSP.Simulated_Annealing import *
from GA_TSP.Evolve_Population import *


def optimizer(optimize_goal, city_number, long_roads):
    if optimize_goal:
        return city_number*(long_roads//2)
    else:
        return 0

# The variables that control the outputs
same_start = True
optimization_show = True
number_of_cities = 50
longest_distance = 4
optimization_goal = number_of_cities*(longest_distance/2)
optimization_show = optimizer(optimization_show, number_of_cities, longest_distance)    # Shows whether or not we want
# the optimization goal to show up on the graph
cities = [x for x in range(2, number_of_cities+1)]
repeats = number_of_cities//5
init_temp = number_of_cities*repeats
pop_size = 16

# set up the roads between the cities
paver = Problem_Matrix.ProblemMatrix(number_of_cities, longest_distance)
paver.road_rule = list(random_permutation(cities))
paver.make_matrix()
roads = paver.city_matrix

# set up the routes, I've got many of them just in case you'd like to radomize the start points
hill_route = Route(cities, same_start, paver)
steep_route = Route(cities, same_start, paver)
# repeated_hill_route = Route(cities, same_start, paver)
# repeated_steep_route = Route(cities, same_start, paver)
annealing_route = Route(cities, same_start, paver)

# Implemennts the Algorithms and Plots them on a graph
journeys = list()
journeys.append([hill_climb(optimization_goal , hill_route.route, roads), 'hill_climb'])
journeys.append([steep_climb(optimization_goal, steep_route.route, roads), 'steep_climb'])
journeys.append([simulated_annealing(annealing_route.route, roads, init_temp), 'simulated_annealing'])
journeys.append([steep_simulated_annealing(annealing_route.route,roads,init_temp),"steep_annealing"])
journeys.append([create_result(number_of_cities, paver, pop_size, "order", "rank", "elitism")])
# journeys.append([repeated_climb(optimization_goal, repeated_hill_route.route, roads, repeats), 'repeat_hill'])
# journeys.append([repeated_climb(optimization_goal, repeated_steep_route.route, roads, repeats, True), 'steep_repeat'])
# journeys.append([repeated_anneal(annealing_route.route, roads, init_temp, repeats, False), 'repeated_simulated_annealing'])
plot_travels(journeys, optimization_goal, optimization_show)