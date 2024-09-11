from dataclasses import dataclass

from core.src.models.booking import Booking


@dataclass
class Ticket:
    ticket_id: int
    booking_id: Booking
    seat_number: int
