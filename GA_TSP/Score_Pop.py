from Tools.Distance_check import distance_check

def score_pop(Population, roads):
    for gene in Population.genes:
        gene[0] = distance_check(gene[1], roads)
    Population.genes = sorted(Population.genes, key=lambda x: x[0])
    if not Population.scored:
        Population.scored = True