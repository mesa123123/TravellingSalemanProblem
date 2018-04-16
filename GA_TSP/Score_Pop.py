from Tools.Distance_check import distance_check
from GA_TSP.Population import Population

def score_pop(Population, roads):
    for gene in Population.genes:
        gene[0] = distance_check(gene[1], roads)
    # sorts the population
    Population.genes = sorted(Population.genes, key=lambda x: x[0])
    if not Population.scored:
        Population.scored = True
    return Population