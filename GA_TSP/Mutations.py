import random as rnd


def swap_mutation(gene, mutation_chance):
    mutate = rnd.random()
    if mutate < mutation_chance:
        cut1 = rnd.randint(0, len(gene)-2)
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


def scramble_mutation(gene, mutation_chance):
    mutate = rnd.random()
    if mutate < mutation_chance:
        cut1 = rnd.randint(0, len(gene)-2)
        cut2 = rnd.randint(cut1, len(gene)-1)
        scramble = list()
        for i in range(cut1, cut2):
            scramble.append(gene[i])
        rnd.shuffle(scramble)
        for i in range(cut1, cut2):
            gene[i] = scramble[i-cut1]
    return gene


def inversion_mutation(gene, mutation_chance):
    mutate = rnd.random()
    if mutate < mutation_chance:
        cut1 = rnd.randint(0, len(gene)-2)
        cut2 = rnd.randint(cut1, len(gene)-1)
        inverse = list()
        for i in range(cut1, cut2):
            inverse.append(gene[i])
        inverse.reverse()
        for i in range(cut1, cut2):
            gene[i] = inverse[i-cut1]
    return gene


def displacement_mutation(gene, mutation_chance):
    mutate = rnd.random()
    if mutate < mutation_chance:
        cut1 = rnd.randint(0, len(gene)-2)
        cut2 = rnd.randint(cut1, len(gene)-1)
        displaced_range = list()
        outside_range = list()
        output_gene = list()
        for i in range(cut1, cut2):
            displaced_range.append(gene[i])
        for j in range(0, cut1):
            outside_range.append(gene[j])
        for k in range(cut2, len(gene)):
            outside_range.append(gene[k])
        insert_index = rnd.randint(0, len(outside_range))
        for l in range(0, insert_index):
            output_gene.append(outside_range[l])
        for m in range(0, len(displaced_range)):
            output_gene.append(displaced_range[m])
        for n in range(insert_index, len(outside_range)):
            output_gene.append(outside_range[n])
        for p in range(0, len(gene)):
            gene[p] = output_gene[p]
    return gene
