import core
from factories import config
from adapters import repositories

def get_booking_by_id_use_case() -> core.GetBookingById:
    db = next(config.get_db())
    booking_repository = repositories.SQLAlchemyBookingRepository(session=db)
    return core.GetBookingById(booking_repository=booking_repository)
