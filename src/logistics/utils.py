from typing import Optional

from numpy import ndarray
from numpy.random import default_rng

from src.logistics.types import Destination, Road, RoadNetwork, Route, RoutePopulation


def create_road_network(num_cities: int, road_length_limit: float) -> RoadNetwork:
    rnd = default_rng()
    city_weights: ndarray = rnd.uniform(low=1, high=road_length_limit, size=(num_cities, num_cities))
    route_network: RoadNetwork = [
        Road(departure_city=i + 1, arrival_city=j + 1, road_length=round(city_weights[i][j], 3))
        for i in range(num_cities + 1)
        for j in range(i + 1, num_cities + 1)
    ]
    return route_network


def create_route(road_network: RoadNetwork) -> Route:
    rnd = default_rng()
    rnd_route = rnd.permutation(len(road_network) + 1)
    destinations = [Destination(visit_number=i, current_city=rnd_route[i]) for i in range(len(road_network))]
    return Route(itinerary=destinations, route_score=-0.0)


def _score_distances(destinations: list[Destination], road_network: RoadNetwork) -> list[Destination]:
    destinations[0].arrived_by_road = None
    for i in range(1, len(destinations)):
        city_B: int = destinations[i].current_city
        city_A: int = destinations[i - 1].current_city
        connecting_road: Optional[Road] = next(
            (road for road in road_network if {road.departure_city, road.arrival_city} == {city_A, city_B}),
            None,
        )
        if not connecting_road:
            raise ValueError(f"There is a missing road in the route_network between city: {city_A} and city: {city_B}")
        destinations[i].arrived_by_road = connecting_road
    return destinations


def plot_route(road_network: RoadNetwork, route: Optional[Route] = None) -> Route:
    route: Route = route if route else create_route(road_network)
    destinations: list[Destination] = sorted(route.itinerary, key=lambda d: d.visit_number)
    destinations: list[Destination] = _score_distances(destinations, road_network)
    total_dist: float = sum([dest.arrived_by_road.road_length for dest in destinations])
    return Route(destinations, total_dist)

def create_route_population(population_size: int, road_network: RoadNetwork) -> RoutePopulation:
    pop: RoutePopulation = RoutePopulation(
        population_size=population_size,
        num_of_cities=len(road_network),
        routes=[plot_route(road_network) for i in range(population_size)],
    )
    pop.routes = sorted(pop.routes, key=lambda x: x.route_score)
    return pop
