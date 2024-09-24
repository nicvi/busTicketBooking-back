import pytest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from adapters import BusSql, RouteSql, TripSql, Base


@pytest.fixture(scope="module")
def db_session_mock():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

    mock_session = sessionmaker(bind=engine)
    session = mock_session()

    bus = BusSql(bus_number="1234", number_of_seats=50)
    route = RouteSql(origin_city="CityA", destination_city="CityB", departure_date=datetime(2024, 9, 25))
    trip = TripSql(bus_id=1, route_id=1, seats_occupied=0)

    session.add(bus)
    session.add(route)
    session.add(trip)
    session.commit()

    yield session

    session.close()
