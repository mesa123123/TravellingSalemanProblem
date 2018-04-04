from GA_TSP.Selection_functions.Next_Generation import *

def nuclear_aristocracy(Population, roads, aging=False):
    child_genes = nuclear_family(Population, roads)
    output = list()
    if aging:
        for i in range(0, len(Population.genes)):
            output[i] = Population.genes[i][1]
            output[i*2] = child_genes.genes[i][1]

    else:
        output.append([child_genes.genes[i] for i in range(0, len(child_genes.genes))])
        output.append([Population.genes[i] for i in range(0, len(Population.genes))])
    output = output[0]
    for i in output:
        print(i[0])
    print('----------------------------------------------------------------------------')
    output = sorted(output, key=lambda x: x[0])
    Population.genes = [output[i] for i in range(0, len(Population.genes))]
    return Population