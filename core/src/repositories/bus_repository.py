from abc import ABC, abstractmethod

from core.src.models.bus import Bus


class BusRepository(ABC):
    @abstractmethod
    def get_bus_by_id(self, bus_id: int) -> Bus:
        pass

    @abstractmethod
    def get_all_buses(self) -> list[Bus]:
        pass

    @abstractmethod
    def save_bus(self, bus: Bus):
        pass
