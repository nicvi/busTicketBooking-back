from dataclasses import dataclass
from datetime import datetime

@dataclass
class Booking:
    id: int
    user_id: int
    booking_date: datetime
    status: str
    trip_id: int