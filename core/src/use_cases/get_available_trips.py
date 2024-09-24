from datetime import datetime

from .. import models
from .. import repositories


class GetAvailableTrips:
    def __init__(self, trip_repository: repositories.TripRepository):
        self.trip_repository = trip_repository

    def execute(self, origin_city: str, destination_city: str, departure_date: datetime) -> list[models.Trip]:
        trips = self.trip_repository.get_available_trips(origin_city, destination_city, departure_date)
        return trips
