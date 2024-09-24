from datetime import datetime
from typing import Any

from sqlalchemy import func, orm

from .. import db_models
import core


class SQLAlchemyTripRepository(core.TripRepository):
    def __init__(self, session: orm.Session):
        self.session = session

    def update_seats_occupied(self, trip_id: int, seats_occupied: int):
        pass

    def get_trip_by_id(self, trip_id: int) -> core.Trip:
        pass

    def get_available_trips(
            self,
            origin_city: str,
            destination_city: str,
            departure_date: datetime
    ) -> list[tuple[Any, ...]]:
        fetched_trips = (
            self.session.query(db_models.TripSql.id.label('trip_id'),
                               db_models.BusSql.bus_number,
                               db_models.RouteSql.origin_city,
                               db_models.RouteSql.destination_city,
                               db_models.RouteSql.departure_date,
                               db_models.TripSql.seats_occupied)
            .join(db_models.BusSql, db_models.TripSql.bus_id == db_models.BusSql.id)
            .join(db_models.RouteSql, db_models.TripSql.route_id == db_models.RouteSql.id)
            .filter(
                db_models.RouteSql.origin_city == origin_city,
                db_models.RouteSql.destination_city == destination_city,
                func.date(db_models.RouteSql.departure_date) == departure_date.date()
            )
        ).all()
        return fetched_trips
