from adapters.src.repositories.sql_repositories.sqlalchemy_city_repository import SQLAlchemyCityRepository
from core.src.use_cases.get_cities import GetCitiesUseCase
from factories.config.db_connection import SessionLocal


def get_cities_use_case():
    db = SessionLocal()
    city_repository = SQLAlchemyCityRepository(session=db)
    return GetCitiesUseCase(city_repository=city_repository)
