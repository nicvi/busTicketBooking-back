import unittest
from datetime import datetime
from unittest.mock import MagicMock

from core.src.repositories.trip_repository import TripRepository
from core.src.use_cases.get_available_trips import GetAvailableTrips


class TestGetAvailableTrips(unittest.TestCase):
    def setUp(self):
        self.mock_trip_repository = MagicMock(spec=TripRepository)

        self.get_available_trips = GetAvailableTrips(self.mock_trip_repository)

    def test_execute_with_valid_trips(self):
        origin_city = "Guayaquil"
        destination_city = "Machala"
        departure_date = datetime(2024, 9, 15)
        self.mock_trip_repository.get_available_trips.return_value = [
            {
                'trip_id': 1,
                'bus_number': '1234',
                'seats_occupied': 10,
            },
            {
                'trip_id': 2,
                'bus_number': '5678',
                'seats_occupied': 15,
            }
        ]

        trips = self.get_available_trips.execute(origin_city, destination_city, departure_date)

        self.mock_trip_repository.get_available_trips.assert_called_once_with(
            origin_city, destination_city, departure_date
        )
        self.assertEqual(len(trips), 2)
        self.assertEqual(trips[0]['trip_id'], 1)
        self.assertEqual(trips[1]['bus_number'], '5678')

    def test_execute_with_no_trips(self):
        origin_city = "Guayaquil"
        destination_city = "Cuenca"
        departure_date = datetime(2024, 9, 20)

        self.mock_trip_repository.get_available_trips.return_value = []
        trips = self.get_available_trips.execute(origin_city, destination_city, departure_date)

        self.mock_trip_repository.get_available_trips.assert_called_once_with(
            origin_city, destination_city, departure_date
        )
        self.assertEqual(trips, [])
