from GA_TSP.Score_Pop import score_pop
from GA_TSP.Crossover_functions.Path_Encoding import partially_mapped_crossover

def queen_bee(Population, roads):
    if not Population.scored:
        score_pop(Population, roads)
    queen_bee = Population.genes[0][1]
    for i in range(1, len(Population.genes)):
        Population[i][1] = partially_mapped_crossover(queen_bee, Population.genes[i][1], True)

