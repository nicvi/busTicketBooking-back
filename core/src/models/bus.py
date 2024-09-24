from dataclasses import dataclass


@dataclass
class Bus:
    bus_id: int
    bus_number: str
    number_of_seats: int
    amenities: list[str]
