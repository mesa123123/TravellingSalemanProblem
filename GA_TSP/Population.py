from Tools.Random_Permutation import random_permutation
from Tools.Problem_Matrix import ProblemMatrix
from GA_TSP.Score_Pop import score_pop

class Population:
    genes = None
    scored = None
    roads = None

    def __init__(self, gene_number, city_number):
         cities_model = [i for i in range(2, city_number+1)]
         blank_genes = [[0]*2 for i in range(0, gene_number)]
         for gene in blank_genes:
             gene[1] = random_permutation(cities_model)
         self.genes = blank_genes
         self.scored = False
