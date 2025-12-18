import copy
import random as rnd
from typing import Callable

from logistics.types import RoadNetwork
from logistics.utils import plot_route
from solver.genetics.recombination.utils.scores import (
    random_recombination_score_method,
    ranked_recombination_score_method,
)
from solver.genetics.recombination.utils.styles import (
    crossover_recombination_style,
    order_recombination_style,
    partially_mapped_recombination_style,
)
from solver.genetics.types import RoutePopulation

RECOMBINATION_SCORE_FUNCTIONS: dict[str, Callable] = {
    "random": random_recombination_score_method,
    "rank": ranked_recombination_score_method,
}


RECOMBINATION_STYLE_FUNCTIONS: dict[str, Callable] = {
    "partially_mapped": partially_mapped_recombination_style,
    "order": order_recombination_style,
    "crossover": crossover_recombination_style,
}


def _run_recombination(routes, index, recombination_style_func):
    itin_length = len(routes[0].itinerary)
    parent_1 = (routes[index].get_full_itinerary(),)
    parent_2 = (routes[index + 1].get_full_intinerary(),)
    detour_1 = (rnd.randint(1, (itin_length // 2) - 1),)
    detour_2 = (rnd.randint((itin_length // 2) - 1, itin_length),)
    child_1_path = recombination_style_func(parent_1, parent_2, detour_1, detour_2)
    child_2_path = recombination_style_func(parent_2, parent_1, detour_1, detour_2)
    return (child_1_path, child_2_path)


def reproduce(
    population: RoutePopulation,
    road_network: RoadNetwork,
    recombination_score: str,
    reproducion_style: str,
) -> RoutePopulation:
    try:
        recombination_score_func: Callable = RECOMBINATION_SCORE_FUNCTIONS[recombination_score]
        recombination_style_func: Callable = RECOMBINATION_STYLE_FUNCTIONS[reproducion_style]
    except KeyError:
        raise
    sorted_population: RoutePopulation = recombination_score_func(population)
    offspring: RoutePopulation = copy.deepcopy(sorted_population)
    routes = copy.deepcopy(offspring.routes)
    for i in range(0, len(routes), 2):
        child_in_paths = _run_recombination(routes, i, recombination_style_func)
        offspring.routes[i].set_full_itinerary(child_in_paths[0])
        offspring.routes[i + 1].set_full_itinerary(child_in_paths[1])
    offspring.routes = [plot_route(road_network, route) for route in offspring.routes]
    return offspring
