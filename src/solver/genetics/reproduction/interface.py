import copy
import random as rnd
from enum import StrEnum
from typing import Callable, List, TypeVar

from logistics.types import Road, RoadNetwork
from logistics.utils import plot_route
from solver.genetics.reproduction.utils import (
    crossover_reproduction_style,
    order_reproduction_style,
    partially_mapped_reproduction_style,
)
from solver.genetics.types import RoutePopulation
from solver.genetics.utils import sort_population_by_random, sort_population_by_route_score

T = TypeVar("T", bound=List)


class ReproductionStyle(StrEnum):
    PARTIALLY_MAPPED = "partially_mapped"
    ORDER = "order"
    CROSSOVER = "crossover"


class ReproductionMethod(StrEnum):
    RANK = "rank"
    RANDOM = "random"


REPRODUCTION_METHOD_FUNCTIONS: dict[ReproductionMethod, Callable] = {
    ReproductionMethod.RANK: sort_population_by_route_score,
    ReproductionMethod.RANDOM: sort_population_by_random,
}


REPRODUCTION_STYLE_FUNCTIONS: dict[ReproductionStyle, Callable] = {
    ReproductionStyle.PARTIALLY_MAPPED: partially_mapped_reproduction_style,
    ReproductionStyle.ORDER: order_reproduction_style,
    ReproductionStyle.CROSSOVER: crossover_reproduction_style,
}


def reproduce(
    population: RoutePopulation,
    next_generation_population: RoutePopulation,
    road_network: RoadNetwork,
    selection: ReproductionMethod,
    style: ReproductionStyle = "partially_mapped",
) -> RoutePopulation:
    reproduction_method_func = REPRODUCTION_METHOD_FUNCTIONS.get(selection)
    reproduction_style_func = REPRODUCTION_STYLE_FUNCTIONS.get(selection)
    reproduction_method_func(population)
    offspring = copy.deepcopy(population)
    for route in offspring.routes:
        route_halfway: int = len(route.itinerary) // 2
        first_detour: int = rnd.randint(1, route_halfway - 1)
        second_detour: int = rnd.randint(route_halfway - 1, len(route.itinerary))
        new_itinerary: list[Road] = reproduction_style_func(route, road_network, first_detour, second_detour)
        route.itinerary = new_itinerary
    offspring.routes = [plot_route(road_network, route) for route in offspring.routes]
    return offspring
