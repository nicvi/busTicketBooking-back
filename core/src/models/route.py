from dataclasses import dataclass
from datetime import datetime


@dataclass
class Route:
    route_id: int
    origin_city: str
    destination_city: str
    departure_date: datetime
