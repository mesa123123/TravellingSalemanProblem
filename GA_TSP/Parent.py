from GA_TSP.Score_Pop import score_pop
from GA_TSP.Population import Population
from GA_TSP.Path_Crossover import gene_crossover
import random as rnd


def rank(population, roads, first, second, style):
    if not population.scored:
        score_pop(population, roads)
    ranked_generation = list()
    child_generation = Population(population.gene_number, population.city_number)
    p1 = list()
    p2 = list()
    # ranks the children based on population size
    prize_money = len(population.genes)
    for i in range(0, len(population.genes)):
        ranked_generation.append([prize_money, population.genes[i][0], population.genes[i][1]])
        prize_money += len(population.genes) - (i+1)
    # selects the parents based upon these ranks
    for j in range(0, len(population.genes)):
        parent_choice_1 = rnd.randint(len(population.genes), prize_money)
        parent_choice_2 = rnd.randint(len(population.genes), prize_money)
        for k in range(0,len(ranked_generation)):
            if parent_choice_1 >= ranked_generation[k][0]:
                p1 = ranked_generation[k-1][2]
            if parent_choice_2 >= ranked_generation[k][0]:
                p2 = ranked_generation[k-1][2]
                # stops the parents being the same gene
                if p1 == p2:
                    if len(ranked_generation[k-2]) > 0:
                        p2 = ranked_generation[k-2][2]
                    else:
                        p2 = ranked_generation[k][2]
        # adds it to the child generation
        child_generation.genes[j] = [0, tuple(gene_crossover(p1, p2, only_child=True, first=first, second=second, style=style))]
    return score_pop(child_generation, roads)


#Takes the parents of the previous generation, shuffles them and simply breeds two children in their place
def random(Parent_Pop, roads, first=0, second=0, style="partially_mapped"):
    if not Parent_Pop.scored:
        score_pop(Parent_Pop, roads)
    rnd.shuffle(Parent_Pop.genes)
    child_generation = Population(Parent_Pop.gene_number, Parent_Pop.city_number)
    for i in range(0, len(Parent_Pop.genes), 2):
        children = gene_crossover(Parent_Pop.genes[i][1], Parent_Pop.genes[i+1][1], first=first, second=second, style=style)
        child_generation.genes[i] = ([0, tuple(children[0])])
        child_generation.genes[i+1] = ([0, tuple(children[1])])
    return score_pop(child_generation, roads)
