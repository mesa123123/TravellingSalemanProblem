
# keeps the best of parents and then adds all of the children except the worst
def elitism(population, child_genes):
    output = list()
    output.append(population.genes[0])
    for i in range(0, len(population.genes) - 1):
        output.append(child_genes.genes[i])
    return output


# Returns the top 10 of either the children and the parents or just returns the children
def on_fitness(parent_pop, child_pop, aging=False):
    output = list()
    if aging:
        for i in range(0, len(parent_pop.genes) // 2):
            output.append(child_pop.genes[i])
            output.append(child_pop.genes[i])
    else:
        for i in range(0, len(child_pop.genes)):
            output.append(child_pop.genes[i])
            output.append(parent_pop.genes[i])
    return output

