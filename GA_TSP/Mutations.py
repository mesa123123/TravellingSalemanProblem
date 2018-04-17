import random as rnd


def swap_mutation(gene, mutation_chance):
    mutate = rnd.random()
    if mutate < mutation_chance:
        cut1 = rnd.randint(0,len(gene)-2)
        cut2 = rnd.randint(cut1, len(gene)-1)
        temp = gene[cut2]
        gene[cut2] = gene[cut1]
        gene[cut1] = temp
    return gene


def insertion_mutation(gene, mutation_chance):
    mutate = rnd.random()
    if mutate < mutation_chance:
        cut1 = rnd.randint(0, len(gene)-3)
        cut2 = rnd.randint(cut1 + 1, len(gene)-1)
        temp = gene[cut2]
        for i in range(cut2, cut1+1, -1):
            gene[i] = gene[i-1]
        gene[cut1+1] = temp
    return gene


def displacement_mutation():
    pass


def scramble_mutation():
    pass


def inversion_mutation():
    pass