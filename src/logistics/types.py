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


type Route_Network = list[Road]
type Route = list[Destination]
