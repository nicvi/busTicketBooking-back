from abc import ABC, abstractmethod
from typing import List

class CityRepository(ABC):
    @abstractmethod
    def get_available_cities(self) -> List[str]:
        pass
