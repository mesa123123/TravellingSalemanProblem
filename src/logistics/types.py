from dataclasses import dataclass


@dataclass
class Road:
    depature_city: int
    arrival_city: int
    route_length: float


@dataclass
class Destination:
    visit_number: int
    current_city: int
    travelled_route: Road


type Route = list[Destination]
