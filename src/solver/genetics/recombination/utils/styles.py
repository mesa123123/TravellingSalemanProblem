from itertools import islice

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


# MARK: Tests are failing here...
def _process_raw_gene_map(gene_map: dict[int, int]) -> dict[int, int]:
    new_gene_map = {k: (gene_map[v] if v in gene_map.keys() else v) for k, v in gene_map.items()}
    return new_gene_map if gene_map == new_gene_map else _process_raw_gene_map(new_gene_map)


def partially_mapped_recombination_style(parent_1: InPath, parent_2: InPath, detour_1: int, detour_2: int) -> InPath:
    swapped_genes = _swapped_genes(parent_2, detour_1, detour_2)
    genes_map: dict[int, int] = _process_raw_gene_map(
        {v2: v1 for v1, v2 in islice(zip(parent_1.values(), parent_2.values()), detour_1, detour_2)}
    )
    p1_remaining_values: list[int] = list(parent_1.values())
    remaining_genes_raw: list[int] = p1_remaining_values[:detour_1] + p1_remaining_values[detour_2:]
    remaining_genes = [genes_map[v] if v in genes_map.keys() else v for v in remaining_genes_raw]
    return {k: (remaining_genes.pop(0) if v == 0 else v) for k, v in swapped_genes.items()}


def crossover_recombination_style(parent_1: InPath, parent_2: InPath, detour_1: int, detour_2: int) -> InPath:
    swapped_genes = _swapped_genes(parent_2, detour_1, detour_2)
    remaining_genes = {}
    pass
