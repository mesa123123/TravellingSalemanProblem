from random import shuffle
from typing import Optional


class Population:
    gene_number: Optional[int] = None
    city_number: Optional[int] = None
    genes: list[list[int | None]] = [[], []]
    scored: bool = False
    roads = None

    def __init__(self, gene_number, city_number, child=False):
        if gene_number % 2 != 0:
            gene_number += 1
        if not child:
            cities_model = [i for i in range(2, city_number + 1)]
            blank_genes = [[0] * 2 for i in range(0, gene_number)]
            for gene in blank_genes:
                copied_cities = cities_model.copy()
                gene[1] = shuffle(copied_cities)
        else:
            blank_genes = []
        self.gene_number = gene_number
        self.city_number = city_number
        self.genes = blank_genes
        self.scored = False
