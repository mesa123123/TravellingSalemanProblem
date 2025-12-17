from dataclasses import dataclass
from typing import Optional

type Itinerary = list[Destination]
type RoadNetwork = list[Road]


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
    itinerary: Itinerary
    route_score: float
