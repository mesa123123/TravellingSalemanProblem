from random import randint


def partially_mapped_crossover(p1, p2, only_child=False):
    # cuts the parent genomes and switches the genes within the cuts
    # must make first cut at atleast 1 because otherwise swapping algorithm will not work
    first_cut = randint(1, len(p1)//2 - 1)
    second_cut = randint(len(p1)//2, len(p1))
    cut_genome = random_cut(p1, p2, first_cut, second_cut)
    # Work out any genes that have doubled up, in this context stop the children from visiting cities more than once
    c1 = [cut_genome[0][i] for i in range(0, len(cut_genome[0]))]
    c2 = [cut_genome[1][i] for i in range(0, len(cut_genome[1]))]
    # switch the genes outside the cuts for C1 so there are no repeated genes
    rearrange = True
    i = first_cut
    j = 0
    while(rearrange):
        if c1[i] == c1[j]:
            c1[j] = c2[i]
            i = first_cut
            j = 0
        else:
            j += 1
        if j == first_cut:
            j = second_cut
        if j == len(p1):
            i += 1
            j = 0
        if i == second_cut:
            rearrange = False
    # iron out kinks in C2 so there are no repeated genes
    rearrange = True
    i = first_cut
    j = 0
    while (rearrange):
        if c2[i] == c2[j]:
            c2[j] = c1[i]
            i = first_cut
            j = 0
        else:
            j += 1
        if j == first_cut:
            j = second_cut
        if j == len(p1):
            i += 1
            j = 0
        if i == second_cut:
            rearrange = False
    #If we want the parents to create one or two child genomes
    if only_child:
        return [0, c1]
    else:
        return [[0, c1],[0, c2]]


def order_crossover():
    pass


def cycle_crossover():
    pass


#function that allows the genes within the cut to switch over in their children
def random_cut(p1, p2, first_cut, second_cut):
    c1 = [0]*len(p1)
    c2 = [0]*len(p2)
    #Populate the children genomes through the crossover at two arbitrary points; perhaps we could arbitrary an
    # un-artbitrary these points?
    for i in range(first_cut, second_cut):
        c1[i] = p2[i]
        c2[i] = p1[i]
    for i in range(0,first_cut):
        c1[i] = p1[i]
        c2[i]= p2[i]
    for i in range(second_cut,len(p1)):
        c1[i] = p1[i]
        c2[i] = p2[i]
    return [c1, c2]


# these were used in testing purposes
# p1 = [1,3,2,6,4,5,7,9,8]
# p2 = [2,4,5,8,7,6,9,1,3]
#
# children = partially_mapped_crossover(p1, p2, False)
# print(children[0][1])
# print(children[1][1])
# children[0][1].sort()
# children[1][1].sort()
# print(children[0][1])
# print(children[1][1])