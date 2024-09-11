from abc import ABC, abstractmethod
from core.src.models.booking import Booking
from typing import List

class BookingRepository(ABC):
    @abstractmethod
    def save_booking(self, booking: Booking):
        pass

    @abstractmethod
    def get_booking_by_id(self, booking_id: int) -> Booking:
        pass

    @abstractmethod
    def get_bookings_by_user_id(self, user_id: int) -> List[Booking]:
        pass
