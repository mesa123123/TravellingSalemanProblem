from random import randint


def gene_crossover(p1, p2, only_child=False, first=0, second=0, style="partially_mapped"):
    # determines where the cuts in the genomes will be
    # first cut has to be more than 0, and second cut has to be less than length-1
    if first == 0 and second == 0:
        first_cut = randint(1, len(p1)//2 - 1)
        second_cut = randint(len(p1)//2, len(p1)-1)
    else:
        first_cut = first
        second_cut = second
    # makes the cut and swaps the genes
    cut_genome = gene_switch(p1, p2, first_cut, second_cut)
    c1 = [cut_genome[0][i] for i in range(0, len(cut_genome[0]))]
    c2 = [cut_genome[1][i] for i in range(0, len(cut_genome[1]))]
    # makes the crossover
    if style == "partially_mapped":
        c1 = partially_mapped(c1, p1, first_cut, second_cut)
        c2 = partially_mapped(c2, p2, first_cut, second_cut)
    elif style == "order":
        c1 = order_crossover(c1, p1, first_cut, second_cut)
        c2 = order_crossover(c2, p2, first_cut, second_cut)
    # If we want the parents to create one or two child genomes
    if only_child:
        return c1
    else:
        return [c1, c2]


# Completes a partially mapped crossover
def partially_mapped(c, p, first_cut, second_cut):
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


# Implements an Order Crossover
def order_crossover(c, p, first_cut, second_cut):
    rearrange = True
    i = second_cut
    j = second_cut
    while rearrange:
        twin = False
        for k in range(first_cut, second_cut):
            if p[i] == c[k]:
                twin = True
        if not twin:
            c[j] = p[i]
            j += 1
            if j == len(p):
                j = 0
        i += 1
        if i == len(p):
                i = 0
        if i == second_cut:
            rearrange = False
    return c


def cycle_crossover(c, p, first_cut, second_cut):
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


# these were used in testing purposes
# p1 = [1,3,2,6,4,5,7,9,8]
# p2 = [2,4,5,8,7,6,9,1,3]
#
# children = gene_crossover(p1, p2, first=2, second=6, style="order")
# print(p1, " p1")
# print(p2, " p2")
# print(children[0], " c1")
# print(children[1], " c2")
# children[0].sort()
# children[1].sort()
# print(children[0])
# print(children[1])
