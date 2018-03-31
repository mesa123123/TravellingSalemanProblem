from GA_TSP.Score_Pop import score_pop
from GA_TSP.Crossover_functions.Path_Encoding import partially_mapped_crossover


def queen_bee(Population, roads):
    if not Population.scored:
        score_pop(Population, roads)
    queen_bee = Population.genes[0][1]
    for i in range(1, len(Population.genes)):
        Population[i] = [0, partially_mapped_crossover(queen_bee, Population.genes[i][1], True)]


def elite_nuclear_family(Population, roads):
    if not Population.scored:
        score_pop(Population, roads)
    for i in range(0, len(Population.genes), 2):
        children = partially_mapped_crossover(Population[i][1], Population[i+1][1])
        Population[i] = [0, children[0]]
        Population[i+1] = [0, children[1]]


def probabilistic_selection(Population, roads):
    pass