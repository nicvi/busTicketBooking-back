from typing import List

from sqlalchemy.orm import Session
from sqlalchemy import distinct

from adapters.source.repositories.db_models.route_sql import RouteSql
from core.src.repositories.city_repository import CityRepository


class SQLAlchemyCityRepository(CityRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_available_cities(self) -> List[str]:
        origin_cities = self.session.query(distinct(RouteSql.origin_city)).all()
        destination_cities = self.session.query(distinct(RouteSql.destination_city)).all()

        all_cities = set([city for (city,) in origin_cities + destination_cities])
        return list(all_cities)
