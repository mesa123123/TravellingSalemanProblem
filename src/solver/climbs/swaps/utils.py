import copy

from logistics.types import RoadNetwork, Route
from logistics.utils import plot_route


def get_best_nearest_neighbour_swap(target: float, route: Route, road_network: RoadNetwork) -> Route:
    del target
    best_route: Route = route
    while member := 0 < int(len(route.itinerary)) - 3:
        new_route: Route = copy.deepcopy(route)
        new_route.itinerary[member].visit_number += 1
        new_route.itinerary[member + 1].visit_number -= 1
        new_route_scored: Route = plot_route(road_network, new_route)
        if new_route_scored.route_score < best_route.route_score:
            best_route: Route = new_route_scored
        member += 1
    return best_route


def get_good_enough_nearest_neighbour_swap(target: float, route: Route, road_network: RoadNetwork) -> Route:
    while member := 0 < int(len(road_network)) - 3:
        new_route: Route = copy.deepcopy(route)
        new_route.itinerary[member].visit_number += 1
        new_route.itinerary[member + 1].visit_number -= 1
        new_route_scored: Route = plot_route(road_network, new_route)
        if new_route_scored.route_score <= target:
            return new_route
    return route
