from dataclasses import dataclass
from typing import Optional


@dataclass
class Road:
    departure_city: int
    arrival_city: int
    road_length: float


@dataclass
class Destination:
    visit_number: int
    current_city: int
    arrived_by_road: Optional[Road] = None


@dataclass
class Route:
    itinerary: list[Destination]
    route_score: float


@dataclass
class RoutePopulation:
    population_size: int
    num_of_cities: int
    routes: list[Route]


type RoadNetwork = list[Road]
