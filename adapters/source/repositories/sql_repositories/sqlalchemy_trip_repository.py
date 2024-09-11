from datetime import date,datetime
from sqlite3 import Date

from sqlalchemy import cast, func
from sqlalchemy.orm import Session

from adapters.source.repositories.db_models import RouteSql, BusSql, TripSql
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
            departure_date: str
    ) -> list[Trip]:
        print("===> SQLAlchemyTripRepository / get_available_trips")

        # result = self.session.query(TripSql).join(RouteSql).filter(
        #     RouteSql.origin_city == origin_city,
        #     RouteSql.destination_city == destination_city,
        #     RouteSql.departure_date == departure_date
        # ).all()

        # new_departure_date = datetime.strptime('2024-09-11', '%Y-%m-%d').date()
        # new_departure_date = datetime.today()
        new_departure_date = datetime(2024, 9, 15)
        print(f"===> date random: {Date.today()}")
        print(f"===> Date departure_date: {new_departure_date}")
        search_datetime = datetime(2024, 9, 10)
        print(f"===> origin_city: {origin_city}")

        result = (
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
                # func.date(RouteSql.departure_date) == search_datetime  # cast to ignore time
            )
        ).all()

        print(f"===> get_available_trips - result: {result}")
        #
        # # Print results
        # for trip in result:
        #     print(trip)
        return [Trip()]
        # return self.session.query(TripSql).all()
