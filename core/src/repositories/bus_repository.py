from abc import ABC, abstractmethod

from .. import models


class BusRepository(ABC):
    @abstractmethod
    def get_bus_by_id(self, bus_id: int) -> models.Bus:
        pass

    @abstractmethod
    def get_all_buses(self) -> list[models.Bus]:
        pass

    @abstractmethod
    def save_bus(self, bus: models.Bus):
        pass
