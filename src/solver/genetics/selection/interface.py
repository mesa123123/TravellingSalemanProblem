from typing import Callable

from logistics.types import Route
from solver.genetics.selection.utils import top_ten_both_generations, young_elitism
from solver.genetics.types import RoutePopulation

SELECTION_FUNCTIONS: dict[str, Callable] = {
    "young_elitism": young_elitism,
    "top_ten_both_generations": top_ten_both_generations,
    "children_only": lambda x, y: y,
}


def _score_routes(routes: list[Route]) -> list[Route]:
    return sorted(routes, key=lambda x: x.route_score)


def selection(
    parent_population: RoutePopulation, children_population: RoutePopulation, selection: str
) -> RoutePopulation:
    try:
        selection_func: Callable = SELECTION_FUNCTIONS[selection]
    except KeyError:
        raise
    parent_population.routes = _score_routes(parent_population.routes)
    children_population.routes = _score_routes(children_population.routes)
    return selection_func(parent_population, children_population)
