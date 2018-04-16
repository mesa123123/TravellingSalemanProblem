from random import randint


def partially_mapped_crossover(p1, p2, only_child=False, first=0, second=0):
    # cuts the parent genomes and switches the genes within the cuts
    # must make first cut at at least 1 because otherwise swapping algorithm will not work
    if first == 0 and second == 0:
        first_cut = randint(1, len(p1)//2 - 1)
        second_cut = randint(len(p1)//2, len(p1))
    else:
        first_cut = first
        second_cut = second
    cut_genome = gene_switch(p1, p2, first_cut, second_cut)
    c1 = [cut_genome[0][i] for i in range(0, len(cut_genome[0]))]
    c2 = [cut_genome[1][i] for i in range(0, len(cut_genome[1]))]
    # switch the genes outside the cuts for C1 so there are no repeated genes
    c1 = cryspr_map(c1, p1, first_cut, second_cut)
    c2 = cryspr_map(c2, p2, first_cut, second_cut)
    # If we want the parents to create one or two child genomes
    if only_child:
        return c1
    else:
        return [c1, c2]


# Implements an Order Crossover
def order_crossover(p1, p2, only_child=False, first=0, second=0):
    # cuts the parent genomes and switches the genes within the cuts
    # must make first cut at at least 1 because otherwise swapping algorithm will not work
    if first == 0 and second == 0:
        first_cut = randint(1, len(p1)//2 - 1)
        second_cut = randint(len(p1)//2, len(p1))
    else:
        first_cut = first
        second_cut = second
    cut_genome = gene_switch(p1, p2, first_cut, second_cut)
    # puts the swapped genes into children
    c1 = [cut_genome[0][i] for i in range(0, len(cut_genome[0]))]
    c2 = [cut_genome[1][i] for i in range(0, len(cut_genome[1]))]
    # switch over the remaining genes
    c1 = order_insert(c1, p1, first_cut, second_cut)
    c2 = order_insert(c2, p2, first_cut, second_cut)
    # If we want the parents to create one or two child genomes
    if only_child:
        return c1
    else:
        return [c1, c2]

def cycle_crossover():
    pass


# function that allows the genes within the cut to switch over in their children
def gene_switch(p1, p2, first_cut, second_cut):
    c1 = [0]*len(p1)
    c2 = [0]*len(p2)
    # Populate the children genomes through the crossover at two arbitrary points; perhaps we could arbitrary an
    # un-arbitrary these points?
    for i in range(first_cut, second_cut):
        c1[i] = p2[i]
        c2[i] = p1[i]
    for i in range(0, first_cut):
        c1[i] = p1[i]
        c2[i] = p2[i]
    for i in range(second_cut, len(p1)):
        c1[i] = p1[i]
        c2[i] = p2[i]
    return [c1, c2]


def cryspr_map(c, p, first_cut, second_cut):
    rearrange = True
    i = first_cut
    j = 0
    while rearrange:
        if c[i] == c[j]:
            c[j] = p[i]
            i = first_cut
            j = 0
        else:
            j += 1
        if j == first_cut:
            j = second_cut
        if j == len(c):
            i += 1
            j = 0
        if i == second_cut:
            rearrange = False
    return c


def order_insert(c, p, first_cut, second_cut):
    pass

# these were used in testing purposes
# p1 = [1,3,2,6,4,5,7,9,8]
# p2 = [2,4,5,8,7,6,9,1,3]
#
# children = partially_mapped_crossover(p1, p2, False)
# print(children[0])
# print(children[1])
# children[0].sort()
# children[1].sort()
# print(children[0])
# print(children[1])
