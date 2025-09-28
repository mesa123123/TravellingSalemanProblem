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
    arrived_by_road: Road


type Route_Network = list[Road]
type Route = list[Destination]
