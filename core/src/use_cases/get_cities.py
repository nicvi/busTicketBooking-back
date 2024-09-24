from .. import repositories


class GetCities:
    def __init__(self, city_repository: repositories.CityRepository):
        self.city_repository = city_repository

    def execute(self) -> list[str]:
        return self.city_repository.get_available_cities()
