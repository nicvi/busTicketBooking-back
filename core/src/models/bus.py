from dataclasses import dataclass
from typing import List


@dataclass
class Bus:
    bus_id: int
    bus_number: str
    number_of_seats: int
    amenities: List[str]
