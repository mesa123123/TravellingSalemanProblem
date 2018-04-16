from GA_TSP.Score_Pop import score_pop
from GA_TSP.Population import Population
from GA_TSP.Selection import selection

def create_result(city_number, paver, pop_size, crossover, parent, select):
    generation = city_number*20
    # if the cuts are set to 0 is means that there will be random cuts made for each crossover
    first_cut = 0 # city_number//4
    second_cut = 0 # (city_number*3)//4
    if pop_size%2 != 0:
        pop_size += 1
    Person = Population(pop_size, city_number)
    roads = paver.city_matrix
    score_pop(Person, roads)
    optimal_route = list()
    optimal_route.append(Person.genes[0][0])
    for i in range(0, generation):
        Person = selection(Person, roads, first_cut, second_cut, crossover, parent, select)
        optimal_route.append(Person.genes[0][0])
    return optimal_route
