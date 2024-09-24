from abc import ABC, abstractmethod

from .. import models


class BookingRepository(ABC):
    @abstractmethod
    def save_booking(self, booking: models.Booking):
        pass

    @abstractmethod
    def get_booking_by_id(self, booking_id: int) -> models.Booking:
        pass

    @abstractmethod
    def get_bookings_by_user_id(self, user_id: int) -> list[models.Booking]:
        pass
