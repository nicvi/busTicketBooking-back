from abc import ABC, abstractmethod
from datetime import datetime

from .. import models


class TripRepository(ABC):
    @abstractmethod
    def get_trip_by_id(self, trip_id: int) -> models.Trip:
        pass

    @abstractmethod
    def get_available_trips(
            self,
            origin_city: str,
            destination_city: str,
            departure_date: datetime
    ) -> list[models.Trip]:
        pass

    @abstractmethod
    def update_seats_occupied(self, trip_id: int, seats_occupied: int):
        pass
