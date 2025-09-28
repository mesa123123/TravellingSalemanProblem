from numpy import ndarray
from numpy.random import default_rng

from src.logistics.types import Road, Route_Network


def create_route_network(num_cities: int, road_length_limit: float) -> Route_Network:
    rnd = default_rng()
    city_weights: ndarray = rnd.uniform(low=1, high=road_length_limit, size=(num_cities, num_cities))
    route_network: Route_Network = [
        Road(depature_city=i + 1, arrival_city=j + 1, route_length=round(city_weights[i][j], 3))
        for i in range(num_cities)
        for j in range(i + 1, num_cities)
    ]
    return route_network
