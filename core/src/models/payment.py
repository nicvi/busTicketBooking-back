from dataclasses import dataclass
from datetime import date

from .. import models


@dataclass
class Payment:
    id: int
    booking: models.Booking
    payment_method: str
    status: str
    payment_date: date
