from typing import Optional

from numpy import ndarray
from numpy.random import default_rng

from src.logistics.types import Destination, Road, Road_Network, Route


def create_road_network(num_cities: int, road_length_limit: float) -> Road_Network:
    rnd = default_rng()
    city_weights: ndarray = rnd.uniform(low=1, high=road_length_limit, size=(num_cities, num_cities))
    route_network: Road_Network = [
        Road(departure_city=i + 1, arrival_city=j + 1, road_length=round(city_weights[i][j], 3))
        for i in range(num_cities + 1)
        for j in range(i + 1, num_cities + 1)
    ]
    return route_network


def plot_route(route: Optional[Route], all_roads: Road_Network) -> Route:
    if not route:
        rnd = default_rng()
        rnd_route = rnd.permutation(len(all_roads) + 1)
        destinations = [Destination(visit_number=i, current_city=rnd_route[i]) for i in range(len(all_roads))]

        route = Route(route_plot=destinations, route_score=-0.0)
    destinations: list[Destination] = sorted(route.route_plot, key=lambda d: d.visit_number)
    destinations[0].arrived_by_road = None
    for i in range(1, len(destinations)):
        city_B = destinations[i].current_city
        city_A = destinations[i - 1].current_city
        connecting_road: Optional[Road] = next(
            (road for road in all_roads if {road.departure_city, road.arrival_city} == {city_A, city_B}),
            None,
        )
        if not connecting_road:
            raise ValueError(f"There is a missing road in the route_network between city: {city_A} and city: {city_B}")
        destinations[i].arrived_by_road = connecting_road
    total_dist: float = sum([dest.arrived_by_road.road_length for dest in destinations])
    return Route(destinations, total_dist)


def get_best_swapped_route(route, roads) -> Route:
    best_route: Route = route
    while member := 0 < int(len(roads)) - 3:
        new_route: Route = route.copy()
        new_route[member].visit_number += 1
        new_route[member + 1].visit_number -= 1
        new_route_scored: Route = plot_route(new_route, roads)
        if new_route_scored.route_score < best_route.route_score:
            best_route = new_route_scored
        member += 1
    return best_route
