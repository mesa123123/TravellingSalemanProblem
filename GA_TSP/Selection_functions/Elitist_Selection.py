from GA_TSP.Selection_functions.Breed import *


#Takes the best half of the parents and the kids and selects them for the next generation
def nuclear_aristocracy(Population, roads, aging=False, first=0, second=0):
    child_genes = nuclear_family(Population, roads, first=first, second=second)
    output = list()
    if aging:
        for i in range(0, len(Population.genes)//2):
            output.append(Population.genes[i])
            output.append(child_genes.genes[i])
    else:
        for i in range(0,len(child_genes.genes)):
            output.append(child_genes.genes[i])
            output.append(Population.genes[i])
    output = sorted(output, key=lambda x: x[0])
    for i in range(0,len(Population.genes)):
        Population.genes[i] = output[i]
    return Population


def rank_selection(Population, roads, aging=False, first=0, second=0):
    pass