# from dataclasses import dataclass
#
# from core.src.models.bus import Bus
# from core.src.models.route import Route
#
#
# @dataclass
# class Trip:
#     trip_id: int
#     bus: Bus
#     route: Route
#     seats_occupied: int = 0

from dataclasses import dataclass, field
from typing import Optional

from core.src.models.bus import Bus
from core.src.models.route import Route

@dataclass
class Trip:
    trip_id: Optional[int] = field(default=None)
    bus: Optional[Bus] = field(default=None)
    route: Optional[Route] = field(default=None)
    seats_occupied: int = 0