import random as rnd


def swap_mutation(length: int) -> dict[int, int]:
    old_order = list(range(length))
    pivot: int = rnd.randint(1, length - 2)
    new_order = [index - pivot if index <= pivot else index + pivot for index in old_order]
    swap_map: dict[int, int] = dict(zip(old_order, new_order))
    return swap_map


def insertion_mutation(length: int) -> dict[int, int]:
    old_order = list(range(length))
    move_to = rnd.randint(0, length - 1)
    move_from = rnd.randint(0, length - 1)
    while move_to == move_from:
        move_from = rnd.randint(0, length - 1)
    new_order: list[int] = [
        move_to if v == move_from else v + 1 if v >= move_to and v < move_from else v for v in old_order
    ]
    insertion_map: dict[int, int] = dict(zip(old_order, new_order))
    return insertion_map


def scramble_mutation(length: int) -> dict[int, int]:
    lower = rnd.randint(0, length - 2)
    upper = rnd.randint(lower + 1, length - 1)
    original_range: list[int] = list(range(lower, upper))
    new_range = original_range.copy()
    rnd.shuffle(new_range)
    scramble_map = dict(zip(original_range, new_range))
    return scramble_map


def inversion_mutation(length: int) -> dict[int, int]:
    lower = rnd.randint(0, length - 2)
    upper = rnd.randint(lower + 1, length - 1)
    original_range: list[int] = list(range(lower, upper))
    new_range = original_range.copy()
    new_range.reverse()
    invert_map = dict(zip(original_range, new_range))
    return invert_map


def displacement_mutation(length: int) -> dict[int, int]:
    itinerary: list[int] = list(range(length))
    lower: int = rnd.randint(0, length - 2)
    upper: int = rnd.randint(lower + 1, length - 1)
    land: int = rnd.randint(0, len(itinerary) - len(range(lower, upper)))
    block_to_move: list[int] = itinerary[lower:upper]
    outside_range: list[int] = itinerary[:lower] + itinerary[upper:]
    new_itinerary: list[int] = outside_range[:land] + block_to_move + outside_range[land:]
    displacement_map: dict[int, int] = dict(zip(itinerary, new_itinerary))
    return displacement_map
