from abc import ABC, abstractmethod
from core.src.models.trip import Trip

class TripRepository(ABC):
    @abstractmethod
    def get_trip_by_id(self, trip_id: int) -> Trip:
        pass

    @abstractmethod
    def get_available_trips(self, origin_city: str, destination_city: str, departure_date: str) -> list[Trip]:
        pass

    @abstractmethod
    def update_seats_occupied(self, trip_id: int, seats_occupied: int):
        pass
