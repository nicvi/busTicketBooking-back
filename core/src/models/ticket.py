from dataclasses import dataclass

from .. import models


@dataclass
class Ticket:
    ticket_id: int
    booking_id: models.Booking
    seat_number: int
