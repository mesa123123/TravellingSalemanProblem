from GA_TSP.Score_Pop import score_pop
from GA_TSP.Population import Population
from GA_TSP.Crossover_functions.Path_Encoding import partially_mapped_crossover
import random

# this allows the best algorithm to share its traits with the rest of the population, and allows the best of the
# population to continue onward to the next generation
def queen_bee(Population, roads):
    if not Population.scored:
        score_pop(Population, roads)
    queen_bee = Population.genes[0][1]
    for i in range(1, len(Population.genes)):
        Population.genes[i] = [0, tuple(partially_mapped_crossover(queen_bee, Population.genes[i][1], True))]

# takes the parents of the previous generation and simply breeds two children in their place
def nuclear_family(Parent_Pop, roads):
    if not Parent_Pop.scored:
        score_pop(Parent_Pop, roads)
    random.shuffle(Parent_Pop.genes)
    child_generation = Population(Parent_Pop.gene_number, Parent_Pop.city_number)
    for i in range(0, len(Parent_Pop.genes), 2):
        children = partially_mapped_crossover(Parent_Pop.genes[i][1], Parent_Pop.genes[i+1][1])
        child_generation.genes[i] = ([0, tuple(children[0])])
        child_generation.genes[i+1] = ([0, tuple(children[1])])
    return score_pop(child_generation, roads)


def probabilistic_selection(Population, roads):
    pass

