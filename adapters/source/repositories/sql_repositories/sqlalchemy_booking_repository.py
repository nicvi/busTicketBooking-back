from sqlalchemy.orm import Session

from core.src.models.booking import Booking
from core.src.repositories.booking_repository import BookingRepository


class SQLAlchemyBookingRepository(BookingRepository):
    def __init__(self, session: Session):
        self.session = session

    def save_booking(self, booking: Booking):
        pass

    def get_bookings_by_user_id(self, user_id: int) -> list[Booking]:
        pass

    def create_booking(self, booking: Booking) -> Booking:
        self.session.add(booking)
        self.session.commit()
        self.session.refresh(booking)
        return booking

    def get_booking_by_id(self, booking_id: int) -> Booking:
        pass
