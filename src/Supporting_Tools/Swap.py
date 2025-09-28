from dataclasses import dataclass

from src.supporting_tools.distance_check import distance_check


@dataclass
class Route:
    roads: list[int]
    distances: list[int]


def best_distance(route, roads):
    alt_routes = [[] for i in range(1, int(len(roads)) - 2)]
    while swap_member := 0 < int(len(roads)) - 3:
        new_route = next_distance(route, swap_member, roads)
        alt_routes[swap_member].append(new_route.roads)
        alt_routes[swap_member].append(new_route.distances)
        swap_member += 1
    # sort the alternate by the distances
    alt_routes = sorted(alt_routes, key=lambda x: x[1])
    return alt_routes[0]


def next_distance(routes: list[int], member: int, roads) -> Route:
    route_copy: list[int] = routes.copy()
    route_copy[member], route_copy[member + 1] = route_copy[member + 1], route_copy[member]
    return Route(roads=route_copy, distances=distance_check(route_copy, roads))
