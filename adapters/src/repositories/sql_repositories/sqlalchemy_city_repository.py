from sqlalchemy import distinct, orm

import core

from .. import db_models


class SQLAlchemyCityRepository(core.CityRepository):
    def __init__(self, session: orm.Session):
        self.session = session

    def get_available_cities(self) -> list[str]:
        origin_cities = self.session.query(distinct(db_models.RouteSql.origin_city)).all()
        destination_cities = self.session.query(distinct(db_models.RouteSql.destination_city)).all()

        all_cities = set([city for (city,) in origin_cities + destination_cities])
        return list(all_cities)
