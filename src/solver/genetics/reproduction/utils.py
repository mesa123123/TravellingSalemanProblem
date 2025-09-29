    if style != "cycle":
        cut_genome = gene_switch(p1, p2, first_cut, second_cut)
        c1 = [cut_genome[0][i] for i in range(0, len(cut_genome[0]))]
        c2 = [cut_genome[1][i] for i in range(0, len(cut_genome[1]))]
    else:
        c1 = None
        c2 = None
    # Makes the cross-over based on the selected style of crossover
    children = style_selection(style, p1, p2, c1, c2, first_cut, second_cut)
    # If we want the parents to create one or two child genomes
    return children[0] if only_child else children


def style_selection(style, p1, p2, c1, c2, first_cut, second_cut):
    if style == "partially_mapped":
        child_1 = partially_mapped(c1, p1, first_cut, second_cut)
        child_2 = partially_mapped(c2, p2, first_cut, second_cut)
    elif style == "order":
        child_1 = order_crossover(c1, p1, first_cut, second_cut)
        child_2 = order_crossover(c2, p2, first_cut, second_cut)
    else:
        child_1 = cycle_crossover(list(p1), list(p2))
        child_2 = cycle_crossover(list(p2), list(p1))
    return [child_1, child_2]


def order_reproduction_style(population, road_network):
    pass


def partially_mapped_reproduction_style():
    pass


def crossover_reproduction_style():
    pass


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


def cycle_crossover(p1, p2):
    child = [0] * len(p1)
    cycle_list = list()
    cycle_list.append(p1[0])
    current_select = p1[0]
    cycle_list.append(p2[list.index(p1, current_select)])
    current_select = cycle_list[-1]
    while current_select != p1[0]:
        cycle_list.append(p2[list.index(p1, current_select)])
        current_select = cycle_list[-1]
    for i in range(0, len(cycle_list) - 1):
        index_of_interest = list.index(p1, cycle_list[i])
        child[index_of_interest] = p1[index_of_interest]
    for i in range(0, len(child)):
        if child[i] == 0:
            child[i] = p2[i]
    return [i for i in child]


# function that allows the genes within the cut to switch over in their children
def gene_switch(p1, p2, first_cut, second_cut):
    c1 = [0] * len(p1)
    c2 = [0] * len(p2)
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


def order_reproduction_style():
    pass


def partially_mapped_reproduction_style():
    pass


def crossover_reproduction_style():
    pass
