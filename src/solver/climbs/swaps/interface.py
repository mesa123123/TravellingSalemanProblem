from enum import StrEnum
from typing import Callable

from logistics.types import RoadNetwork, Route
from solver.climbs.swaps.utils import get_best_nearest_neighbour_swap, get_good_enough_nearest_neighbour_swap


class Swap(StrEnum):
    BEST_NEIGHBOUR = "best_neighbour"
    GOOD_ENOUGH_NEIGHBOUR = "good_enough_neighbour"


SWAP_FUNCTIONS: dict[Swap, Callable] = {
    Swap.BEST_NEIGHBOUR: get_best_nearest_neighbour_swap,
    Swap.GOOD_ENOUGH_NEIGHBOUR: get_good_enough_nearest_neighbour_swap,
}


def run_swap(route: Route, road_network: RoadNetwork, swap: Swap, target: float) -> Route:
    swap_func: Callable | None = SWAP_FUNCTIONS.get(swap)
    if swap_func:
        return swap_func(target, route, road_network)
    return route
