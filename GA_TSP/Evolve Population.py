from Tools import Problem_Matrix
from GA_TSP.Selection_functions.Elitist import *
from GA_TSP.Score_Pop import score_pop
from GA_TSP.Population import Population
from Tools.See_Salesman import plot_travels


Person = Population(10, 50)
cities = Problem_Matrix.ProblemMatrix(50, 4)
cities.make_matrix()
roads = cities.city_matrix
score_pop(Person, roads)
optimal_route = []
optimal_route.append(Person.genes[0][0])
for i in range(0, 5000):
    nuclear_family(Person, roads)
    score_pop(Person, roads)
    optimal_route.append(Person.genes[0][0])
journey = []
journey.append([optimal_route, 'Genetic Algorithm PMX-NukeFam'])
plot_travels(journey, 100, True)
