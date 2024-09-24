from datetime import datetime

from ..... import sql_repositories


def test_get_available_trips(db_session_mock):
    session = db_session_mock
    trip_repository = sql_repositories.SQLAlchemyTripRepository(session)
    origin_city = "CityA"
    destination_city = "CityB"
    departure_date = datetime(2024, 9, 25)

    available_trips = trip_repository.get_available_trips(origin_city, destination_city, departure_date)

    assert len(available_trips) == 1
    assert available_trips[0]['trip_id'] == 1
    assert available_trips[0]['bus_number'] == "1234"
    assert available_trips[0]['origin_city'] == "CityA"
    assert available_trips[0]['destination_city'] == "CityB"
    assert available_trips[0]['departure_date'].date() == departure_date.date()
    assert available_trips[0]['seats_occupied'] == 0