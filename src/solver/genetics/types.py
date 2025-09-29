from dataclasses import dataclass

from logistics.types import Route


@dataclass
class RoutePopulation:
    population_size: int
    num_of_cities: int
    routes: list[Route]
