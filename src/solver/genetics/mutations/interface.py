import copy
import random as rnd
from typing import Callable

from logistics.types import RoadNetwork, Route
from logistics.utils import plot_route
from solver.genetics.mutations.utils import (
    displacement_mutation,
    insertion_mutation,
    inversion_mutation,
    scramble_mutation,
    swap_mutation,
)

MUTATION_FUNCTIONS: dict[str, Callable] = {
    "swap": swap_mutation,
    "insert": insertion_mutation,
    "scramble": scramble_mutation,
    "inversion": inversion_mutation,
    "displacement": displacement_mutation,
}


def mutate(route: Route, road_network: RoadNetwork, mutation: str, mutation_chance: int = 50) -> Route:
    mutate: int = rnd.randint(0, 100)
    try:
        mutation_func: Callable | None = MUTATION_FUNCTIONS.get(mutation)
    except KeyError:
        raise
    if mutate <= mutation_chance and mutation_func:
        mutated_route: Route = copy.deepcopy(route)
        mutation_map: dict[int, int] = mutation_func(len(route.itinerary))
        for dest in mutated_route.itinerary:
            dest.visit_number = mutation_map[dest.visit_number]
        return plot_route(road_network, mutation_func(mutated_route))
    return route
