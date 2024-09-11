from dataclasses import dataclass
from datetime import datetime

from core.src.models.booking import Booking


@dataclass
class Payment:
    payment_id: int
    booking: Booking
    payment_method: str
    payment_status: str
    payment_date: datetime