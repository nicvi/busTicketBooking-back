from .. import models
from .. import repositories



class GetBookingById:
    def __init__(self, booking_repository: repositories.BookingRepository):
        self.booking_repository = booking_repository

    def execute(self, booking_id: int) -> models.Booking:
        return self.booking_repository.get_booking_by_id(booking_id)
