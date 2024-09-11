from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Session

from adapters.src.repositories.db_models import RouteSql, BusSql, TripSql
from core.src.models.trip import Trip
from core.src.repositories.trip_repository import TripRepository


class SQLAlchemyTripRepository(TripRepository):
    def __init__(self, session: Session):
        self.session = session

    def update_seats_occupied(self, trip_id: int, seats_occupied: int):
        pass

    def get_trip_by_id(self, trip_id: int) -> Trip:
        pass

    def get_available_trips(
            self,
            origin_city: str,
            destination_city: str,
            departure_date: datetime
    ) -> list[Trip]:
        fetched_trips = (
            self.session.query(TripSql.id.label('trip_id'),
                               BusSql.bus_number,
                               RouteSql.origin_city,
                               RouteSql.destination_city,
                               RouteSql.departure_date,
                               TripSql.seats_occupied)
            .join(BusSql, TripSql.bus_id == BusSql.id)
            .join(RouteSql, TripSql.route_id == RouteSql.id)
            .filter(
                RouteSql.origin_city == origin_city,
                RouteSql.destination_city == destination_city,
                func.date(RouteSql.departure_date) == departure_date.date()
            )
        ).all()
        return []
