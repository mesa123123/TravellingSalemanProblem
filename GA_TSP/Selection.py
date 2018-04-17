from GA_TSP.Parent import *
from GA_TSP.Mutations import *


# Takes the top 10 from both generations and creates a new generation from the both; if aging is on it takes the
# top 10 of both
def selection(population, roads, style="partially mapped", parent="random", selection="on_fitness", mutation=None,
              mutation_chance=0.1):
    # create child genes
    if parent == "rank":
        child_genes = rank(population, roads, style=style)
    else:
        child_genes = random(population, roads, style=style)
    # implement selection algorithm to create new generation
    if selection == "elitism":
        output = elitism(population, child_genes)
    else:
        output = on_fitness(population, child_genes)
    # sort it and return it
    output = sorted(output, key=lambda x: x[0])
    if mutation != None:
        for gene in output:
            gene[1] = insertion_mutation(list(gene[1]), mutation_chance)
    for i in range(0,len(population.genes)):
        population.genes[i] = output[i]
    return population


# keeps the best of parents and then adds all of the children except the worst
def elitism(population, child_genes):
    output = list()
    output.append(population.genes[0])
    for i in range(0, len(population.genes)-1):
        output.append(child_genes.genes[i])
    return output


# Returns the top 10 of either the children and the parents or just returns the children
def on_fitness(parent_pop, child_pop, aging=False):
    output = list()
    if aging:
        for i in range(0, len(parent_pop.genes)//2):
            output.append(child_pop.genes[i])
            output.append(child_pop.genes[i])
    else:
        for i in range(0,len(child_pop.genes)):
            output.append(child_pop.genes[i])
            output.append(parent_pop.genes[i])
    return output