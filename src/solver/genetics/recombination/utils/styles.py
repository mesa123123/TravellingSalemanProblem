from logistics.types import Itinerary


def _gene_switch(parent_1: Itinerary, parent_2: Itinerary, detour_1: int, detour_2: int) -> tuple[list[int], list[int]]:
    return (
        [
            parent_2[i].current_city
            if parent_2[i].visit_number > detour_1 or parent_2[i].visit_number < detour_2
            else 0
            for i in range(len(parent_1))
        ],
        [
            parent_1[i].current_city
            if parent_1[i].visit_number > detour_1 or parent_1[i].visit_number < detour_2
            else 0
            for i in range(len(parent_1))
        ],
    )


def order_recombination_style(
    parent_1: Itinerary, parent_2: Itinerary, detour_1: int, detour_2: int
) -> tuple[Itinerary, Itinerary]:
    child_1_swapped_cities, child_2_swapped = _gene_switch(parent_1, parent_2, detour_1, detour_2)
    child_1_remaining: list[int] = [
        parent_1[i].current_city for i in parent_1 if parent_1[i].current_city not in child_1_swapped_cities
    ]
    child_2_remaining: list[int] = [
        parent_2[i].current_city for i in parent_2 if parent_2[i].current_city not in child_2_swapped_cities
    ]


#     rearrange = True
#     i = second_cut
#     j = second_cut
#     while rearrange:
#         twin = False
#         for k in range(first_cut, second_cut):
#             if p[i] == c[k]:
#                 twin = True
#         if not twin:
#             c[j] = p[i]
#             j += 1
#             if j == len(p):
#                 j = 0
#         i += 1
#         if i == len(p):
#             i = 0
#         if i == second_cut:
#             rearrange = False
#     return c
#
#
def partially_mapped_recombination_style(
    parent_1: Itinerary, parent_2: Itinerary, detour_1: int, detour_2: int
) -> tuple[Itinerary, Itinerary]:
    child_1, child_2 = _gene_switch(parent_1, parent_2, detour_1, detour_2)
    pass


#     rearrange = True
#     i = first_cut
#     j = 0
#     while rearrange:
#         if c[i] == c[j]:
#             c[j] = p[i]
#             i = first_cut
#             j = 0
#         else:
#             j += 1
#         if j == first_cut:
#             j = second_cut
#         if j == len(c):
#             i += 1
#             j = 0
#         if i == second_cut:
#             rearrange = False
#     return c
#
#
def crossover_recombination_style(
    parent_1: Itinerary, parent_2: Itinerary, detour_1: int, detour_2: int
) -> tuple[Itinerary, Itinerary]:
    child_1, child_2 = _gene_switch(parent_1, parent_2, detour_1, detour_2)
    pass


#     child = [0] * len(p1)
#     cycle_list = list()
#     cycle_list.append(p1[0])
#     current_select = p1[0]
#     cycle_list.append(p2[list.index(p1, current_select)])
#     current_select = cycle_list[-1]
#     while current_select != p1[0]:
#         cycle_list.append(p2[list.index(p1, current_select)])
#         current_select = cycle_list[-1]
#     for i in range(0, len(cycle_list) - 1):
#         index_of_interest = list.index(p1, cycle_list[i])
#         child[index_of_interest] = p1[index_of_interest]
#     for i in range(0, len(child)):
#         if child[i] == 0:
#             child[i] = p2[i]
#     return [i for i in child]
#
#
