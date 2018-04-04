from Tools.Random_Permutation import random_permutation


class Population:
    gene_number = None
    city_number = None
    genes = None
    scored = None
    roads = None

    def __init__(self, gene_number, city_number, child=False):
        if gene_number % 2 != 0:
            gene_number += 1
        if not child:
            cities_model = [i for i in range(2, city_number+1)]
            blank_genes = [[0]*2 for i in range(0, gene_number)]
            for gene in blank_genes:
                gene[1] = random_permutation(cities_model)
        else:
            blank_genes = []
        self.gene_number = gene_number
        self.city_number = city_number
        self.genes = blank_genes
        self.scored = False
