import core
from adapters import repositories
from factories import config


def get_view_available_trips_use_case() -> core.GetAvailableTrips:
    db = next(config.get_db())
    trip_repository = repositories.SQLAlchemyTripRepository(session=db)
    return core.GetAvailableTrips(trip_repository=trip_repository)
