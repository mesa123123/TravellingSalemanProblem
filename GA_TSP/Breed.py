from GA_TSP.Score_Pop import score_pop
from GA_TSP.Population import Population
from GA_TSP.Path_Crossover import gene_crossover
import random


def rank_selection(population, roads, first, second, style):
    if not population.scored:
        score_pop(population, roads)
    ranked_generation = list()
    child_generation = Population(population.gene_number, population.city_number)
    p1 = list()
    p2 = list()
    prize_money = len(population.genes)
    for i in range(0, len(population.genes)):
        ranked_generation.append([prize_money, population.genes[i][0], population.genes[i][1]])
        prize_money += len(population.genes) - (i+1)
    for j in range(0, len(population.genes)):
        parent_choice_1 = random.randint(len(population.genes), prize_money)
        parent_choice_2 = random.randint(len(population.genes), prize_money)
        for k in range(0,len(ranked_generation)):
            if parent_choice_1 >= ranked_generation[k][0]:
                p1 = ranked_generation[k-1][2]
            if parent_choice_2 >= ranked_generation[k][0]:
                p2 = ranked_generation[k-1][2]
                if p1 == p2:
                    if len(ranked_generation[k-2]) > 0:
                        p2 = ranked_generation[k-2][2]
                    else:
                        p2 = ranked_generation[k][2]
        if(len(p1) == 0):
            print(parent_choice_1)
        child_generation.genes[j] = [0, tuple(gene_crossover(p1, p2, only_child=True, first=first, second=second, style=style))]
    return score_pop(child_generation, roads)


# this allows the best algorithm to share its traits with the rest of the population, and allows the best of the
# population to continue onward to the next generation
def queen_bee(Population, roads):
    if not Population.scored:
        score_pop(Population, roads)
    queen_bee = Population.genes[0][1]
    for i in range(1, len(Population.genes)):
        Population.genes[i] = [0, tuple(gene_crossover(queen_bee, Population.genes[i][1], True))]

#Takes the top 10 of each generation:
#Takes the best half of the parents and the kids and selects them for the next generation
def nuclear_aristocracy(population, roads, aging=False, first=0, second=0, style="partially mapped"):
    child_genes = __random_breed(population, roads, first=first, second=second, style=style)
    output = list()
    if aging:
        for i in range(0, len(population.genes)//2):
            output.append(population.genes[i])
            output.append(child_genes.genes[i])
    else:
        for i in range(0,len(child_genes.genes)):
            output.append(child_genes.genes[i])
            output.append(population.genes[i])
    output = sorted(output, key=lambda x: x[0])
    for i in range(0,len(population.genes)):
        population.genes[i] = output[i]
    return population


#Takes the parents of the previous generation, shuffles them and simply breeds two children in their place
def __random_breed(Parent_Pop, roads, first=0, second=0, style="partially_mapped"):
    if not Parent_Pop.scored:
        score_pop(Parent_Pop, roads)
    random.shuffle(Parent_Pop.genes)
    child_generation = Population(Parent_Pop.gene_number, Parent_Pop.city_number)
    for i in range(0, len(Parent_Pop.genes), 2):
        children = gene_crossover(Parent_Pop.genes[i][1], Parent_Pop.genes[i+1][1], first=first, second=second, style=style)
        child_generation.genes[i] = ([0, tuple(children[0])])
        child_generation.genes[i+1] = ([0, tuple(children[1])])
    return score_pop(child_generation, roads)
