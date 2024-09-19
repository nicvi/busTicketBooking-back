from adapters.src.repositories.sql_repositories.sqlalchemy_booking_repository import \
    SQLAlchemyBookingRepository
from core.src.use_cases.get_booking_by_id import GetBookingById
from factories.config.sql_alchemy_session import get_db


def get_booking_by_id_use_case() -> GetBookingById:
    print("===> get_booking_by_id_use_case")
    db = next(get_db())
    booking_repository = SQLAlchemyBookingRepository(session=db)
    return GetBookingById(booking_repository=booking_repository)
