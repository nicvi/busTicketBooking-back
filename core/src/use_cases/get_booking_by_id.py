from core.src.repositories.booking_repository import BookingRepository
from core.src.models.booking import Booking


class GetBookingById:
    def __init__(self, booking_repository: BookingRepository):
        self.booking_repository = booking_repository

    def execute(self, booking_id: int) -> Booking:
        return self.booking_repository.get_booking_by_id(booking_id)
