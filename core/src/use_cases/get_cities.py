from core.src.repositories.city_repository import CityRepository


class GetCities:
    def __init__(self, city_repository: CityRepository):
        self.city_repository = city_repository

    def execute(self) -> list[str]:
        return self.city_repository.get_available_cities()
