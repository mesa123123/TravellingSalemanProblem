import copy
import random as rnd
from enum import StrEnum
from typing import Callable, List, TypeVar

from logistics.types import RoadNetwork, Route
from logistics.utils import plot_route
from solver.genetics.mutations.utils import (
    displacement_mutation,
    insertion_mutation,
    inversion_mutation,
    scramble_mutation,
    swap_mutation,
)

T = TypeVar("T", bound=List)


class Mutation(StrEnum):
    SWAP = "swap"
    INSERT = "insert"
    SCRAMBLE = "scramble"
    INVERSION = "inversion"
    DISPLACEMENT = "displacement"


MUTATION_FUNCTIONS: dict[Mutation, Callable[[T, float], T]] = {
    Mutation.SWAP: swap_mutation,
    Mutation.INSERT: insertion_mutation,
    Mutation.SCRAMBLE: scramble_mutation,
    Mutation.INVERSION: inversion_mutation,
    Mutation.DISPLACEMENT: displacement_mutation,
}


def mutate(route: Route, road_network: RoadNetwork, mutation: Mutation, mutation_chance: int = 50) -> Route:
    mutate: int = rnd.randint(0, 100)
    mutation_func: Callable[[T, float], T] | None = MUTATION_FUNCTIONS.get(mutation)
    if mutate <= mutation_chance and mutation_func:
        mutated_route: Route = copy.deepcopy(route)
        mutation_map: dict[int, int] = mutation_func(len(route.itinerary))
        for dest in mutated_route.itinerary:
            dest.visit_number = mutation_map[dest.visit_number]
        return plot_route(road_network, mutation_func(mutated_route))
    return route
