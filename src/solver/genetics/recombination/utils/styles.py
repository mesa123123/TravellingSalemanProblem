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


# MARK: This is causing problems. Might have to get some things sorted with pytest_kedge
def partially_mapped_recombination_style(parent_1: InPath, parent_2: InPath, detour_1: int, detour_2: int) -> InPath:
    p1_vals = list(parent_1.values())
    p2_vals = list(parent_2.values())
    genes_map = dict(zip(p2_vals[detour_1:detour_2], p1_vals[detour_1:detour_2]))

    def resolve_full(d):
        final_res = {}
        for k in d:
            curr = d[k]
            visited = {k}  # Track to prevent infinite hang
            while curr in d:
                if curr in visited:
                    break
                visited.add(curr)
                curr = d[curr]
            final_res[k] = curr
        return final_res

    final_map = resolve_full(genes_map)
    remaining_genes_raw = p1_vals[:detour_1] + p1_vals[detour_2:]
    remaining_genes = [final_map.get(v, v) for v in remaining_genes_raw]
    swapped_genes = _swapped_genes(parent_2, detour_1, detour_2)
    return {k: (remaining_genes.pop(0) if v == 0 else v) for k, v in swapped_genes.items()}


def crossover_recombination_style(parent_1: InPath, parent_2: InPath, detour_1: int, detour_2: int) -> InPath:
    swapped_genes = _swapped_genes(parent_2, detour_1, detour_2)
    remaining_genes = {}
    pass
