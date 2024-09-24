from sqlalchemy.orm import Session

import core


class SQLAlchemyBookingRepository(core.BookingRepository):
    def __init__(self, session: Session):
        self.session = session

    def save_booking(self, booking: core.Booking):
        pass

    def get_bookings_by_user_id(self, user_id: int) -> list[core.Booking]:
        pass

    def create_booking(self, booking: core.Booking) -> core.Booking:
        pass

    def get_booking_by_id(self, booking_id: int) -> core.Booking:
        pass
