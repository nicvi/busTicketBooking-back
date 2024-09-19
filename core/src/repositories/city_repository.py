from abc import ABC, abstractmethod


class CityRepository(ABC):
    @abstractmethod
    def get_available_cities(self) -> list[str]:
        pass
