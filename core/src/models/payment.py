from dataclasses import dataclass
from datetime import date

from core.src.models.booking import Booking


@dataclass
class Payment:
    id: int
    booking: Booking
    payment_method: str
    status: str
    payment_date: date
