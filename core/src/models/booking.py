from dataclasses import dataclass
from datetime import date

@dataclass
class Booking:
    id: int
    user_id: int
    booking_date: date
    status: str
    trip_id: int
