type InPath = dict[int, int]


def _swapped_genes(parent: InPath, detour_1: int, detour_2: int) -> InPath:
    if detour_2 < detour_1:
        raise ValueError("detour_1_should_be_smaller_or_equal_to_detour_2")
    return {k: (v if detour_1 <= k <= detour_2 else 0) for k, v in parent.items()}


def order_recombination_style(parent_1: InPath, parent_2: InPath, detour_1: int, detour_2: int) -> InPath:
    swapped_genes: InPath = _swapped_genes(parent_2, detour_1, detour_2)
    remaining_genes: list[int] = [v for v in parent_1.values() if v not in swapped_genes.values()]
    full_genes: InPath = {k: (remaining_genes.pop(0) if v == 0 else v) for k, v in swapped_genes.items()}
    return full_genes


def partially_mapped_recombination_style(parent_1: InPath, parent_2: InPath, detour_1: int, detour_2: int) -> InPath:
    swapped_genes = _swapped_genes(parent_2, detour_1, detour_2)
    remaining_genes = [v for v in parent_1.values() if v not in swapped_genes.values()]
    return {k: (remaining_genes.pop() if k == 0 else v) for k, v in swapped_genes.items()}


def crossover_recombination_style(parent_1: InPath, parent_2: InPath, detour_1: int, detour_2: int) -> InPath:
    swapped_genes = _swapped_genes(parent_2, detour_1, detour_2)
    remaining_genes = {}
    pass
