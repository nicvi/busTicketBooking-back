import core
from adapters import repositories
from factories import config


def get_cities_use_case() -> core.GetCities:
    db = next(config.get_db())
    city_repository = repositories.SQLAlchemyCityRepository(session=db)
    return core.GetCities(city_repository=city_repository)
