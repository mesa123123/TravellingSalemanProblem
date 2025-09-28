from typing import Optional

from numpy import ndarray
from numpy.random import default_rng

from src.logistics.types import Road, Route, Route_Network


def create_route_network(num_cities: int, road_length_limit: float) -> Route_Network:
    rnd = default_rng()
    city_weights: ndarray = rnd.uniform(low=1, high=road_length_limit, size=(num_cities, num_cities))
    route_network: Route_Network = [
        Road(departure_city=i + 1, arrival_city=j + 1, road_length=round(city_weights[i][j], 3))
        for i in range(num_cities)
        for j in range(i + 1, num_cities)
    ]
    return route_network


def get_total_distance(route: Route) -> float:
    try:
        total_dist: float = sum([dest.arrived_by_road.road_length for dest in route])
    except ValueError:
        raise Exception("You've mucked up with the road lengths somewhere")
    return total_dist


def plot_route(route: Route, all_roads: Route_Network) -> Route:
    sorted_route: Route = sorted(route, key=lambda d: d.visit_number)
    sorted_route[0].arrived_by_road = None
    for i in range(1, len(sorted_route)):
        city_B = sorted_route[i].current_city
        city_A = sorted_route[i - 1].current_city
        connecting_road: Optional[Road] = next(
            (road for road in all_roads if {road.departure_city, road.arrival_city} == {city_A, city_B}),
            None,
        )
        if not connecting_road:
            raise ValueError(f"There is a missing road in the route_network between city: {city_A} and city: {city_B}")
        sorted_route[i].arrived_by_road = connecting_road
    return sorted_route


def get_best_swapped_route(route, roads) -> Route:
    current_record: float = get_total_distance(route)
    best_route: Route = route
    while member := 0 < int(len(roads)) - 3:
        new_route: Route = route.copy()
        new_route[member].visit_number += 1
        new_route[member + 1].visit_number -= 1
        new_distance: float = get_total_distance(plot_route(new_route, roads))
        if new_distance < current_record:
            current_record = new_distance
            best_route = new_route
        member += 1
    return best_route
