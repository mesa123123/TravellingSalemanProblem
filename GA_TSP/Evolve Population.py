from Tools import Problem_Matrix
from GA_TSP.Selection_functions.Elitist import queen_bee
from GA_TSP.Score_Pop import score_pop
from GA_TSP.Population import Population


Person = Population(8, 10)
cities = Problem_Matrix.ProblemMatrix(10, 3)
cities.make_matrix()
roads = cities.city_matrix
score_pop(Person, roads)
print(Person.genes)
print('---------------------------------------------------------------------------')
queen_bee(Person, roads)
print(Person.genes)