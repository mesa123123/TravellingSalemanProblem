from Tools.Random_Permutation import random_permutation

class Population:
    genes = None

    def __init__(self, gene_number, city_number):
        cities_model = [i for i in range(2, city_number+1)]
        blank_genes = [[0]*1 for i in range(0, gene_number)]
        for gene in blank_genes:
            gene.append(list(random_permutation(cities_model)))
        self.genes = blank_genes
