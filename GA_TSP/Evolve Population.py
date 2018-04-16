from Tools import Problem_Matrix
from GA_TSP.Breed import *
from GA_TSP.Score_Pop import score_pop
from GA_TSP.Population import Population
from Tools.See_Salesman import plot_travels

city_number = 50
longest_dist = 4
pop_size = 16
same_start = True
style = "order"
optimal_dist = city_number*(longest_dist//2)
generation = city_number*10
first_cut = 15
second_cut = 35
if pop_size%2 != 0:
    pop_size += 1
Person = Population(pop_size, city_number)
cities = Problem_Matrix.ProblemMatrix(city_number, longest_dist)
cities.make_matrix()
roads = cities.city_matrix
score_pop(Person, roads)
optimal_route = list()
optimal_route.append(Person.genes[0][0])
# for i in range(0, generation):
Person = rank_selection(Person, roads, first=first_cut, second=second_cut, style=style)
    # optimal_route.append(Person.genes[0][0])
journey = list()
journey.append([optimal_route, 'Genetic Algorithm PMX-NukeFam'])
plot_travels(journey, optimal_dist, True)
