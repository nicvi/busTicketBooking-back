from adapters.src.repositories.sql_repositories.sqlalchemy_city_repository import \
    SQLAlchemyCityRepository
from core.src.use_cases.get_cities import GetCities
from factories.config.db_connection import SessionLocal


def get_cities_use_case() -> GetCities:
    db = SessionLocal()
    city_repository = SQLAlchemyCityRepository(session=db)
    return GetCities(city_repository=city_repository)
