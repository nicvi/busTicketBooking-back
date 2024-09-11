from pip._internal.utils import datetime

from core.src.repositories.trip_repository import TripRepository


class GetAvailableTripsUseCase:
    def __init__(self, trip_repository: TripRepository):
        self.trip_repository = trip_repository

    def execute(self, origin_city: str, destination_city: str, departure_date: datetime):
        trips = self.trip_repository.get_available_trips(origin_city, destination_city, departure_date)
        return trips
