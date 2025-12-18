type InPath = dict[int, int]


def _switched_genes(parent: InPath, detour_1: int, detour_2: int) -> InPath:
    return {k: (v if detour_1 < k < detour_2 else 0) for k, v in parent.items()}


def order_recombination_style(parent_1: InPath, parent_2: InPath, detour_1: int, detour_2: int) -> InPath:
    swapped_genes = _switched_genes(parent_2, detour_1, detour_2)
    remaining_genes = [v for v in parent_1.values() if v not in swapped_genes.values()]
    return {k: (remaining_genes.pop() if k == 0 else v) for k, v in swapped_genes.items()}


def partially_mapped_recombination_style(parent_1: InPath, parent_2: InPath, detour_1: int, detour_2: int) -> InPath:
    swapped_genes = _switched_genes(parent_2, detour_1, detour_2)
    child_genes = {}
    # for k,v in swapped_genes.items():
    #     if v != 0:
    #         yield v
    #     # MARK: Look at the DEEBA KANNAN VIDEO ON THIS FOR THE PARTIAL MAP FUNCTION THERE IS A RECURSIVE WAY TO HANDLE
    #     # THIS ALGO
    #     else:
    #         if parent_1[k] in swapped_genes.values():
    #             parent_2[next((key for key, value in swapped_genes.items() if value == parent_1[k]), None)]
    pass


def crossover_recombination_style(parent_1: InPath, parent_2: InPath, detour_1: int, detour_2: int) -> InPath:
    swapped_genes = _switched_genes(parent_2, detour_1, detour_2)
    remaining_genes = {}
    pass


