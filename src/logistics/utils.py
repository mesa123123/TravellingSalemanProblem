from numpy import ndarray
from numpy.random import default_rng

from src.logistics.types import Road, Route, Route_Network


def create_route_network(num_cities: int, road_length_limit: float) -> Route_Network:
    rnd = default_rng()
    city_weights: ndarray = rnd.uniform(low=1, high=road_length_limit, size=(num_cities, num_cities))
    route_network: Route_Network = [
        Road(depature_city=i + 1, arrival_city=j + 1, route_length=round(city_weights[i][j], 3))
        for i in range(num_cities)
        for j in range(i + 1, num_cities)
    ]
    return route_network


def create_route(num_cities: int, network: Route_Network) -> Route:
    pass


def get_best_distance(route, roads):
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


def distance_check(route, roads):
    number_of_cities = int(len(roads)) - 1
    distance = []
    # append the distance from the hometown to the first stop
    try:
        distance.append(roads[1][route[0]])
    except IndexError:
        print("Error: ", route[0])
    for i in range(1, number_of_cities - 1):
        if i < number_of_cities - 1:
            a = route[i - 1]
            b = route[i]
        else:
            a = route[number_of_cities - 1]
            b = route[0]
        try:
            distance.append(roads[a][b])
        except IndexError:
            print("Error: ", route[0])
            print(i)
    return sum(distance)
