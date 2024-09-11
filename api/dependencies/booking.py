from adapters.source.repositories.sql_repositories.sqlalchemy_booking_repository import SQLAlchemyBookingRepository
from core.src.use_cases.create_booking import CreateBookingUseCase
from core.src.use_cases.cancel_booking import CancelBookingUseCase
from core.src.repositories.trip_repository import TripRepository
from core.src.repositories.ticket_repository import TicketRepository
from core.src.use_cases.get_booking import GetBookingUseCase
from factories.config.sql_alchemy_session import get_db


def get_create_booking_use_case() -> CreateBookingUseCase:
    return CreateBookingUseCase(
        # booking_repository=BookingRepository(),
        trip_repository=TripRepository(),
        ticket_repository=TicketRepository(),
    )

def get_cancel_booking_use_case() -> CancelBookingUseCase:
    return CancelBookingUseCase(
        # booking_repository=BookingRepository(),
        trip_repository=TripRepository(),
        ticket_repository=TicketRepository(),
    )

def get_booking_use_case() -> GetBookingUseCase: # who/where call the implemented repository??
    db = next(get_db())
    booking_repository = SQLAlchemyBookingRepository(session=db)
    return GetBookingUseCase(booking_repository=booking_repository)
