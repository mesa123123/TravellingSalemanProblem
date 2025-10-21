import random as rnd
from math import exp

from logistics.types import RoadNetwork, Route
from logistics.utils import plot_route
from solver.climbs.swaps.interface import Swap, run_swap


def _anneal(anneal: bool, cost: float, temp: float) -> bool:
    return anneal and rnd.uniform(0, 1) < exp(abs(cost) / temp * 10)


def climber(
    target: float, route: Route, road_network: RoadNetwork, swap_func: Swap, temp: float, anneal: bool = False
) -> Route | tuple[Route, float]:
    new_route: Route = run_swap(route=route, road_network=road_network, swap=swap_func, target=target)
    cost = new_route.route_score - route.route_score
    route = new_route
    if temp > 0:
        if _anneal(anneal, cost, temp):
            return (route, temp)
        return climber(
            target=target, route=route, road_network=road_network, swap_func=swap_func, temp=temp - 1, anneal=anneal
        )
    return route


def repeat_climber(
    num_generations: int,
    target: float,
    road_network: RoadNetwork,
    swap_func: Swap,
    temp: float,
) -> list[Route]:
    story = []
    while num_generations > 0:
        next_route = climber(
            target=target, route=plot_route(road_network), road_network=road_network, swap_func=swap_func, temp=temp
        )
        story.append(next_route)
    return story


def simulated_annealing(target: float, route: Route, road_network: RoadNetwork, swap_func: Swap, temp: float):
    final_temp: float = temp / 10
    story: list[Route] = [route]
    while temp > final_temp:
        result = climber(
            target=target, route=route, road_network=road_network, swap_func=swap_func, temp=temp, anneal=True
        )
        if isinstance(result, tuple):
            story.append(result[0])
            temp = result[1]
        else:
            story.append(result)
            temp = 0.0
    return sorted(story, key=lambda x: x.route_score)[-1]


def repeat_anneal(
    num_generations: int,
    target: float,
    road_network: RoadNetwork,
    swap_func: Swap,
    temp: float,
) -> list[Route]:
    story = []
    while num_generations > 0:
        next_route = simulated_annealing(
            target=target,
            route=plot_route(road_network),
            road_network=road_network,
            swap_func=swap_func,
            temp=temp,
        )
        story.append(next_route)
    return story
