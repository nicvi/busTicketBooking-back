from core.src.models.booking import Booking
from core.src.repositories.booking_repository import BookingRepository


class GetBookingById:
    def __init__(self, booking_repository: BookingRepository):
        self.booking_repository = booking_repository

    def execute(self, booking_id: int) -> Booking:
        print(f"===> GetBookingById/execute/booking_id: {booking_id}")
        return self.booking_repository.get_booking_by_id(booking_id)
