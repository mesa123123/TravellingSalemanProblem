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

    def get_full_itinerary(self) -> dict[int, int]:
        return {dest.visit_number: dest.current_city for dest in self.itinerary}

    def set_full_itinerary(self, in_path: dict[int, int]) -> None:
        self.itinerary = [Destination(visit_number=k, current_city=v) for k, v in in_path.items()]
