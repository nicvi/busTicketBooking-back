from dataclasses import dataclass

from core.src.models.bus import Bus
from core.src.models.route import Route


@dataclass
class Trip:
    trip_id: int
    bus: Bus
    route: Route
    seats_occupied: int = 0
