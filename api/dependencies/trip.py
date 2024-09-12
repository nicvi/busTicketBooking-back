from adapters.src.repositories.sql_repositories.sqlalchemy_trip_repository import SQLAlchemyTripRepository

from core.src.use_cases.get_available_trips import GetAvailableTrips
from factories.config.sql_alchemy_session import get_db


def get_view_available_trips_use_case() -> GetAvailableTrips:
    db = next(get_db())
    trip_repository = SQLAlchemyTripRepository(session=db)
    return GetAvailableTrips(trip_repository=trip_repository)
