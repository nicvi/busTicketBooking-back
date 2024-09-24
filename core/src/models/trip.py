from dataclasses import dataclass

from .. import models


@dataclass
class Trip:
    trip_id: int
    bus: models.Bus
    route: models.Route
    seats_occupied: int = 0
