import copy

from logistics.types import Route
from logistics.utils import plot_route


def get_best_swapped_route(route, roads) -> Route:
    best_route: Route = route
    while member := 0 < int(len(roads)) - 3:
        new_route: Route = copy.deepcopy(route)
        new_route[member].visit_number += 1
        new_route[member + 1].visit_number -= 1
        new_route_scored: Route = plot_route(new_route, roads)
        if new_route_scored.route_score < best_route.route_score:
            best_route: Route = new_route_scored
        member += 1
    return best_route
